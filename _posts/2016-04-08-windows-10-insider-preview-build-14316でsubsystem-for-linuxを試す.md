---
layout: single
title: "Windows 10 Insider preview build 14316でsubsystem for linuxを試す"
date: "2016-04-08"
categories: 
  - "tips"
  - "何か"
tags: 
  - "bash"
  - "insider-preview"
  - "windows"
  - "windows10"
---

タイトルが長い。

まずInsider previewのfast ringに入り、build 14316のアップデートを適用する。すると、Windowsの機能？のところにWindows Subsystem for Linux (Beta）という超かっこいい項目があるので、有効にする。

[![Windows-features](https://blog.naotaco.com/assets/images/posts/2016/04/Windows-features.png)](https://blog.naotaco.com/assets/images/posts/2016/04/Windows-features.png)

| ![起動したところ](https://blog.naotaco.com/assets/images/posts/2016/04/bash-on-windows.png) |
|:--:|
|  起動してunameを打ったところ |

あとは普通にBash on Ubuntu on Windowsとかいうプログラムが追加されているので、起動して適当にあそぶ。

試した範囲では、build-essentialをはじめとする各種パッケージは普通にaptで入るし、それでzsh, emacs, gitあたりは普通にconfigure/makeできて動いた。emacsをちょっと使ったら表示がぶっ壊れたりしてたし、動作はだいぶ怪しいところが当然あるが、普通にうごくのがすごい。

 

### Zsh

\[code lang="shell"\] sudo apt-get install -y git-core gcc make autoconf yodl libncursesw5-dev texinfo ls mkdir zsh-build cd zsh-build/ git clone git://zsh.git.sf.net/gitroot/zsh/zsh cd zsh/ ./Util/preconfig ./configure make make install \[/code\]

### emacs 24.5

\[code lang="shell"\] curl -O http://ftp.jaist.ac.jp/pub/GNU/emacs/emacs-24.5.tar.gz tar xzf emacs-24.5.tar.gz cd emacs-24.5 ./configure --without-x make make install emacs emacs -version \[/code\]

### git

\[code lang="shell"\] git clone https://github.com/git/git.git --depth 1 cd git/ make configure ./configure --with-curl --prefix=$HOME/local make make install \[/code\]

まるでubuntuのように動く。ただデフォルトのリポジトリがクソ重いので、riken様のリポジトリに変えておくとよい。普通にubuntuと同じように/etc/apt/sources.listを変えるだけ。

root@localhost:~# cat /etc/apt/sources.list
deb http://ftp.jaist.ac.jp/pub/Linux/ubuntu/ trusty main restricted universe multiverse
deb http://ftp.jaist.ac.jp/pub/Linux/ubuntu/ trusty-updates main restricted universe multiverse
deb http://security.ubuntu.com/ubuntu trusty-security main restricted universe multiverse

emacsが入ると自分のinit.elを試したくなるのが人情というものだろう。私のはこれ: [https://github.com/naotaco/emacs.d](https://github.com/naotaco/emacs.d)

いつも通りel-getを~/.emacs.d/以下にcloneして、このinit.elを置いて起動したら普通に動いた（ただしgit1.9.5以上が必要なので、自分でビルドする必要がある）。すごい。

| ![emacs](https://blog.naotaco.com/assets/images/posts/2016/04/emacs-ok.png) |
|:--:|
|  emacs |

| ![すぐ表示が壊れる](https://blog.naotaco.com/assets/images/posts/2016/04/emacs-ng.png) |
|:--:|
|  すぐ表示が壊れる |

| ![Auto completionもHelmも動く。](https://blog.naotaco.com/assets/images/posts/2016/04/emacs-helm.png) |
|:--:|
|  Auto completionもHelmも動く。 |

なにがなんだかわからないが、本当に動いててすごい。使ってて頭が混乱する。あと、Ctrl+Aがどっかにキーを奪われているのかbash/emacsで使えないのが厳しい。まあそれを言えば、コマンドプロンプト並の機能しかないターミナル自体がそもそも相当厳しいが、まあさすがにこの辺はそのうちなんとかなるだろう。とりあえず無限の可能性を感じる。
