#! /usr/bin/env python
# -*- coding: utf-8 -*-

def copy_docstr(fromojb):
    def wrapper(tg):
        tg.__doc__ = fromojb.__doc__
        return(tg)
    return wrapper