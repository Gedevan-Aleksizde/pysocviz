#! /usr/bin/env python
# -*- coding: utf-8 -*-
from textwrap import wrap


def wrap_format(width):
    def f(labels):
        return ['\n'.join(wrap(text, width)) for text in labels]
    return f


label_format = wrap_format
