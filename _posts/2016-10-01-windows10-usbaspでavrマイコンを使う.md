---
layout: single
title: "Windows10 + usbaspでAVRマイコンを使う"
date: "2016-10-01"
categories: 
  - "tips"
  - "未分類"
tags: 
  - "avr"
  - "マイコン"
---

AVRマイコンとはAtmel社の製造しているマイコンである。Arduino(およびそのパチもん)に使われているのもAVRのMEGAシリーズというやつで、安くて小さく扱いやすいのが特徴である。他方、ほんとうに[素のマイコンのまま売ってる](https://www.google.co.jp/search?q=atmel+atmega88&client=firefox-b&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjH29ebtbLPAhXBpJQKHRpvA1AQ_AUICCgB&biw=1449&bih=994)ので、直接USBでPCにつないでスケッチをWriteみたいなそういうカジュアルな使い方はまったくできない。ライタと呼ばれる書き込み装置を使ってマイコンにバイナリを転送することになるわけだ。

このライタにはたくさんの種類があり、まあどれを使ってもいっしょだと思うのだが、買うとそこそこの値段\[ref\]といっても数千円なんだから、今考えれば買ってしまえばよかろうという感じである\[/ref\]する。そこでUSBaspというオープンソースのAVRライタを自作することになるわけで、ご多分に漏れず僕の手元には大学の先生に言われるがままに作ったUSBaspと秋月で衝動買いしたAVRマイコンが多数あるわけだ(ここまで8年前の知識)。

| ![AVRマイコンたち。ATMEGA88, ATTINY85など](https://blog.naotaco.com/assets/images/posts/2016/10/WP_20160929_00_52_57_Rich-400x300.jpg) |
|:--:|
|  AVRマイコンたち。ATMEGA88, ATTINY85など |

| ![学生時代に自作したusbasp](https://blog.naotaco.com/assets/images/posts/2016/10/WP_20160929_00_53_38_Rich-400x300.jpg) |
|:--:|
|  学生時代に自作したUSBasp |

久々にライタとAVRマイコンが出土したので是非いじってみようと思うわけだが、何も思い出せないし当時のPCもないし、なんならWindows10用のドライバなど全く提供されていないのでどこから手を付けて良いかわからぬ。

たぶん、必要なものはこれで足りるはずだ。

1. USBasp本体
2. USBaspのドライバ
3. AVRマイコン
4. AVRDUDE
5. avr-gcc

### 1． USBasp本体

このページを読んでいるくらいだから、あなたは昔作ったUSBaspを手元にもてあましているか、あるいはライタの自作を志しているのだろう。現在でも[USBaspのサイト](http://www.fischl.de/usbasp/)は残っているので、回路図とライタ用のファームウェアを入手することができる。しかしページを読むとわかるように、USBasp自体がAVRマイコン(ATmega8/88)でできている。AVRマイコンに書き込むためのライタを作るためにAVRマイコンにファームウェアを書き込む必要があるのだ。どういうことだよ。誰かまわりの人にたのむしかない。

今ならできあいのライタを買ってくるか、Arduinoなんかでも書き込めるようになってるという話も聞くので、どう考えてもそちらの方が賢いと思われる。が、そんなことはどうでもよいので本稿ではUSBaspを使って進めることにする。

### 2\. USBaspドライバ

さて、出土したUSBaspをPCにつなぐと、何らかのデバイスとして認識した音はする。当然だがドライバがなく使える状態にはならないので、適当に落としてきてドライバを当てようとすると、よく分からないエラーのようなものがでて進めない。これはドライバの問題というか、Windows8.1以降、ドライバの署名が必須になったことが原因である。この確認を無効にすることもできるが、回復コンソールから操作する必要があり非常に面倒だ。

 

<blockquote class="twitter-tweet" data-lang="en"><p dir="ltr" lang="ja"><a href="https://twitter.com/naotaco">@naotaco</a> Zadig使おう <a href="https://t.co/MM1XPPXu5v">https://t.co/MM1XPPXu5v</a></p>— おかもとけいじ (@mokusatsu) <a href="https://twitter.com/mokusatsu/status/778524563411841024">September 21, 2016</a></blockquote>

<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

 

などといっていたら[Zadig](http://zadig.akeo.ie/)というのを教えてもらった。理屈はまったく不明だが、とりあえずドライバに署名がなされるらしい？これ署名確認を無効化するのとどっちがマシなのだろうか……。とりあえず、公式ページにある[ドライバ](http://www.fischl.de/usbasp/)とZadigでUSBaspを認識するようになった。すごい。

### 3\. AVRマイコン

好きなのを買ってくればよい。いまでもよく使っていたATMEGA8系やATTINY系が現役でおじさんはうれしい。詳しいことはよくわからないが、ADコンバータが乗っている/いないの差分があったりするので、よくわからなければATMEGA88を買っておけば良いとおもう。

### 4\. AVRDUDE

ライタを使ってバイナリを転送するのに必要なプログラム。[公式ページ](http://www.nongnu.org/avrdude/)から今でもダウンロードできる。MinGW環境でコンパイルすることが出来る。ただしmsys2では不可だった。またドキュメントの通りに謎のオプションを設定しないとconfigureできなかった。

\[code lang="shell"\] set PREFIX=&amp;lt;your install directory path&amp;gt; export PREFIX gunzip -c avrdude-6.3.tar.gz | tar xf - cd avrdude-6.3 ./configure LDFLAGS="-static" --prefix=$PREFIX --datadir=$PREFIX --sysconfdir=$PREFIX/bin --enable-versioned-doc=no make make install \[/code\]

あとはインストール場所にパスを通せばOK.

### 5\. avr-gcc

もはやどこが正しい配布サイトなのかわからないが、[ここからコンパイル済みのバイナリが](http://andybrown.me.uk/2015/03/08/avr-gcc-492/)ダウンロードできる。解凍したら動いた。

### 動かす

ここまでやったのだからLチカくらいはしておきたい。下記Makefileとmain.cがあればC1ピンが上下するはずである。

https://gist.github.com/naotaco/1ce1f274504b5bf5cf28b8fb4db65fe5

https://gist.github.com/naotaco/f5a436dfefd35a407ca58b724ff33985

クロックをいじってあそんでいたので、内蔵8MHzで動作するようになっている。8,9行目を消せばデフォルトの内蔵1MHzで動作するので、省電力になる（はず）。そのときはF\_CPUの値を1/8に変更しないと、delayの時間が合わなくなってしまう。

別のマイコンを使う時はMakefileのatmega88のところを適宜書き換える。[たくさん選べる](http://www.nongnu.org/avr-libc/user-manual/index.html)が、m88, m8, tiny45, tiny2313くらいしか使ったことがない。そもそもどこで売ってるんだ。

USBasp以外のライタを使うときはavrdudeの-cオプションを変更すればよいはず。こちらも[たくさん選べる](http://www.nongnu.org/avrdude/user-manual/avrdude_4.html#Option-Descriptions)ので、秋月でAVRISPmkIIを買った場合でもだいじょうぶ。といっても、その場合は純正のリッチなAVR STUDIOで開発できそうだしどうにでもなりそうな感じはする。

上のMakefileとmain.cを置いたフォルダで、make　→　make flashとするとバイナリが転送される。また、avr-gcc同梱のavr-objdumpでavr-objdump.exe -d main.o とすると逆アセンブルもできる。べんりだが読めない。

<iframe src="https://vine.co/v/5n0ZYrivTFB/embed/simple" width="480" height="480" frameborder="0"></iframe>

<script src="https://platform.vine.co/static/scripts/embed.js"></script>

以上。
