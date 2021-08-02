# An Unofficial Package for Python Users Who Are Interested in the Practical and Modern Data Visualization

実践的でモダンなデータビジュアライゼーションに関心のある Python ユーザのための socviz 非公式移植パッケージ

## このパッケージが提供するもの

1. [socviz](https://github.com/kjhealy/socviz) のデータセットの pandas 移植版
2. Healy "[Data Visualization: A Practical Introduction](https://socviz.co/)" の作図サンプルコードの Python 版
3. Python でストレスなくグラフを描くためのいくつかのユーティリティ関数

## インストール方法

```shs
pip install git+https://github.com/Gedevan-Aleksizde/pysocviz.git
```

または, clone してからインストール

```sh
git clone git@github.com:Gedevan-Aleksizde/pysocviz.git
cd pysocviz
pip install ./
```

conda 等他の管理ツールで github リポジトリからインストールする方法は各自調べてください

## 使い方

以下のコードで必要なものをインポートできます.

```python
from pysocviz.reader import load_dataset
from pysocviz.properties import colors, linetypes
from pysocviz.utils import redefine_cat_with_na
```

詳細は `notebooks` 内の作例を見てください.