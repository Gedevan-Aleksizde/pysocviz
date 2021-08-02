#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np


def redefine_cat_with_na(series, ordered=None, na_label='NA'):
    """
    Redefine a categorical variable with missing values.
    :param series: `pandas.Series object`.
    :param ordered: Whether `Series` is ordered or not, default is `None`
    :param na_label: Actually label of na value, default is `NA`. You need to avoid conflict with existing category values.
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
