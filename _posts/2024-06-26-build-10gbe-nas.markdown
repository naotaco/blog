---
layout: single
title: NASを作ってデータ置き場を移行した
date: 2024-06-26 03:31:22 +09:00
categories: PC NAS 買った
header:
  image: /assets/images/posts/10gbe-nas/nas-header.webp
---

写真や動画を内蔵HDDに置いていたのだが、容量・性能ともに限界を感じていたため、強いNASを作ってそちらに移行した。

### 元の状態と課題

写真や動画をはじめとするデータが10TB少々あり、これを内蔵HDDに全て入れていた。近い容量のRAID1の安いNASを置き、そこにWindowsのアプリ（BunBackup）を使って毎日バックアップをしていた。またたまにUSB接続のHDDにもバックアップを別途とっていた。

またWindowsシステムや比較的小さくランダムアクセスが必要なデータ（各種ソースコードやLightroomのカタログなど）は内蔵のSSDに置いていた。

この状況を図にするとこのようになる。

![](/assets/images/posts/10gbe-nas/diagram-before.png){:width="90%" .align-center}

主なワークフローとしては、Lightroomで画像をSDカードからHDDにコピーしてインポートし、現像したJPEGファイルをOneDriveに出力して保存するような感じ。動画の場合もLightroomでコピーして、DaVinci Resolveで編集、出力先は同じくOneDriveとしている。

大きな問題はなく運用できていたのだが、RAWデータや元動画が置かれるHDDの容量が常に逼迫しているという問題があった。今回も2年前に大きなサイズにしたばかりのHDDが一杯になってしまったため、容量の増加が急務となっていた。

またHDDなのでアクセスが遅いという問題もあった。特に50MP以上のRAW画像を現像しているとHDDアクセスが詰まるのか長時間（30秒～）Lightroomの画像が表示できないこともあり、こちらも対策が必要であった。

### 要件と機種選定・調達

前出の課題を解消するため、あたらしいストレージを用意することにする。

単にHDDを大きくするだけだと性能の問題が解決できないため、10GbEのNASを作り、そこにHDDのデータをすべて移す方向で考えた。

- 実容量：25TB以上
  - 現データが約11TBあり、直近は2.5TB/年でデータが増えていることを踏まえ、この先5年使える容量を設定
- 性能：シーケンシャルリードで500MB/s以上
  - 特に根拠はないが、これくらいは出てくれないと高速化の恩恵を感じられないと思ったため
  - これを実現するためにはSSDキャッシュと10GbEに対応している必要がある
- HDDが4～6本入ること
  - 4本で運用を開始し、容量が不足したら増やせる状態がよい

国内メーカーのNASはいまひとつ買う気にならないので、QNAPとSynologyのラインナップを見ながら考えていた。Synologyは純正の10GbEボードが死ぬほど高いので躊躇していたのだが、MellanoxのNICをさせば動くという情報があり（後述）、合計で安くあがりそうなSynologyのDS1621+を買った。約15万円なり。QNAPは全体的にやや高く、ちょうどいい機種がなかったのが残念。

HDDは東芝のMG09で、泣く子も黙るエンタープライズグレードである。これを選んだのは単に18TBのHDDで一番安かったからなのだが、何にせよグレードが高いのは良いことである。1本あたり約4.5万円で、4本買ったら18万円になった。

SSDキャッシュの動作はReadのみか、Read&Writeを選ぶことができる。ReadキャッシュはSSDが壊れてもデータが失われることはないが、WriteキャッシュはSSDが破損した場合データ損失が発生する。このため、Writeキャッシュを有効にする場合はSSDを2枚用意してミラーリングできるようにしないといけない（SSDが1枚のときはWriteキャッシュの設定ができないようになっている）。

メインのユースケースにおいてシーケンシャル書き込みはメディアからの画像コピーになるので、メディアの速度より速い必要はない。CFeでも700MB/sあれば十分だ。余計なリスクを増やすのも気が進まないので、まずはReadキャッシュのみにすることとした。容量は1TBである。そこまで速度も必要ないのでコスパ重視でKIOXIAのExceria plus G3を買った。

あとはメモリ。

![](/assets/images/posts/10gbe-nas/10gbe-nas-1.webp){:width="70%" .align-center}

（つづく）

### 結果



![](/assets/images/posts/10gbe-nas/10gbe-nas-2.webp){:width="70%" .align-center}

![](/assets/images/posts/10gbe-nas/10gbe-nas-3.webp){:width="70%" .align-center}

![](/assets/images/posts/10gbe-nas/10gbe-nas-4.webp){:width="70%" .align-center}

![](/assets/images/posts/10gbe-nas/diagram-after.png){:width="90%" .align-center}

![](/assets/images/posts/10gbe-nas/cdm_ds1621.png){:width="70%" .align-center}

![](/assets/images/posts/10gbe-nas/cdm_sn850.png){:width="70%" .align-center}






