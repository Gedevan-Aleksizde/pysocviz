#! /usr/bin/env python
# -*- coding: utf-8 -*-
from plotnine import geom_text, geom_label
from ..misc.constants import arrow_type


def make_adjust_text_args(arrow=None, arrowstyle=None, **kwargs):
    at = {}
    if not arrow:
        arrow = 'none'
        at['arrowprops'] = {'arrowstyle': arrow_type[arrow]}
    else:
        at['arrowprops'] = {}
    if arrowstyle:
        at['arrowprops']['arrowstyle'] = arrowstyle
    if kwargs.get('size'):
        at['arrowprops']['lw'] = kwargs.get('size')
    if kwargs.get('color'):
        at['arrowprops']['color'] = kwargs.get('color')
    if kwargs.get('alpha'):
        at['arrowprops']['alpha'] = kwargs.get('alpha')
    return at


def geom_text_repel(arrow=None, arrowstyle=None, **kwargs):
    """
    :param arrow: str. one of 'last', 'first', 'both'
    :param arrowstyle: str
    :param kwargs:
    :return: plotnine.geoms.geom_text.geom_text
    """
    gt = geom_text(adjust_text=make_adjust_text_args(arrow, arrowstyle, **kwargs), **kwargs)
    return gt


def geom_label_repel(arrow=None, arrowstyle=None, **kwargs):
    """
    :param arrow: str. one of 'last', 'first', 'both'
    :param arrowstyle: str
    :param kwargs:
    :return: plotnine.geoms.geom_label.geom_label
    """
    gl = geom_label(adjust_text=make_adjust_text_args(arrow, arrowstyle, **kwargs), **kwargs)
    return gl
