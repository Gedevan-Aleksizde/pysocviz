# An Unofficial Package for Python Users Who Are Interested in the Practical and Modern Data Visualization

実践的でモダンなデータビジュアライゼーションに関心のある Python ユーザのための socviz 非公式移植パッケージ

## このパッケージが提供するもの

1. [socviz](https://github.com/kjhealy/socviz) のデータセットの pandas 移植版
2. Healy "[Data Visualization: A Practical Introduction](https://socviz.co/)" の作図サンプルコードの Python 版
3. Python でストレスなくグラフを描くためのいくつかのユーティリティ関数

## インストール方法

```sh
pip install git+https://github.com/Gedevan-Aleksizde/pysocviz.git
```

または, clone してからインストールしてください.

```sh
git clone git@github.com:Gedevan-Aleksizde/pysocviz.git
cd pysocviz
pip install ./
```


あるいは, Releases から ZIP をダウンロードして

```sh
pip install pysocviz-X.X.zip
```

Notebook の実行結果を再現するために, [poetry](https://python-poetry.org/) を使用してパッケージのバージョンを指定してインストールできます. poetry をインストールしていない場合は `pip install poetry` などでインストールできます. カレントディレクトリに `pyproject.toml` がある状態で以下を実行してください.

```sh
poetry install
```

`git clone` をするか, ZIPをダウンロードして展開すれば `pyproject.toml` は見つかります.

conda 等他の管理ツールで github リポジトリからインストールする方法は各自調べてください

## 使い方

以下のコードで必要なものをインポートできます.

```python
from pysocviz.loader import load_dataset  # socviz のデータセット読み込み関数
from pysocviz.properties import *         # colorname, linetype
from pysocviz.utils import *              # 本文中で使ういくつかの便利関数
from pysocviz.p9extra import *            # geom_* theme_* など plotnine の関数として利用できるもの
```

詳細は [`notebooks/jp`](notebooks/jp) 内の作例を見てください.


## This package provides:

1. Pandas version of datasets in [socviz](https://github.com/kjhealy/socviz) 
2. Python version of the sample codes to emulate graphes in Healy's "[Data Visualization: A Practical Introduction](https://socviz.co/)"
3. Some functions to draw graphes more conveniently by Python

## Installation

```shs
pip install git+https://github.com/Gedevan-Aleksizde/pysocviz.git
```

Or, using `git clone`:

```sh
git clone git@github.com:Gedevan-Aleksizde/pysocviz.git
cd pysocviz
pip install ./
```

Or after downloading zip file from "Releases",

```sh
pip install pysocviz-X.X.zip
```

You can install full dependencies to run the notebooks by [poetry](https://python-poetry.org/). Download `pyproject.toml` from this repository, place it into the current directory, and run the below:

```sh
poetry install
```

## Usage

You can import all functions from this package:

```python
from pysocviz.loader import load_dataset  # to load datasets
from pysocviz.properties import *         # colorname, linetype name dictionaries
from pysocviz.utils import *              # some utility functions
from pysocviz.p9extra import *            # extra plotnine functions like geom_* theme_*
```

See [`notebooks`](notebooks/) in detail.
