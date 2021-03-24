---
title: "ASUS EeePC X101 review (使用編)"
date: "2011-09-27"
categories: 
  - "何か"
  - "買った"
tags: 
  - "meego"
  - "pc"
  - "x101"
---

無事帰宅したので、さらにMeeGoを使ってみることにした。

とりあえず、山では暗くて見えなかったハードウェアまわりから見ていく。

まず何よりキーボード。

\[caption id="attachment\_229" align="aligncenter" width="400" caption="キーボード"\]![](https://blog.naotaco.com/assets/images/posts/2011/09/DSC056241-400x266.jpg "SONY DSC")\[/caption\]

（アメリカで買ったのだから当然だが）USキーボードなのはすばらしい。が、どう見ても変態配列。まず5列なのでF1-F12がFnと同時押し必須。そしてEscに追いやられたバッククオートがEnter右下にある（写真参照）。この微妙な配列と、極限まで浅いキーストローク、足りないキーの奥行きによって、とても打ちにくいキーボードが完成されている。最初から期待はしていないが。

\[caption id="attachment\_230" align="aligncenter" width="400" caption="右側面"\]![](https://blog.naotaco.com/assets/images/posts/2011/09/DSC05628-400x266.jpg "SONY DSC")\[/caption\]

そして右側面にはmicroSDスロットがある。普通のSDじゃないのは仕方ないのだろう。16GBのを調達してさしておいた。

左側面にはアダプタ差し込み口があるが、非常に細いプラグとなっていて心許ない。さすがに折れるようなことは無いだろうが、PSP用のアダプタのプラグよりだいぶ細いってどういうことなんだろう。

\[caption id="attachment\_231" align="aligncenter" width="400" caption="天板"\]![](https://blog.naotaco.com/assets/images/posts/2011/09/DSC05623-400x266.jpg "SONY DSC")\[/caption\]

そして天板は表面に細かい凹凸の加工がしてあるがプラの質感そのままの出来。パームレストと共通。微妙に手の脂が目立って悲しい。剛性は十分で、特に強度的な不安は覚えないのが凄い。

そして裏面のゴムをむしりとってネジをとり、フタをあけるとメモリとSSDにアクセスできる。

\[caption id="attachment\_232" align="aligncenter" width="400" caption="SSDとメモリ"\]![](https://blog.naotaco.com/assets/images/posts/2011/09/DSC05630-400x266.jpg "SONY DSC")\[/caption\]

左がPCI\_Express miniSSDで、ネジを1本外すと飛び上がってくる。予想に反して普通に交換できそうだったので、8GBで足りなければ適当に買って換装しよう。メモリは普通のDDR3 SO-DIMMっぽいけど、MAXが2GBらしいので、1回換装したら終わりですね（換える前提）。メモリがエルピーダだったのはポイント高い。

というわけで、ハードウェアとしては異常にチープだけど、値段のわりには遊べそうなので大変満足です。とりあえずお金が無いのでハードウェア的にはしばらくそのままかなあ。

 

で、日本語が入れられない件はSKKのかわりにAnthyを入れたら解決した。端末からscim-anthyパッケージを入れるだけなのだが、マネージャがZypperというものらしく、suになってから、

\# zypper install scim-anthy

とやったらインストールできた。yumだとパッケージは見つかったみたいだけどエラー。んでscimの設定かえてAnthyにしたら無事日本語が入力できるようになった。すばらしい。

ちなみにデフォルトで入ってるFacebookとTwitterクライアントは認証情報を忘れたり思い出したりするっぽくて（無線が安定していないだけか？）まったく使い物にならない。あとユーザ名がUser固定でパスワード1つでログインしたりsuしたりできるのが割と謎ではある。

基本的にLinuxを期待しているとMeeGoの使い勝手はまったく期待外れでしょうね。一応Chromiumと端末は使えるのでギリギリ耐えられるけど、近いうちにUbuntuに入れ換えることになると思う。
