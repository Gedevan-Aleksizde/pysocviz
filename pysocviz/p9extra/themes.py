#! /usr/bin/env python
# -*- coding: utf-8 -*-
from plotnine import theme, element_blank, element_rect, element_line, theme_light, element_text
from ..misc.constants import wsj_colors

def theme_map_pseudo():
    return theme(
        axis_title=element_blank(),
        axis_text=element_blank(),
        panel_grid=element_blank(),
        legend_title=element_blank(),
        legend_position=(.1, .1)
    )


def theme_economist(base_family=None, base_size=12, horizontal=True, dkpanel=False):
    ax_x, ax_y = (
        element_line(size=2, color='white'),
        element_blank()
    ) if horizontal else (element_line(size=2, color='white'), element_blank())
    panel_bg = element_rect(fill='#c3d6df') if dkpanel else element_blank()
    return theme_light(
        base_family=base_family, base_size=base_size
    ) + theme(
        plot_background=element_rect(fill='#d5e4eb'),
        panel_background=panel_bg,
        legend_background=element_blank(),
        legend_key=element_blank(),
        panel_grid_major_y=ax_y,
        panel_grid_minor_y=element_blank(),
        panel_grid_major_x=ax_x,
        panel_grid_minor_x=element_blank(),
        panel_border=element_blank(),
        axis_line_y=element_blank(),
        axis_line_x=element_line(),
        axis_ticks_major_x=element_line(color='black'),
        axis_ticks_major_y=element_blank()
    )


def theme_wsj(base_family=None, base_size=12, color="brown", title_family=None):
    return theme_light(
        base_family=base_family, base_size=base_size
    ) + theme(
        title=element_text(family=title_family),
        plot_background=element_rect(fill=wsj_colors[color]),
        panel_background=element_blank(),
        legend_background=element_blank(),
        legend_key=element_blank(),
        panel_border=element_blank(),
        panel_grid_major_y=element_line(linetype=':', size=2, color='black'),
        panel_grid_minor_y=element_blank(),
        panel_grid_major_x=element_blank(),
        panel_grid_minor_x=element_blank(),
        axis_line_x=element_line()
    )
