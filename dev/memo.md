## TODO

### 再現すべきユーティリティ関数は?

* setup_course_notes, color_pal, color_comp
* pandas でも十分簡単にできるので不要?:
  * int_to_year
  * %>%
  * %nin%
  * freq_tab
  * round_df
  * center_df
  * prefix_strip - 正規表現は自分で書けてほしいが statsmodels 自体あんまり使わないし...
  * prefix_replace
* lay_out は無理
* tw_tab は?
* その他本文で使われている他のパッケージの関数の擬似的な再現
* RQSS
* 座標系の変換はこれで正しいのか自信がない
* hrbrthemes っぽいテーマ
* plotnine の拡張関数をクラスで定義する

### TODO: 補足説明に必要なもの

* scale_color_* の使い分け: プリセットか手動か, 連続か質的か, 順序カテゴリか
* legend の位置がめちゃくちゃになるときの対処法
* 保存字・デバイスごとの出力の違いについての注意
* data=, mapping= は邪魔なので省略