---
layout: single
title: "低温調理器を自作する - TCP talkers - (Web UI編)"
date: "2015-03-30"
categories: 
  - "何か"
tags: 
  - "golang"
  - "raspberrypi2"
  - "低温調理器"
  - "料理"
---

さて、デーモン化したはよいが、結局温度設定を突っ込むにはRedisを介さなければいけないのであった。不便で仕方ないのでWebから設定できるようにしたい。スマホから肉を煮たい。まさに人間の根源的な欲求だと思う。というわけで今回はWebから設定できるようにした。

![Cooker-block-diagram](https://blog.naotaco.com/assets/images/posts/2015/03/Cooker-block-diagram1-1024x547.png)

 

図だけでもそれっぽくかわいい感じにつくればそれっぽく見えると思っていたのだが、どうやらそんなこともなさそうである。

さて、いまどきさすがにuse CGI; というのもどうかと思うので、現代的にWAF的なアレをアレして作ろうと思ってGoでできてるGojiを選択した。とにかくシンプルで軽い、というのは完全に後付けの理由で、実際はせっかくGoをビルドしたから使いたかっただけの話である。

Raspberry Pi用のGoのビルドは、[このへん](http://dave.cheney.net/2012/09/25/installing-go-on-the-raspberry-pi)に書いてあるようにやればよいだけなのだが、hgでcloneしてくるところを私のように何も考えずやるととにかく最新がビルドされてしまい、go version と打つと、

$ go version
go version devel +9ef10fde754f Thu Dec 11 16:32:25 2014 +1100 linux/arm

と表示されてしまい一体バージョンいくつの機能が入っているのかさっぱりわからないことになってしまう。いい感じに1.4.2をビルドしたほうがよさそうである。やり方わかったらおしえてください（クズ

まあそんな適当な感じにビルドしてきたGoでもGojiはちゃんと動くのですごい。

基本的に/をGETされたら状態をHTMLで表示して、formからの文字列を/set/にPOSTする感じにしてみた。しかしこれ冷静に考えると設定するSet系だけはWeb APIっぽくて表示は違うからだいぶきもちわるいな。Get系もWeb APIにしてAjax的な感じでいいかんじにしてあげればいいのかもしれないが、そもそもにおいて全くJS書けないし考えたくない感じがする。

\[caption id="attachment\_769" align="aligncenter" width="399"\][![ゴミのようなWebデザイン](https://blog.naotaco.com/assets/images/posts/2015/03/cookercooker-front.png)](https://blog.naotaco.com/assets/images/posts/2015/03/cookercooker-front.png) ゴミのようなWebデザイン\[/caption\]

ともあれ、現在の温度が表示されたり、目標温度を更新したりできるようになった。いい感じである。見ての通りCSSもJSも1文字たりとも書いていない。

今回のコードは[こちら](https://github.com/naotaco/cooker-front)。

また、go runで立ち上げていると邪魔なので、daemon同様、Supervisorでデーモン化してやる。

https://gist.github.com/naotaco/870a65a2ce2ce5c33e1d

かんたん。こうしてやればサーバ再起動のあともdaemonもWebサーバもいっしょに上がってくるので安心である。

動かしてみたところ。

 

<iframe src="https://vine.co/v/OLuW9qEpmp3/embed/simple" width="480" height="480" frameborder="0"></iframe>

<script src="https://platform.vine.co/static/scripts/embed.js"></script>

 

こんなかんじで、Force On/Offを押すと設定温度が強制的に100/0℃になり手動でOn/Offも可能。今後やることとしては、

- JSかなんか使って自動更新
- ログ機能(いまの肉を煮始めてから何度で何分経過したのか知りたい)
- グラフ機能(いまの肉を煮始めてからどのように温度が上昇したのか知りたい)
- タイマ機能(家に帰ってたら肉が煮えていて欲しい/指定した温度でn時間経ったら止めたい)
- Raspberry Pi自体の無線化

といったあたりだろうか。ひとまずPCを立ち上げてSSHしなくても肉が煮られるようになったので、当初の目的であるスロークッカーにTCPを喋らせる、は達成できたと言って良いのではないかと思う。
