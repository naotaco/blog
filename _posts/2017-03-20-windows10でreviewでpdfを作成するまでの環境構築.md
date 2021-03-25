---
layout: single
title: "Windows10でRe:VIEWでPDFを作成するまでの環境構築"
date: "2017-03-20"
categories: 
  - "tips"
  - "何か"
tags: 
  - "latex"
  - "msys"
  - "review"
---

Re:VIEWというツールがある。シンプルな構文で文書を書いておいて、それをTeX経由でPDFに変換してくれるものだ。

主に某技術系壁サークルの界隈でさかんに使われているようで、今回私が[技術書典2](https://techbookfest.org/event/tbf02)に出す同人誌はこれを使って書くことにしたのであった。（[低温調理器自作本出すから](https://techbookfest.org/event/tbf02/circle/5649952705347584)来てくれ！！！！）

で、Re:VIEWで調べるがどいつもこいつもmacばっかり使っていてWindowsで動かした話があんまりない。まして入稿までとなると絶望的である。

一応この方法で何度か日光企画さんに入稿してまっとうな本になっているので、方法をまとめておく。

必要なものはこちら。

- TeX Live
- Msys2

まず、TexLiveのインストールイメージを[ここ](http://ftp.jaist.ac.jp/pub/CTAN/systems/texlive/Images/)からダウンロードする。[texlive2018.iso](http://ftp.jaist.ac.jp/pub/CTAN/systems/texlive/Images/)というやつ。筆者は2017で試したが最新版を入れておけばよいと思う。

あほみたいに時間がかかるので、この裏でMSYS2を入れる。これさえあればもうCygwinはいらない。→ [https://sourceforge.net/projects/msys2/](https://sourceforge.net/projects/msys2/)

MSYS2ではpacmanというコマンドでパッケージを入れられる。rubyを入れるには、こう。

\[code lang="shell"\] pacman -S ruby \[/code\]

一緒にgemも入る。簡単かよ。

あとは次のようにして、Re:VIEWをインストールする。

\[code lang="shell"\] gem install review \[/code\]

多少時間はかかるが問題なくインストールできた。しかしこの状態でreview-pdfmakerを叩いてもLaTeXが入っていないのでエラーになる。

TeXLiveのISOファイルのダウンロードが終わったら、適当にマウント（Window10なら標準でできる）してインストーラを起動する。なにやらオプションっぽいものをいろいろ選べる雰囲気を感じるが、騙されたと思って**諦めてFull schema（日本語だと完全インストール？）を選択する**。CJKだけ入れればいいじゃんと思うところだが、PDF作成時によくわからないエラーがでる。よくわからないが、Full schemaでインストールするとエラーはでない。もう知らん。

お気づきかもしれないが、そのままgemで入るバイナリの置き場所とTeXLiveのインストール先にパスが通らないので、手で足してやる。gemの方は自分のホーム下になるのでパスに注意。

\[code lang="shell"\] # .bashrcに追記 PATH=$PATH:/c/texlive/2018/bin/win32/ PATH=$PATH:/home/xxxx/.gem/ruby/2.3.0/bin \[/code\]

これで次のようにすると、本の名前でフォルダができて、そこに入ってコマンドを叩くとPDFができる。

\[code lang="shell"\] review-init book-name cd book-name review-pdfmaker config.yml #=> book.pdf \[/code\]

さて、ひとまずconfig.ymlの中をみて、書名や著者名など、一通りの設定を入れるとよい。

で、このままだと生成されるPDFのフォントが埋め込みになっていないので入稿に必要なPDF/Xへの変換が出来ない。そこで、何らかフォントマップを指定する必要がある。kanji-config-updmap status とすると、使用可能なフォントマップの一覧がでてくる。私の環境ではipa, ipaex, kozuka, kozuka-pr6n, ms, yu-win10が表示された。この中から一つを選んでkanji-config-updmapの引数に指定すると、このフォントを使ってゴシックや明朝のフォントが使われ、生成されたPDFに埋め込まれることになる。

\[code lang="shell"\] kanji-config-updmap-user status kanji-config-updmap-user ipa \[/code\]

あとは、できたPDFをAcrobat Pro or Acrobat DCでPDF/X-1a（Japane CXolor CXoated）に変換して色の変換設定をすれば（詳しいことは[この本](https://github.com/TechBooster/FirstStepReVIEW)を読むとよい）よいはず、だった。 が、Windows版のAcrobat Pro XIでPDF/Xに変換すると特定の文字が消えるということが判明。具体的には数式中のマイナス記号が消えた。

| ![](https://blog.naotaco.com/assets/images/posts/2017/03/pdf_error.png) |
|:--:|
|  NG |

| ![](https://blog.naotaco.com/assets/images/posts/2017/03/pdf_ok.png) |
|:--:|
|  OK |

冗談だろ……。

泣きながらぐぐっていると[同じ問題にぶちあたった人](http://oku.edu.mie-u.ac.jp/tex/mod/forum/discuss.php?d=1513)を発見。どうもバグとのことなので、Acrobat DCを使っている人は問題ないっぽい。

AcrobatのプリフライトでPDF/X変換に変換するときに、「.notdefグリフを使用する文字を空白文字で代用(nオブジェクト)」と出るとアウトっぽい。たしかに、私の場合は2箇所で消えていて、2オブジェクトを空白文字で代用とメッセージが出た。緑のチェックマークついてるし、気付くわけないだろ。

ひとまず回避するには、mapファイルをdvipdfmxのオプションに渡すと良いらしい。このようなファイルをtest-encoding.mapという名前でconfig.ymlと同じ階層にひとまず作って、

\[code lang="tex"\]

% % test.map % cmsy10 bbad153f cmsy10

\[/code\]

次のように、config.ymlのdvioptionsに指定する。このとき、相対パスでの指定はうまくいかなかったので、フルパスで指定している。ちなみにパスを間違えてもエラーは出ない（流れてしまって見落としている可能性もあるが）。

\[code lang="shell"\] # LaTeX用のdvi変換コマンドのオプションを指定する dvioptions: "-d 5 -f /c/somewhere/book-name/test-encoding.map" \[/code\]

何もかも分からないが、この設定でRe:VIEWから吐き出されたPDFファイルをAcrobat Pro XIに食わせると、問題なさそうなPDF/Xファイルができる。

ちなみに、TeXLiveを使っているからか、章の変わり目で空白ページが挟まらない設定(oneside, openany)は次のようにする必要があった。

\[code lang="shell"\] # LaTeX用のdocumentclassを指定する texdocumentclass: \["jsbook", "b5j,uplatex,oneside,openany"\] \[/code\]

### 追記@2017/03/28:

などと言っていたら武藤さんからリプライを頂戴した。

<blockquote class="twitter-tweet" data-lang="en"><p dir="ltr" lang="ja"><a href="https://twitter.com/naotaco">@naotaco</a> ActobatのプリフライトX-1a変換は色変換を含んでいてこれに限らずほかにも不幸なことが生じやすいので、トラディショナルなAcrobatからPostScript保存→Distillerのほうが安全ですね…</p>— kmuto (@kmuto) <a href="https://twitter.com/kmuto/status/843981656532819968">March 21, 2017</a></blockquote>

<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

確かにこの件以外にもプリフライトで変換すると色変換やらなんやら、緑のチェックマークが1ダースくらい表示されており不穏な感じがするのは間違いない……。教えて頂いたようにAcrobatからPostScriptで保存してDistillerでPDF/Xに変換というのを試してみた。30ページくらいしか書いていないころは問題なく変換できたので安心していたが、終盤になって試したときにはPostScript吐き出しのときにエラーを出して吐き出せなくなっていた。エラーと言っても何の情報もなく「エラーが発生しました」とのこと。職場の使えないおっさんかよ……。ひとまずプリフライトで変換したPDFを確認したところ他に問題はなさそうなので、今回はこれで入稿した。

ちなみにPostScriptにしたあとDistillerで変換するときにまた多数の設定があり、これを適切に設定しようと日光企画にDistillerの設定をどうしたらよいか聞いてみたところ、「PDF/A-1b:2005(CMYK)を使用しているがX-1aでもフォントが埋め込まれていれば大丈夫」と返答をいただいた。もうちょっとこう、色変換とか、、まあ、いいか、考えるのをやめよう、、

 

ということで入稿した。入稿ポエムは別途書く。

 

<blockquote class="twitter-tweet" data-lang="en"><p dir="ltr" lang="ja">低温調理器自作の入門本を4/9(土)の <a href="https://twitter.com/hashtag/%E6%8A%80%E8%A1%93%E6%9B%B8%E5%85%B8?src=hash">#技術書典</a> で頒布します！デバイス選定からフィードバック制御まで実測データに基づいて書きました。Anovaとの対決も。これを読んで君もオリジナルの低温調理器を作ろう！！ <a href="https://t.co/ScdnjnjsQC">https://t.co/ScdnjnjsQC</a> <a href="https://t.co/ATZdfHtDEf">pic.twitter.com/ATZdfHtDEf</a></p>— 肉と鍋 @技術書典 か-36 (@naotaco) <a href="https://twitter.com/naotaco/status/846330210404347904">March 27, 2017</a></blockquote>

<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
