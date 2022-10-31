---
layout: single
title: GitHub Pagesのデプロイがタイムアウトするようになった
date: 2022-10-31 02:00:11 +09:00
categories: GitHub blog
---

このブログはGitHub Pagesにより公開されているわけだが、このデプロイジョブが失敗するようになった。

[![GitHub Actionsのジョブ一覧。deployジョブが10分4秒で失敗している](/assets/images/posts/2022-10-31-02-04-23.png){:width="80%" .align-center} ](/assets/images/posts/2022-10-31-02-04-23.png)

deployジョブを見てみると、次のようなログで終わっていた。

```
Current status: deployment_queued
Current status: deployment_queued
Timeout reached, aborting!
Error: Timeout reached, aborting!
Deployment cancelled with https://api.github.com/repos/naotaco/blog/pages/deployment/cancel/xxxx
```

何がなんだかわからないが、とにかくタイムアウトしているということはわかる。ずっとqueuedとログが出ていたので、単にサーバが混んでいて待たされているだけなのか？とも思ったが、そんなことはなかった（たぶん）。

一つ前段のbuildジョブを見てみる。

[![buildジョブのstep一覧。全18分のうち16分がUpload artifactにかかっている](/assets/images/posts/2022-10-31-02-07-54.png){:width="80%" .align-center} ](/assets/images/posts/2022-10-31-02-07-54.png)

こちらも全部で18分少々かかっており、長すぎるように思われる。stepごとにみてみるとartifactのuploadに16分かかっており、なにかおかしいような気がする。

ぐぐっていると、[似たようなことを質問している人](https://github.com/community/community/discussions/35197)がいた。回答者曰く、

> データのコピーに時間がかかっている。10GBというサイズは上限の10倍なので、減らした方がよい。

と。[ドキュメント](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages#usage-limits)を見てみると、GitHub Pagesの上限（正確には、"a recommended limit" なので、推奨サイズか）は1GBらしい。recommendedということで即エラーとはならないものの、大きすぎるリポジトリがタイムアウトになるのは仕方ないといえる[^1]。

さて私のリポジトリのサイズはいかほどか。Upload artifactのログの最後にサイズが出ているので、見てみると、

> Total size of all the files uploaded is 2826141363 bytes

なるほど2.8GB。なるほど。このしょぼいブログがね。もちろんこのサイズは何も間違ってはおらず、リポジトリのファイルの合計が概ねこのくらいであった。

話は単純で、このブログは画像をとにかく雑に放り込んであるので、それがほとんどのサイズを占めていたのであった。なので、シンプルに画像を減らしたり軽くしたりするだけで問題は解決した。

#### 単純に画像が大きい＆JPEGの画質設定が90くらいになっている

まずはこれで、単にクソでかいJPEGが死ぬほど置いてあった。撮って出しだったり、PCでの観賞用にExportした画像をそのまま置いたりしてあったため。

これは画像を一括リサイズできるフリーソフトのRalphaを使って一発で解決した。でかい画像を長辺2000px, 画質80くらいにしたところ1GBくらい減ったような記憶がある。

#### JPGにすべき画像がPNGになっている

これもあるあるで、面倒だったのでWindowsで撮ったスクリーンショットをそのまま入れていた。それがPNGに適した画像の場合はファイルサイズが小さくなって良いのだが、写真はまったく向かない。写真のトリミングが面倒だという理由で写真を多数スクリーンショット→PNGでブログに貼っていたため、クソデカPNGが大量に生成されていた。

これも画像の処理はRalphaで一発。PNGをJPGに変換しつつ、画像サイズや画質設定は前項のJPEGと同じにする。

ファイル名が変わるので、markdownに書いてある画像のアドレスを差し替える必要がある。findとsedをこねくりまわして.PNGを.JPGに置換した。

#### Wordpressが生成した不要な画像が残っている

最悪だったのがこれで、以前使っていたWordpressに画像をアップロードしたときに自動で生成される小さいサイズの画像がGitHub pages移行後も全てそのまま入っていたのであった。たとえばある画像はこんなことになっていた。

```
xxxx.jpg
xxxx-130x90.jpg
xxxx-390x205.jpg
xxxx-392x272.jpg
xxxx-400x267.jpg
xxxx-720x480.jpg
xxxx-768x512.jpg
xxxx-800x445.jpg
xxxx-900x600.jpg
```

幸い、無印の画像が最大サイズという仕様のようだったので、これに統一することにした。こちらもいろいろとこねくりまわして、`\-[0-9]+x[0-9]+\.jpg` みたいな感じのパターンに該当する画像ファイルを全部消し、markdownからは該当しそうなリンクを全て無印に置き換えた。4500くらいあった画像が約800まで減った。

これらをすべて実施したあとはブログサイズが450MBくらいとなった。

#### 結果

[![buildに約4分、deployに約1分かかっているGitHub Actionsのジョブ](/assets/images/posts/2022-10-31-02-36-57.png){:width="80%" .align-center} ](/assets/images/posts/2022-10-31-02-36-57.png)

この通り、buildジョブが4分、deployが1分で終わっている。これなら大丈夫そうだ。


[^1]: Proアカウントなので多少は上限を緩和してくれてもいいだろと言いたくもなるが。


