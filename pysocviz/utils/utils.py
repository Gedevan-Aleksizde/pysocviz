#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from plotnine import (
    ggplot, aes, geom_pointrange, coord_flip, labs, geom_text, geom_tile,
    coord_fixed
)
from patsy import dmatrix
from ..misc.constants import gridcarto_us
from ..p9extra.themes import theme_map_pseudo

def prefix_strip(series):
    """
    clip verbose prefix (and brackets) from categorical term names
    For example:
    tidy_ols(ols_result).assign(term=lambda d: prefix_strip(d['term'])

    :param series: pandas.Series
    :return: pandas.Series
    """
    return series.str.replace(r"^.+?\[T\.(.+?)\]$", r"\1", regex=True)


def brackets_replace(series, sep=':'):
    """
    clip only brackets from categorical term names
    For example:
    tidy_ols(ols_result).assign(term=lambda d: prefix_strip(d['term'])

    :param series: pandas.Series
    :param sep: separator strings replaced with brackets
    :return: pandas.Series
    """
    return series.str.replace(r"^(.+?)\[T\.(.+?)\]$", f"\\1{sep}\\2", regex=True)


def redefine_cat_with_na(series, ordered=None, na_label='NA'):
    """
    Redefine a categorical variable with missing values.
    :param series: `pandas.Series object`.
    :param ordered: Whether `Series` is ordered or not, default is `None`
    :param na_label: Actually label of na value, default is `NA`.
    You need to avoid conflict with existing category values.
    :return: Categorical variable as `Pandas.Series`.
    """
    if series.dtype == pd.CategoricalDtype():
        cats = list(series.cat.categories) + [na_label]
        ordered = ordered if ordered else series.cat.ordered
    else:
        cats = series.fillna(na_label).astype(str).unique()
        ordered = ordered if ordered else False
    return pd.Categorical(
        series.astype(str).fillna(na_label).astype(str), cats, ordered=ordered
    )


def tidy_ols(ols_result, conf_int=False):
    tidy = pd.DataFrame(
        {
            'estimate': ols_result.params,
            'std_error': ols_result.bse,
            'statistic': ols_result.tvalues,
            'p_value': ols_result.pvalues
        }
    ).reset_index().rename(columns={'index': 'term'})
    if conf_int:
        tidy = pd.concat([
            tidy,
            ols_result.conf_int().reset_index(drop=True).rename(
                columns={0: 'conf_low', 1: 'conf_high'})
        ], axis=1)
    return tidy


def coefplot(fit, sort='natural', intercept=True, color='blue'):
    tidy = tidy_ols(fit, conf_int=True)
    for c in ['estimate', 'term', 'conf_low', 'conf_high']:
        if c not in tidy.columns:
            raise ValueError(f'column {c} not found in tidy dataframe.')
    if sort not in ['natural', 'magnitude', 'alphabetical']:
        raise ValueError(f'`sort` must be one of `natural`, `magnitude`, `alphabetical`. you specify `{sort}`')
    if not intercept:
        tidy = tidy.loc[lambda d: d['term'] != 'Intercept']
    if sort == 'magnitude':
        g = ggplot(tidy, aes(**dict(x='reorder(term, estimate)', y='estimate')))
    elif sort == 'alphabetical':
        g = ggplot(tidy.sort_values('term'), aes(**dict(x='term', y='estimate')))
    else:
        g = ggplot(tidy, aes(**dict(x='term', y='estimate')))
    return g + geom_pointrange(
        aes(**dict(ymin='conf_low', ymax='conf_high')), color=color
    ) + coord_flip(
    ) + labs(**dict(y='Value', x='Coefficient', title='Coefficient Plot'))


def cplot(fit, formula, data, at):
    """
    plotting ommitted, only a data frame.
    """
    funs = {
        name: 'mean' if dtype in [
            'float64', 'int64'
        ] else lambda col: col.value_counts(
        ).index[0] for name, dtype in zip(data.columns, data.dtypes)
    }
    aux = pd.DataFrame(data.agg(funs)).transpose()
    fixed = data[at].unique()
    x = pd.concat([aux.assign(**{at: val}) for val in fixed])
    cpv = fit.predict(x, linear=False)
    # statsmodels cannot return predictive intervals.
    # So I calculate that approximately by the delta method.
    # See this in detail:
    # https://stackoverflow.com/questions/47414842/confidence-interval-of-probability-prediction-from-logistic-regression-statsmode
    #
    # ugly trick!
    dmx = dmatrix(
        formula.split('~')[1],
        pd.concat([data] + [aux.assign(**{at: x}) for x in fixed])
    )[-fixed.shape[0]:, :]
    cov = np.array(fit.cov_params())
    gradient = (np.array(cpv) * (1 - np.array(cpv)) * dmx.T).T
    std_errors = np.array([np.sqrt(np.dot(np.dot(g, cov), g)) for g in gradient])
    c = 1.96
    upper = np.maximum(0, np.minimum(1, cpv + std_errors * c))
    lower = np.maximum(0, np.minimum(1, cpv - std_errors * c))
    return pd.DataFrame({'xvals': fixed, 'yvals': cpv, 'upper': upper, 'lower': lower})


def statebins(state_data, state_col='state', value_col='value',
              font_size=10, text_color="black", state_border_col=None):
    if state_data[state_col].apply(lambda x: len(x) > 2).any():
        print('merged by state names')
        dat = pd.DataFrame(gridcarto_us).merge(
            state_data.assign(**{state_col: lambda d: d[state_col].str.lower()}),
            left_on='__state__',
            right_on=state_col,
            how='left'
        )
    else:
        print('merged by abbreviations')
        dat = pd.DataFrame(gridcarto_us).merge(
            state_data.assign(**{state_col: lambda d: d[state_col].str.upper()}),
            left_on='__abbr__',
            right_on=state_col,
            how='left'
        )
    return ggplot(
        dat,
        aes(x='__x__', y='__y__', label='__abbr__')
    ) + geom_tile(
        aes(width=.9, height=.9, fill=value_col), color=state_border_col
    ) + geom_text(
        size=font_size, color=text_color
    ) + theme_map_pseudo() + coord_fixed()
