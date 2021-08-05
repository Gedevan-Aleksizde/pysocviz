#! /usr/bin/env python
# -*- coding: utf-8 -*-
from plotnine import theme, element_blank

theme_map_pseudo = lambda: theme(
    axis_title=element_blank(),
    axis_text=element_blank(),
    panel_grid=element_blank(),
    legend_title=element_blank(),
    legend_position=(.1, .1)
)