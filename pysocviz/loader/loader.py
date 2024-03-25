#! /usr/bin/env python
# -*- coding: utf-8 -*-

try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources
from .. import data
import json
import pandas as pd

with pkg_resources.path(data, 'schema.json') as p:
    with open(p, 'r') as f:
        SCHEMA = json.load(f)

map_dtype_base = {
    'factor': lambda x: pd.Categorical(x),
    'integer': lambda x: pd.to_numeric(x, downcast='integer'),
    'character': lambda x : x.astype('str'),
    'Date': lambda x: x.astype('datetime64[ns]'),
    'numeric': lambda x: x.astype('float64'),
    'logical': lambda x: x.astype(bool)
    }

def convert_to_pandas_dtypes(df, df_schema):
    # 大人しく for ループとかで書いたほうが良かった気もする
    convert_funs = {
        c: (lambda col: lambda x:  map_dtype_base[
             df_schema[col]['class']
            ](x[col]) if df_schema[col]['class'] != 'factor' else pd.Categorical(
                x[col], categories=df_schema[col]['levels'],
                ordered=df_schema[col]['ordered']
                )
            )(c) for c in df.columns
    }
    return df.assign(**convert_funs)

def load_dataset(name):
    with pkg_resources.path(data, f'{name}.csv') as datfile:
        d = pd.read_csv(datfile, low_memory=False)
    convert_funs = {
        c: (lambda col: lambda x:  map_dtype_base[
             SCHEMA[name][col]['class']
            ](x[col]) if SCHEMA[name][col]['class'] != 'factor' else pd.Categorical(
                x[col], categories=SCHEMA[name][col]['levels'],
                ordered=SCHEMA[name][col]['ordered']
                )
            )(c) for c in d.columns
    }
    return d.assign(**convert_funs)

dataset_list = list(SCHEMA.keys())
