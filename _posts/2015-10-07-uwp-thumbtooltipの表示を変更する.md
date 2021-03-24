---
title: "[UWP] ThumbToolTipの表示を変更する"
date: "2015-10-07"
categories: 
  - "tips"
tags: 
  - "uwp"
  - "windows10"
  - "windows10-mobile"
---

UWPでSliderを動かすと、デフォルトでカーソル？の上にラベルのような数値が表示される。

[![slider_1](https://blog.naotaco.com/wp-content/uploads/2015/10/slider_1.png)](https://blog.naotaco.com/wp-content/uploads/2015/10/slider_1.png)

だが数値だけ出られても困るような場合というのもある。単位を出したり、そもそも数値と微妙に違うリストからものを選ぶときとか。

このラベルというかヒントというか何かの表示を変えるために調べまくっていたのだが、この名前がThumbToolTipであるということを突き止めるのに9割くらいの時間を費やしていた。あああ。

ちなみにIsThumbToolTipEnabled にfalseを入れれば表示されなくなる。

で、Sliderの値から文字列を返すIValueConverterの実装を用意してあげて, そのインスタンスをThumbToolTipValueConverterにセットしてあげればよい。

https://gist.github.com/naotaco/007e752fd01493b521da

 

[![slider_2](https://blog.naotaco.com/wp-content/uploads/2015/10/slider_2.png)](https://blog.naotaco.com/wp-content/uploads/2015/10/slider_2.png)

こんなかんじで、値が1のときにbが表示される。
