---
layout: single
title: "GitLabとGit LFSを使ってExcelなどのバイナリでできたドキュメントの世代管理をする"
date: "2016-04-02"
categories: 
  - "tips"
  - "未分類"
tags: 
  - "git"
  - "gitlab"
  - "lfs"
  - "サーバ"
---

### 前置き

皆さんも業務上やむを得ずWord, ExcelやPowerpointでドキュメントを作っていることと思います。他にもなんかよく分からない画像だったりとか、Astahとかそういうやつとか。とにかく望むと望むまいと僕たちはプロプライエタリなバイナリに囲まれて生きています。

まあその手のドキュメントは作ったり読んだりしてる限り別にいいんですが、だいたい世代管理が困難に近いです。MicrosoftのSharepointとかいう地上最低の操作性を誇るWebアプリを使う\[ref\]なんとドキュメントのロックができるので、他人との衝突を避けることができます！！\[/ref\]など、まあ手が無いこともないのですが、いろいろと厄介です。で、そういうファッキンバイナリィドキュメンツが数十GB単位で貯まってきた頃に事故があって、誰かが共有フォルダのファイルを消したりぶち壊したりしてしまったりなんだりして、上司が「ちょっとこれいい感じに管理する方法考えといて」とか無茶なことを言ってくるわけです。

後半に私情が挟まりましたが、とにかくバイナリをどう管理するかは我々の会社生活を左右する死活問題なわけなので、真面目に考えます。

要件としてはこのような感じ:

- バイナリだろうがテキストだろうが高速に世代管理ができる
- ストレス無く人間にとって扱うことが出来る操作性である
- Jenkinsにも扱いやすい操作性？である
- バックアップがとりやすい

また、私の場合の条件はこのような感じ:

- NFS/sambaの共有フォルダにバイナリがおいてある
- 数万ファイル、数十GBくらい
- オンプレで使える(自前サーバで使える)

複数人がファイルを同時に編集した場合のコンフリクトについては当人同士で殴り合って解決してもらうことにします。ロックできる仕組みを考えてもよいですが、だいたいの場合終電間際にこっちが編集しようとしているファイルは誰かがロックしたまま帰宅したりしているものなので、そのような仕組みは考えないことにします。また、gitについては人間には難しすぎるとの意見もありますが、add/commit/push/pullしか使わないのでギリギリ扱うことが可能ということにします。

適当に調べた感じ、世の中にはバイナリを世代管理する方法がいくつかあります。

- Gitに突っ込む
- subversionに突っ込む
- Owncloudを使う

など。一応全部試しましたが、一番マシなのはsubversionでした。gitは全部add/commitしただけで1日かかり、最終的にはメモリ不足で落ちました。OwncloudはLDAP連携も世代管理もできますが、動作が不安定で(とくにでかいLDAPとの連携が厳しそう)イマイチでした。subversionはまあ不可能ではないんですが、とにかく遅いしあんまり安定しない(addしてからcommitまでに誰かにファイルを消されたりするとエラーで止まったりとか、そういう…）ので厳しいです。

そこに[Git LFS](https://git-lfs.github.com/)とかいうのをGitHubが作って公開してきたので、これを試すことにしました。実は以前試したことがあったんですが、Git LFSサーバを自分でわざわざ立てる必要があってだるすぎて見送っていたという経緯が。ところが愛しのGitLabが8.2からLFSに対応してきたのです。神か。ということで、GitLab8.2以降があればサーバ側は何も手を加えずにGit LFSが使えます。しかも、LFSに追加したバイナリファイルもWebから見られて過去のファイルにも簡単にアクセスできます。すばらしい。もちろんGitHubは既に対応しているので、GHEを使っているリッチ企業各位はさっさと使えばよいと思います。

### Git LFSとは

よくわかりませんが、指定したファイル(おもにバイナリ)をGitリポジトリではない別のサーバに置いて、Gitとしてはそのハッシュ?が書かれたテキストファイルのみを管理するという仕組みのようです。つまり、GitLabが普段通りのGitのリモートリポジトリに加えて、ファイル転送を待ち受けるLFSサーバをリポジトリごとに用意しているらしい。で、クライアント側はバイナリファイルや大きなファイルをLFSサーバ側にpushして、Gitリポジトリにはファイルのハッシュ？のみをPushすると。

### サーバの準備

前述のように、GitLab 8.2以降であれば立てるだけでよいです。ただし、私はdocker上でGitLabを走らせているので、もしかしたらLFSを有効にする設定が必要なのかもしれません。

[https://github.com/sameersbn/docker-gitlab](https://github.com/sameersbn/docker-gitlab)

このdockerイメージを使うと、デフォルトで使えます。関連する変数は以下の通り:

- GITLAB\_LFS\_ENABLED: LFSの有効/無効。デフォルトでtrue.
- GITLAB\_LFS\_OBJECTS\_DIR: LFSのオブジェクトの置き場所。容量がかさむため、別の場所にしたいときに。
- GITLAB\_BACKUP\_SKIP: 後述

### クライアントの準備

クライアントは通常のGitに加え、Git LFSをインストールする必要があります。

[https://github.com/github/git-lfs/releases](https://github.com/github/git-lfs/releases)

git lfsというコマンドが通ればOKです。

### つかいかた

GitLabは8.2から対応してるはずですが、毎月更新が入っているので最新を使っておきましょう。2016/04/02現在は8.6.3が出ています。ここでは8.6.3で説明します。

まず、適当にGitLabでプロジェクトを作ります。で、それをcloneして、git lfsの設定をします。

\[code lang="shell"\] git clone ssh://git@localhost:10022/naotaco/lfs-test.git cd lfs-test git lfs install # init的な git lfs track "\*.zip" # .zipの全ファイルをLFS対象とする \[/code\]

あとは、指定した拡張子のファイルをaddすればそれはもうLFS管理になります。

\[code lang="shell"\] git add binary.zip git add text-file git commit -m 'hoge' \[/code\]

ここでgit lfs ls-filesとすると、LFS管理されているファイルだけが出るので、管理が別れていることがわかります。

$ git lfs ls-files
db8846fd84 \* binary.zip

あとはpushすればよいのですが、手元のクライアントはLFSのサーバがどこにあるかを知りません。デフォルトのままでPushすると、gitのPushは成功しますが、そのあとのLFSのpushを明後日の方向に試みて失敗します。そこで、lfs.urlというconfigを追加します。

\[code lang="shell"\]

git config --add lfs.url "http://localhost:10080/naotaco/lfs-test.git/info/lfs"

\[/code\]

見ればわかりますが、ここで設定するURLは、リポジトリのHTTPのURLに"/info/lfs"を足したものになります。また、一度pushすると二度認証が走ります。現時点でLFSはHTTP(S)にしか対応していないので、2回目は必ずパスワードを聞かれます。だるい。ID/パスワードを毎回聞かれるのがだるい場合は、git credential helperを使ったりするとパスワードを平文で保存しておいて、毎回打たなくてもいいようにすることもできます(棒)。

$ git push origin master
Username for 'http://localhost:10080': naotaco
Password for 'http://naotaco@localhost:10080':
Git LFS: (1 of 1 files) 5 B / 5 B
Counting objects: 4, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 485 bytes | 0 bytes/s, done.
Total 4 (delta 0), reused 0 (delta 0)
To ssh://git@localhost:10022/naotaco/lfs-test.git
   42f14b9..7c9daa9  master -> master

LFSのSSHで認証できるようにしてくれるとだいぶ助かるのですが。

\[caption id="attachment\_1121" align="aligncenter" width="640"\][![バイナリファイルを追加したところ](https://blog.naotaco.com/assets/images/posts/2016/04/lfs-project-1024x489.png)](https://blog.naotaco.com/assets/images/posts/2016/04/lfs-project.png) zipファイルを追加したところ\[/caption\]

zipファイルを追加してpushすると、Webからは上のようにみえます。見た目での区別がまったくできないのはどうかと思うが……。

### 運用とか

私はJenkinsサーバにNFSで共有フォルダをマウントして、定期的にJenkinsさんにフォルダをまるごとadd/commit/pushさせています。個人個人が手元にリポジトリを持っていて適宜push/pullするような運用でもよいかとは思いますが、ドキュメントの量次第ですね。

LFSは非常に処理が軽く、NFS越しに100GBあっても数分でgit add, git commitが完了します。subversionを使っていたときとは雲泥の差だ……。また、処理途中にファイルが消されたりするような状況に対しても安定しています。つよい。

いずれにせよコマンド操作で全て完結するので、Jenkinsに操作させて定期的にスナップショットをとったり、別のリモートリポジトリにバックアップとしてpushさせたり、お好きな運用が可能です。

### Backup

GitLabには全体をバックアップするRakeタスクがある。が、これをほっとくとLFSのオブジェクトファイルも全てコピーしてtarにしてくれるので非常に厄介です。そもそもファイルがでかすぎるからLFSで管理しているのに、丸ごとバックアップされたらかなわない（まあ頻度次第だとは思うが、私はRakeタスクのバックアップを毎日しているので、少なくともこの対象からは外したい）。

[http://doc.gitlab.com/ce/raketasks/backup\_restore.html#create-a-backup-of-the-gitlab-system](http://doc.gitlab.com/ce/raketasks/backup_restore.html#create-a-backup-of-the-gitlab-system)

ここにあるように、SKIP=lfsと渡すとLFSを除外してくれるので、そうしたいところです。

で、私の使っている前述のdockerイメージではこのSKIPオプションを渡せるようになっているので、GITLAB\_BACKUP\_SKIP=lfs を設定しています。渡せるようになっているというか、私がPRを出して追加してもらったのですが。

### まとめ

GitLabを使うと割と簡単にLFSが使えるので、あほみたいな量のバイナリを押しつけられて泣いてる人はまず試してみるとよいと思う。
