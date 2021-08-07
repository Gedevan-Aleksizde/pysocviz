#! /usr/bin/env python
# -*- coding: utf-8 -*-
from plotnine import scale_color_manual, scale_fill_manual
from ..misc.constants import pander_colors, colorblind_colors, okabeito_colors_gray, okabeito_colors_black
from ..misc.innter_utils import copy_docstr


def scale_pander(func, **kwargs):
    """
    The colorblind and printer-friendly discrete color palette borrowed from `ggthemes::scale_color_pander`
    https://jrnold.github.io/ggthemes/
    :param kwargs: arguments of scale_*_manual except `values`
    :return:
    """
    return func(values=pander_colors, **kwargs)


@copy_docstr(scale_pander)
def scale_color_pander(**kwargs):
    return scale_pander(scale_color_manual, **kwargs)


scale_colour_pander = scale_color_pander


@copy_docstr(scale_pander)
def scale_fill_pander(**kwargs):
    return scale_pander(scale_fill_manual, **kwargs)


def scale_colorblind(func, **kwargs):
    """
    A colorblind safe qualitative discrete palette borrowed from `ggthemes::scale_color_colorblind`
    https://jrnold.github.io/ggthemes/
    :param kwargs: arguments of scale_*_manual except `values`
    :return:
    """
    return func(values=colorblind_colors, **kwargs)


@copy_docstr(scale_colorblind)
def scale_color_colorblind(**kwargs):
    return scale_colorblind(scale_color_manual, **kwargs)


scale_colour_colorblind = scale_color_colorblind


@copy_docstr(scale_colorblind)
def scale_fill_colorblind(**kwargs):
    return scale_colorblind(scale_fill_manual, **kwargs)


def scale_OkabeIto(func, use_black=True, order=None, **kwargs):
    """
    A discrete color palette from "Color Universal Design" by Okabe and Ito, http://jfly.iam.u-tokyo.ac.jp/color/.
    This function is Inspired by `colorblindr::scale_OkabeIto`.
    https://github.com/clauswilke/colorblindr
    :param use_black: bool. if True, black is included, otherwise gray.
    :param order: array-like, which elements are between 0-7 integers. order of color palette.
    The color palette has only 8 elements.
    :param kwargs:
    :return:
    """
    okabeito_colors = okabeito_colors_black if use_black else okabeito_colors_gray
    if not order:
        order = list(range(8))
    return func(
        values=[okabeito_colors[i] for i in order],
        **kwargs
    )


@copy_docstr(scale_OkabeIto)
def scale_color_OkabeIto(use_black=True, order=None, **kwargs):
    return scale_OkabeIto(scale_color_manual, use_black=use_black, order=order, **kwargs)


scale_colour_OkabeIto = scale_color_OkabeIto


@copy_docstr(scale_OkabeIto)
def scale_fill_OkabeIto(use_black=True, order=None, **kwargs):
    return scale_OkabeIto(scale_fill_manual, use_black=use_black, order=order, **kwargs)
