---
title: "低温調理器を自作する - daemonize・豚肩ロース編 -"
date: "2015-03-25"
categories: 
  - "tips"
  - "何か"
tags: 
  - "raspberrypi2"
  - "低温調理器"
  - "料理"
---

今日も今日とて豚肉を食べたい気分になったので、豚肩ロースをやっつけます。いつものようにグラム140円くらいの安い豚肩ロースブロック(最初から縛ってある、すばらしい)を買ってきて、余ってるハーブとクレイジーソルト、胡椒をかけてラップでぐるぐる巻きにして一晩寝かせます。ここで白状しておくと、一晩寝かせるというレシピを書いてみたかっただけなので、この工程の正確な意味は理解していません。ただタイムの香りがよくきいていたので、寝かせたおかげということにしておきます。

\[caption id="attachment\_750" align="aligncenter" width="400"\][![一晩寝かせた肉](https://blog.naotaco.com/wp-content/uploads/2015/03/WP_20150325_18_09_47_Pro-400x300.jpg)](https://blog.naotaco.com/wp-content/uploads/2015/03/WP_20150325_18_09_47_Pro.jpg) タイム・ローリエとともに一晩寝かせた肉\[/caption\]

この時間を利用して開発を進めます。肉を煮ているだけでは進歩などありません。

前回までで、引数に温度を与えたらそれをキープしてくれるスクリプトができました。今回はそれをデーモン化して、外部から温度を設定できるようにします。

ちょっと試した感じではスクリプトの実行が終了したあとGPIOの出力を保持することはできそうになかったので（まあできてもゾンビみたいなHighピンが生まれるだけだろうし）、おとなしく生き続けるデーモン的なプロセスを考えます。要は前回の無限ループスクリプトがバックグラウンドで、外部から温度設定可能な状態になっていてほしい。悩んでいたところ、

 

<blockquote class="twitter-tweet" lang="ja"><a href="https://twitter.com/naotaco">@naotaco</a> supervisor便利っすよ<div></div>— Tomotaka Ito (@tomotaka_ito) <a href="https://twitter.com/tomotaka_ito/status/580650885006639104">2015, 3月 25</a></blockquote>
<script src="//platform.twitter.com/widgets.js" async charset="utf-8"></script>

 

ありがとうございますありがとうございます。

調べてみるとSupervisorというのを入れて、confファイルを書いてやるだけで勝手にスクリプトの実行・停止・再実行をしてくれるとかなんとか。最高かよ。

https://gist.github.com/naotaco/e19c02fe65979385c8e9

こんなかんじのconfファイルを/etc/supervisor/conf.d/に置いて、あとは $ sudo supervisor reload; sudo supervisor start all でOK。スクリプトを実行可能にしておく必要がある。

あとデーモンで動かすと終了が今までみたいにKeyboardIntrruptじゃなくなるので、終了時に一通り落とすようケアしておく必要がある。

https://gist.github.com/naotaco/54b9b5a9edaac1d24c85

こんなかんじで。SIGTERMとatexit両方必要とは思えないのだが、よくわからなかったし両方セットしておく。

これでデーモンとして安定稼働してくれる感じになった。ので、次は温度を外部から受け取れるようにする。最初は何も考えず環境変数で渡そうかと思っていたがいろいろ面倒っぽい。ユーザとかまたぐと。で、とりあえずRedisを試してみた。

https://gist.github.com/naotaco/7f50a04c896d1ff7d372

こんなかんじでsetして、

https://gist.github.com/naotaco/792cca57f6d437158e43

こんなかんじでgetしてくる。

すると別プロセスからでもいい感じに温度を設定できるようになった。OK, あとは気が向いたらフロントエンドを準備するだけだ。

ここまでのコードはGitHub[(cooker-daemon)](https://github.com/naotaco/cooker-daemon)にまとめておいた。

開発も進捗したので、豚肉の調理を進めることにする。

\[caption id="attachment\_749" align="aligncenter" width="400"\][![ジップロックにIN](https://blog.naotaco.com/wp-content/uploads/2015/03/WP_20150325_18_13_22_Pro-400x300.jpg)](https://blog.naotaco.com/wp-content/uploads/2015/03/WP_20150325_18_13_22_Pro.jpg) ジップロックにIN\[/caption\]

いつものようにオリーブオイルで空気を追い出してジップロックに入れ、スロークッカーへ。

\[caption id="attachment\_754" align="aligncenter" width="400"\][![クッカーに投入](https://blog.naotaco.com/wp-content/uploads/2015/03/WP_20150325_18_15_34_Pro-400x300.jpg)](https://blog.naotaco.com/wp-content/uploads/2015/03/WP_20150325_18_15_34_Pro.jpg) クッカーに投入\[/caption\]

\[caption id="attachment\_755" align="aligncenter" width="400"\][![待ちます](https://blog.naotaco.com/wp-content/uploads/2015/03/WP_20150325_18_15_28_Pro-400x300.jpg)](https://blog.naotaco.com/wp-content/uploads/2015/03/WP_20150325_18_15_28_Pro.jpg) 待ちます\[/caption\]

今回は64℃で3時間。

\[caption id="attachment\_753" align="aligncenter" width="400"\][![WP_20150325_20_58_58_Pro](https://blog.naotaco.com/wp-content/uploads/2015/03/WP_20150325_20_58_58_Pro-400x288.jpg)](https://blog.naotaco.com/wp-content/uploads/2015/03/WP_20150325_20_58_58_Pro.jpg) できあがり。タイムの香りがいいかんじ。\[/caption\]

うむ、いい感じだ。

\[caption id="attachment\_752" align="aligncenter" width="400"\][![WP_20150325_21_00_48_Pro](https://blog.naotaco.com/wp-content/uploads/2015/03/WP_20150325_21_00_48_Pro-400x257.jpg)](https://blog.naotaco.com/wp-content/uploads/2015/03/WP_20150325_21_00_48_Pro.jpg) 赤い\[/caption\]

この色は食べて良い色なのか？と脳が疑問を発するが、気にせず食べる。中心部の温度が60度に達してから30分経過している保証がどこにもないので、自己責任で食べましょう。人に出すには躊躇する色ですが、おいしいものはおいしいです。心配ならここからフライパンで表面を焼くくらいしてもいいかも。

いつものように袋に残った肉汁&オリーブオイルにバルサミコ酢・醤油・赤ワインを適当に加えてフライパンで煮詰めてソースをつくって、かけてたべる。

\[caption id="attachment\_751" align="aligncenter" width="400"\][![WP_20150325_21_09_11_Pro](https://blog.naotaco.com/wp-content/uploads/2015/03/WP_20150325_21_09_11_Pro-400x300.jpg)](https://blog.naotaco.com/wp-content/uploads/2015/03/WP_20150325_21_09_11_Pro.jpg) 完成\[/caption\]

うまい、うまいのだが非常に脂っこい。袋に残った脂とオリーブオイルを全部突っ込んだのはさすがにミステイクなのではという気がしたので、次は袋の油分を分離する方策を考えたいところだ。ちなみに400gあったが、脂っこかったため半分くらいで満足できた。健康的な料理である。のこりは明日の朝ご飯になります。

今回Pythonについて学んだこと

- "&&" は存在しない
- ++ も存在しない
- 型がほしい
- うっかり, が入ってるとstrじゃなくてtupleになっちゃってクソめんどくさい
- と思ったけど"\\t".join(some-tuple) とするとログ吐き出しやすくて便利
- hoge()とhoge　で全然挙動が違うことがある
- 2と3は別物
