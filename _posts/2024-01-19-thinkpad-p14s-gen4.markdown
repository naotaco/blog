---
layout: single
title: ThinkPad X1 Carbon Gen10を投げ捨ててp14s Gen4を買ってLightroomのベンチをした話
date: 2024-01-19 02:35:53 +09:00
categories: PC Lenovo Lightroom ベンチマーク
---

最悪だった話の続き。

一昨年（2022年）に[ThinkPad X13 AMD Gen3を買ったところ一瞬で故障→返品となり、X1 Carbonを買った]({% link _posts/2022-09-06-lenovo-thinkpad-x13-gen3-amd.markdown %})。

その後しばらくX1 Carbonを使っていたのだが、これはかなり冷却に無理があるらしくRAW現像を少しするとCPUクロックが1GHzに貼りついてしまい、全てが死ぬほど遅くなる。どうもコア数を欲張って1280Pにしたのがまずかったようだ[^1]。RAW現像が少し遅いくらいならまだいいのだが、現像を開始するとほとんどフリーズしたようにWindows全体がほぼ応答できなくなる。さすがにこれでは話にならないので、見切りを付けて買い換えることにした次第。30万くらいしたのだが……。

プロセスが古く（知らんけど）消費電力の大きいIntelのCPUと薄型ボディの組み合わせが最悪だということはよくわかったので、この2つを避ける。つまりAMDの分厚い機種にすればよいのだ。そもそも最初に買ったX13 AMD Gen3が壊れなければ、あるいはすぐ修理できていればこんなことにはならなかった気がしてならないが……。

### 発注

ということでP14s AMD Gen4を買うことにした。T14との差はよくわからないが、Pシリーズだから速いだろう、知らんけど。

CPUは上位の7840Uを選択。それでも1280Pよりはコア数が少ないが、もはやそのようなことはどうでもよい。メモリはあとから増設できないので十分な32GBを積んでおく。画面は2.8K OLEDが選べるのでそれにした。他にはFHDしか選択肢がない。そういえば最近光沢画面は流行らないのか？あまり見なくなったような気がする。SSDは交換すればよい（後述）ので256GB。キーボードはもちろんUS。

あとバッテリに3セルと4セルの選択肢があって、それぞれの重さについてはどこにも書いておらず、何がなんだかわからない（最悪）。とりあえずでかい方ということで4セルにした。届いたPCの重さを量ったら1337gだった。仕様には約1.34kg～と書いてあるのだが、3セルでも4セルでも重さは変わらないのか…？よくわからないが4セルでこの重さならこれが正解だろう。

これで20万円弱くらい。昨今の物価高からすると安く感じられる（気のせい）。

発注時の納期はいつもの「4週間以上」だったが、数日経ったところで1週間後の発送予定日が突然表示され、概ねそのくらいで発送された。そこから1週間くらいで届いた。えらい。

交換用のSSDは評判のよさそうなSDのSN770を選択。出先で画像を取り込むときに少なくとも500GBくらいの作業領域が欲しかったので、2TBにした。それでも23000円くらいである。これは別途ツクモの通販で買っておく。ついでにWeraの精密ドライバーも買ってみた[^2]。

忘れてはいけないのが回復ドライブ作成用のUSBメモリ。安いやつでいいが、32GBの容量が必要だった。

### セットアップ＆SSD交換

X13 Gen3の時にも書いたが、最近のX1以外のThinkPadはマジで安っぽい。P14sもご多分に漏れずプラスチック感が溢れる仕上がりである。少なくとも昔のX60とかの天板は品位がすごくよかったと思うのだが。ということで質感を比べるとX1 Carbonとは比較にならない。キーボードも相変わらず他メーカーよりマシな水準であるとはいえ薄くて感触が良いとは言えない。しかし、そのようなことは基本的な性能の前では全て些事に過ぎない。

とりあえず初期設定とWindows Updateだけして、SSD交換に入る。が、その前に元からついていたSSDのベンチマークだけしておくことにする。あとからわかるがWDのSN740であった。

[![CrystalDiskMarkのスクリーンショット。おおむねRead 4000MB/s, Write 2000MB/s という数字が読める。](/assets/images/posts/thinkpad_p14s/crystaldiskmark_thinkpad_p14s_with_default_ssd.webp){:width="60%" .align-center} ](/assets/images/posts/thinkpad_p14s/crystaldiskmark_thinkpad_p14s_with_default_ssd.webp)

Read 4000MB/s、Write 2000MB/s。別にこの数字になにか不満があるわけではないが、容量（256GB）には不満がある。

SSDを交換する前に、USBメモリに回復ドライブを作っておく。8GBくらいでいいのかと思っていたが、32GB以上とのことであった。適当に買ったら32GBだったのでセーフ。この作成が遅く、1時間くらいかかった。

ドライブができたら、満を持してSSDの交換である。最近は保守マニュアルを読まなくてもYouTubeに[公式の交換手順動画](https://www.youtube.com/watch?v=8sm1ScVUHqY)が出ている。正直助かる。

まずは動画の通りにBIOSからバッテリをオフにする。この操作をすればバッテリのコネクタを抜かなくてもよいらしい。便利。オフにした瞬間に電源が落ちるのは当然だがちょっとうける。

交換に必要なのはプラスドライバ（サイズは1と0だと思う多分。前者が筐体のネジ、後者がSSD）と、分解用のプラスチック製のヘラ？みたいなやつ（プライツール）。パネルは動画のように簡単に外れないし、安いのでプライツールは買っておいたほうがいい。ネジをはずしてプライツールを押し込んで蓋をあける。Ethernetポートの下側のところがちょっと割れそうになって怖かったが、しばらくやっていたらあいた。

[![ノートパソコンの裏蓋を開けたところの写真。基板やファンが見える](/assets/images/posts/thinkpad_p14s/thinkpad-1.webp){:width="80%" .align-center} ](/assets/images/posts/thinkpad_p14s/thinkpad-1.webp)

動画で使われていた機種と異なって放熱のための？銅の板のようなものはなかった。ネジを外してSSDを抜く。デスクトップPCのマザーボードについているM.2のスロットと異なり、SSDを基板から30度くらい（？）持ち上げる方向に傾けて抜く方式ではないらしい。少しだけ持ち上げてほぼ基板と平行に抜く感じ。

[![2つのM.2SSDが机上で並んでいる写真。](/assets/images/posts/thinkpad_p14s/thinkpad-2.webp){:width="60%" .align-center} ](/assets/images/posts/thinkpad_p14s/thinkpad-2.webp)

SN740と770。今時のSSDは部品も少ないのね。さっさとSN770を装着してネジを締める。

[![](/assets/images/posts/thinkpad_p14s/thinkpad-3.webp){:width="60%" .align-center} ](/assets/images/posts/thinkpad_p14s/thinkpad-3.webp)

蓋とネジを戻して、ACアダプタを接続する。最初にオフにしたバッテリの設定はACアダプタをつなぐと自動で戻るそうなので、普通に電源を入れればよい。作成した回復ドライブを挿入した状態で電源を入れ、F12キーを押すとブート対象が選べるのでUSBメモリを選ぶ。

データ全消しで回復する選択肢を選ぶとリカバリが始まる。

[![](/assets/images/posts/thinkpad_p14s/thinkpad-4.webp){:width="60%" .align-center} ](/assets/images/posts/thinkpad_p14s/thinkpad-4.webp)

これも長く、1時間以上かかっていた気がする。

終わると初期設定にいくので（だるい）、これを倒すと完了。お疲れさまでした。



### 性能

[![](/assets/images/posts/thinkpad_p14s/crystaldiskmark_thinkpad_p14s_with_2TB_SN770.webp){:width="60%" .align-center} ](/assets/images/posts/thinkpad_p14s/crystaldiskmark_thinkpad_p14s_with_2TB_SN770.webp)

速度はどうでもいいが、期待通り。2TBの容量が頼もしい。

問題はRAW現像だ。Lightroomを入れて、手元にあった230枚の画像を現像する（AC接続状態）。4回やったがいずれも8分で終わり、CPU使用率が100%に張り付いているにもかかわらずクロックが3.7GHzあたりから落ちるようなことはなかった。実にすばらしい。

哀れX1 carbonは現像前のレタッチの段階でクロックが落ちて負荷MAXで、そこから現像すると酷く遅くなっていた。以前現像したときの画像フォルダをみてみると、1枚3.4～9.2秒くらいかかっていた。遅いのもそうだがばらつきがでかい。厳しすぎる。ついでにデスクトップPCでも同じ事をしたが、さすがに速かった。少なくとも2024年にRAW現像をするならとにかくAMDにしておけばよいということがわかる。

|                    | 画像枚数 | 所要時間[秒] | 1枚あたり現像時間[秒] |
| ------------------ | ---- | ------- | ------------ |
| X1C i7 1280P_パターン1 | 41   | 141  | 3.44         |
| X1C i7 1280P_パターン2 | 67   | 346  | 5.16         |
| X1C i7 1280P_パターン3 | 60   | 552  | 9.20         |
| P14s R7 7840U      | 230  | 452  | 1.97         |
| 自作デスクトップ R7 5800X  | 230  | 157  | 0.68         |

ストレージがでかくてRAW現像が速いのでもう言うことはなにもない。Rustのコンパイルは遅いかもしれないがそれはパソコンのせいではない。

その他、USBが気になるところではあるが、ドックを常用することもないのであまり高いレベルは求めていない。Type-Cで10Gbps通ることは確認できたので十分。欲を言えばType-Aも10Gbps通してくれた方が嬉しかったが、ラップトップではあまり見かけない（Intelでもそう）のでしょうがないかなあ。

#### FF14ベンチ

ゲームのことはまったくわからないが、別件で簡単にベンチマークをしたかったのでインストール不要でサクッと試せるFF14ベンチ（暁月のフィナーレ）を回してみた。

![FF14ベンチの結果画面。1440・最高画質の設定で、スコアは3433](/assets/images/posts/thinkpad_p14s/ff14_bench_1440_maiximum_thinkpadP14s.webp){:width="60%" .align-center}

![FF14ベンチの結果画面。1440・高画質（ラップトップ）の設定で、スコアは4309](/assets/images/posts/thinkpad_p14s/ff14_bench_1440_High_laptop_thinkpadP14s.webp){:width="60%" .align-center}

2560x1440、フルスクリーン、最高画質設定で3433。同 高画質（ラップトップ）で4309。4000が普通に遊べる目安ということで、一昔前（？）のゲームであればQHDで遊べてしまうといってよいのだろうか。すごいなあ（感嘆）。

### まとめ

Ryzen最高！！！あとは壊れないでくれ！！！

[^1]: 実際は何を選んでもダメだったのかもしれないが、とりあえずそういうことにしておく。
[^2]: 上等な精密ドライバを買うと感触が良いのかなと思ったが、すごく良いと感じられるようなことはあまりなかった。