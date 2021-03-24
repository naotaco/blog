---
title: "HP ProLiant MicroServer Gen8を買って地雷を順番に踏んでった話"
date: "2015-05-04"
categories: 
  - "tips"
  - "ダメ"
  - "何か"
  - "未分類"
tags: 
  - "esxi"
  - "ubuntu"
  - "サーバ"
---

NASにしてた自宅サーバが死んでしまったので、そのリプレースとしてタイトルの通り、Microserver Gen8を買った。HPのML310eを使ったときに割と調子がよかったので、同じでいいかなと。

\[amazon template=wishlist&asin=B00DDIC2P2\]

まずAmazonに出品していた「オフィス・モア (in 神戸)」という店に注文したところ、在庫が10点以上あったにも関わらず入荷未定と連絡がきた。「併売のため」とのことだが、更新が追いつかないペースでこのサーバが売れるとはとても思えないし、たいへん疑わしいと思っている。ということで、ぷらっとオンラインで再度注文。ここは以前も使ったことがあり、webに表示されてる通りに翌営業日に発送される(ただひとつ解せないのが、発送翌日、商品が届いた後になって発送の連絡をしてくるところ)。

ということで、無事届いた。

\[caption id="attachment\_787" align="aligncenter" width="225"\][![かっこいい](https://blog.naotaco.com/assets/images/posts/2015/05/WP_20150505_03_00_48_Pro-e1430762899641-225x300.jpg)](https://blog.naotaco.com/assets/images/posts/2015/05/WP_20150505_03_00_48_Pro.jpg) かっこいい\[/caption\]

デザインはいいかんじである。

今回かなりやけっぱちな記事です。

### はじめに

今回の要件はこちら。

- NASとしてsambaストレージを6TB用意する
- GbE上限くらいの速度
- RAID1 or 10
- ESXiで仮想化してお遊び用にVMを上げる余地を残す

用意したのは、

- サーバ本体
- ECCメモリ16GB(special thanks to [@s03785yh](https://twitter.com/s03785yh))
- WD Red 3TB 4本
- 東芝の適当な500GB 2.5inch HDD(MQ01ABD050)(後述)
- 東芝の適当なUSBメモリ(後述)

適当に手持ちのメモリをさしたところ、まったく起動しなかった。調べてみたところ、ECCが必要とのこと。それくらいは調べておきましょう。。

* * *

 

### パフォーマンスが出ない

まずは起動画面からRAIDコントローラの設定画面に入り、4つのドライブで1つのRAID10 arrayを作成する。6TiBのシングルボリュームができるので、再起動。

次はESXiのインストール。MicroServer Gen8に搭載されているRAIDコントローラのB120iはいわゆるFake RAIDなので、これをOSに見せるためにはドライバが必要になる。ESXiの場合はHPが[カスタムイメージを公開している](http://www8.hp.com/us/en/products/servers/solutions.html?compURI=1499005#tab=TAB4)ので、これを使うだけでよい。CD-Rに焼いて挿入、起動してインストール。ESXi5.5にするか6.0にするか迷うところであるが、どっちでもよい。どっちにしろうまくいかないから。ちなみに、 付属の2GBメモリだけだとESXiはインストールできない。ESXi5.5は開始段階でエラーを出してくれるのだが、6.0はインストール途中 で紫画面で死にます。ハードウェア要件チェック漏れっぽいですね。おとなしく要件どおり8GBだっけ？積んでおきましょう。

さて、ESXiのインストールはあっさり終わり、あとはお好きなOSをのせるだけ。とりあえず流行りっぽいFreeNASを入れてみるが、せっかく作ったRAIDストレージを認識しない。正確に書くと、見えてはいるがVolume作成が終わらない。このあたりで暗雲が立ちこめてくる。いくらやっても解決しないので、Ubutnuでsambaを動かす方向に方針を変更。

Ubuntuのインストールもあっさり終わり、ちゃんと5TBの仮想ディスクも認識された。これをsambaで見せるところまでできたので、Windowsのデスクトップマシンからデータフォルダ(1.8TB)を丸ごとFastCopyでバックアップを実行してみた。Windows側のタスクマネージャで900Mbpsくらい、100MB/sを超える速度が出てたいへん満足である。

が、転送を続けていくと、パフォーマンスが劇的に低下するポイントが来る。だいたい10GB, 10000ファイルを転送したあたりで速度が一気に落ちてきて、大きなファイルの転送中でも10Mbps(bit per sec.)あたりまでしか上がらなくなってくる。細かいファイルの転送ともなるともうダイアルアップ並み。昭和かよ。この間はsmbdがCPUを100%近く食いつぶしているのだが、vmstatで見てみるとwaitがけっこう高い比率を占めており、ストレージの問題という感じがしてくる。

sambaのパラメータいじったり、仮想ディスクの種類(lazy/eager zeroed)を変えたりして試してみるも、結果は全く変わらず。。。

ちなみにsambaのパラメータは、socket optionsをいじれとかいろいろと情報があるが、最近のsamba(4.1.6)ではまったく必要が無い。デフォルトのままでGbE上限は楽に出る（ただし初速のみ）

さすがに実用に耐えないのでいろいろ試してみるが、とにかくどうにもならない。ESXi5.5と6.0も試したし、FreeNASでも試した（Eager zeroedにしたらボリューム作成は出来た）が、傾向は同じ。ある程度のところで速度が一気にADSLレベルに落ちてそれっきり。ここまで1.5日くらいかかった。ESXiとかUbuntuのインストール, partedの操作に異常に慣れてきた。

* * *

 

### 自由度の著しく低いHPのサーバ

あと怪しいところは、ESXi自体のオーバーヘッドか、B120iの実力（仕様）である。

とりあえず前者を排除するため、サーバに直接何らかのOSを入れて検証してみたいところであるが、非情にもUbuntuやらDebianなどという下等なOSはサポート対象に入っていない。[HPのページ](http://h20564.www2.hp.com/hpsc/doc/public/display?sp4ts.oid=5379860&calledBy=Search_Result&docId=emr_na-c03898652-2&docLocale=ja_JP)に よると、RHEL, Windows Server, SUSE, ESXiの4択とのこと。いっそWindows serverにでもしてやろうかと思ったが踏みとどまった。この手はない。

こうなってはしょうがないので、B120iのFake RAIDが細かいファイルを思いっきり書き込むことに向いていないのだろうと思うことにして諦めるしかない（じゃあ何に向いているのだろうか）。そうなると、B120iのRAIDを無効にして(AHCIに設定して、そのままHDDが4台として使う)、OS上でRAIDを組むしかない。BIOSの設定からStorage controllerのモードをRAIDからAHCIに変更できる。

するといま載せてある4本のHDD以外に、OSを入れるディスクが必要になるわけで、筆者は夜な夜なヨドバシに寄って帰るのであった。

* * *

 

### 5台目のHDD

しょうがないので2.5インチのHDDを1本買ってきて、CDドライブのところにむりやり搭載した。せっかくだしHGSTのにしたかったが在庫が無く、東芝の適当なやつにした。

\[caption id="attachment\_800" align="aligncenter" width="400"\][![カジュアルに搭載された5台目](https://blog.naotaco.com/assets/images/posts/2015/05/WP_20150503_21_43_33_Pro-400x300.jpg)](https://blog.naotaco.com/assets/images/posts/2015/05/WP_20150503_21_43_33_Pro.jpg) カジュアルに搭載された5台目\[/caption\]

電源のコネクタが4ピンの小さいやつ（FDD用?）しか生えてないので、4ピンペリフェラルへの変換コネクタと、4ピン→SATA電源端子への変換コネクタを2重にかましてHDDにつなぐ。SATAケーブルは生えていなかったが、マザーボードにSATA ODDと記載がある端子が余っているので、そこにつないであげればOK。ちゃんと5台目のHDDとして認識される。が、ここにESXiをインストールしようとしたらインストーラが途中で止まった。追いかける気力もないので諦める。

もう仮想化はあきらめて、この5台目のディスクに直接Ubuntuをいれて、MBAなんかもここに書き込んで、そっから起動させることにした。さすがにインストールはあっさり済んだし、mdadmでRAID10組めばいいや、楽勝だわ、と思いつつ、再起動。

が、起動しない。Boot error.

調べていくと、こんな記事が見つかった: [http://jarrodla.blogspot.jp/2014/04/hp-microserver-gen8-boot-from-5th-sata.html](http://jarrodla.blogspot.jp/2014/04/hp-microserver-gen8-boot-from-5th-sata.html)

引用すると、

> I discovered that my HP Microserver Gen8 does not boot from the 5th SATA port (the Optical Bay) when the controller is in AHCI mode.

適当に訳すと、

> なんかコントローラをAHCIにしてると5番目のSATAポートからブートできないっぽい

とのこと。もうﾏﾁﾞ意味ゎかんなぃ。。。ﾘｽｹしょ。。。

あまりに意味が分からないので手が勝手にAmazonでUSBメモリをぽちっていた。32GB.

* * *

 

### 6つめのストレージ: USBメモリ

\[amazon template=wishlist&asin=B005IKC2N0\]

最近は安くていいね（棒

MicroServer様はマザーボード上のUSBコネクタに挿したUSBメモリからも起動できるのである。すばらしい。ここまで予見して設計していたのかしら？

というわけで、USBメモリにESXiをインストールする。

\[caption id="attachment\_789" align="aligncenter" width="400"\][![見飽きたやつ](https://blog.naotaco.com/assets/images/posts/2015/05/WP_20150502_001-400x300.jpg)](https://blog.naotaco.com/assets/images/posts/2015/05/WP_20150502_001.jpg) 見飽きたやつ\[/caption\]

これはあっさり終わった。

ただ、ESXiが起動してみると、足した500GBのHDDがうまく見えない。Windowsにいちどつないで、ちゃんとフォーマットしてあげたら見えるようになったので、データストアとして追加。するとまたこけたので、エラーメッセージでぐぐって[出てきたとおりに解決](http://kaede.jp/2013/10/13170428.html)。

ここにFreeNASのVMを作成。あとは4台のHDDをマウントしてやればOKである（慢心

* * *

 

### RDM編

4つのHDDをVMに見せるのに、わざわざそれぞれデータストア作って仮想ディスク作ってその上にRAID載せるのもあほらしいので、なにかパススルー的なものはないのかとぐぐってみたところ、RDMというのでディスクまるごと見せられるとのこと。[この辺](http://blog.thty.net/entry/2014/06/08/161357)を参考に、コマンドで物理ディスクを仮想ディスク的な趣でVMに追加してやる。

さて、これで4台でRAIDZ2だと思ったのだが、足したディスクがFreeNASから見えない。正確には、Diskの一覧には出るが、Volume作成画面には出てこない。だめじゃん。散々調べたり、Ubuntuのpartedからext2に変更してから繋ぎ直してみたりはしたのだが、どうにもならない。だめ押しがこちら。 [https://forums.freenas.org/index.php?threads/disks-not-configured-in-freenas-9-1-release.14287/](https://forums.freenas.org/index.php?threads/disks-not-configured-in-freenas-9-1-release.14287/)

> RDM with FreeNAS is a recipe for disaster. You should give up right now with trying to use RDM if you value your data at all. When RDM fails you, you'll get no sympathy from the forum. If you value your data that little, just delete it now and accept the loss.

とのこと。はい。もうFreeNASは完全に諦めた。

Ubuntuではあっさり見えたので、partedでパーティション作ってext4でフォーマットしてやる。

あとはmdadmでRAID10を組んで、sambaで見せるだけ。

すると、初速こそ最初のパターンと同じなのだが、10000ファイル転送時の速度低下も200-300Mbps程度までしか落ちないし、そのあと大きなファイルの転送のときにはちゃんと900Mbpsくらいまで復帰する。すばらしい。これがRDMの力…？おとなしく物理マシン1つに1つOS入れておけという話はあるが……

 

まあとにかく、4日かけてまともなNASがやっとできた。ねむい。

\[caption id="attachment\_795" align="aligncenter" width="400"\][![いいかんじ](https://blog.naotaco.com/assets/images/posts/2015/05/b543e03a064aa49c21d6b0e392055d4d-400x300.png)](https://blog.naotaco.com/assets/images/posts/2015/05/b543e03a064aa49c21d6b0e392055d4d.png) いいかんじ\[/caption\]

ということで、MicroServer Gen8はsambaサーバがメインの用途の場合はおすすめしづらい。まあ、普通に使ってれば全然問題ないレベルなのかもしれないが、わざわざ選ぶ必要はないと思う。見た目がいいのと、あと金さえ払えばiLOとか便利なのはいいと思うけど。やっぱりESXi入れて仮想化してRHEL入れる、みたいなHPおすすめのお約束の使い方から外れるとつらい感じがする。つまり、総じてエンタープライズっぽい。
