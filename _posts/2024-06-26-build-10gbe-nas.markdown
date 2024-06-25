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

![](/assets/images/posts/10gbe-nas/diagram-before.png){:width="70%" .align-center}

主なワークフローとしては、Lightroomで画像をSDカードからHDDにコピーしてインポートし、現像したJPEGファイルをOneDriveに出力して保存するような感じ。動画の場合もLightroomでコピーして、DaVinci Resolveで編集、出力先は同じくOneDriveとしている。

大きな問題はなく運用できていたのだが、RAWデータや元動画が置かれるHDDの容量が常に逼迫しているという問題があった。今回も2年前に大きなサイズにしたばかりのHDDが一杯になってしまったため、容量の増加が急務となっていた。

またHDDなのでアクセスが遅いという問題もあった。特に50MP以上のRAW画像を現像しているとHDDアクセスが詰まるのか長時間（30秒～）Lightroomの画像が表示できないこともあり、こちらも対策が必要であった。

### 要件

### 結果

![](/assets/images/posts/10gbe-nas/10gbe-nas-1.webp){:width="70%" .align-center}

![](/assets/images/posts/10gbe-nas/10gbe-nas-2.webp){:width="70%" .align-center}

![](/assets/images/posts/10gbe-nas/10gbe-nas-3.webp){:width="70%" .align-center}

![](/assets/images/posts/10gbe-nas/10gbe-nas-4.webp){:width="70%" .align-center}

![](/assets/images/posts/10gbe-nas/cdm_ds1621.png){:width="70%" .align-center}

![](/assets/images/posts/10gbe-nas/cdm_sn850.png){:width="70%" .align-center}

![](/assets/images/posts/10gbe-nas/diagram-after.png){:width="70%" .align-center}




