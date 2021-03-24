---
title: "Vaio ProのCPUクロックがまったく上がらない件"
date: "2015-02-17"
categories: 
  - "tips"
tags: 
  - "pc"
  - "vaiopro"
---

買ってからずっと困っていたのだが、ぐぐってもまったく出てこないため解決できずにいた件。Vaio ProのCPUクロックがロクに上がらない。CPU-Zで見てみると800-1000MHz近辺をうろうろしている。

[![vaio_800](https://blog.naotaco.com/assets/images/posts/2015/02/vaio_800.png)](https://blog.naotaco.com/assets/images/posts/2015/02/vaio_800.png)

さすがに話にならないので、調べまくっていた。

[http://news.mynavi.jp/articles/2013/09/02/vaio/005.html](http://news.mynavi.jp/articles/2013/09/02/vaio/005.html)

\# この辺を読んでいて、GPUの電源と関係がありそうということはわかっていた

もう何度目になるかわからないが、電源オプションを見直していると、Intel Graphics Settingという項目を発見。いつかの自分が最高のパフォーマンスを発揮じゃなどとほざいてMaximum Performanceを選択したらしい。

[![power_option](https://blog.naotaco.com/assets/images/posts/2015/02/power_option.png)](https://blog.naotaco.com/assets/images/posts/2015/02/power_option.png)

さきほどの記事が脳裏をよぎったので、これをBalancedにしてみると、CPUクロックがみるみる上がっていくのであった。。。まじかよ。Maximum Battery Lifeでもよさそう。

[![vaio_2700](https://blog.naotaco.com/assets/images/posts/2015/02/vaio_2700.png)](https://blog.naotaco.com/assets/images/posts/2015/02/vaio_2700.png)

体感的にももたつくことがなくなり大変満足である。なおバッテリは3-4時間しか持たない模様。あと、結局GPUを酷使する場面(Google mapなど)を開くと結局同じことが起こってCPUの電力が不足してクロックが落ちるっぽい。今更という感じだがメモしておく。
