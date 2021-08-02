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
  * prefix_strip
  * prefix_replace
* lay_out は無理
* tw_tab は?

TODO: 欠損値の扱い. Categorical にするときは None や NaN もレベルに含めないと pandas がうまく動かない (gss_sm)

TODO: plotnine の factor だったら大丈夫だったりする?

TODO: いつのまにか factor/reorder が特別に使えるようになっていた

TODO: Fig 3.17, viridis からカラーマップ変更する