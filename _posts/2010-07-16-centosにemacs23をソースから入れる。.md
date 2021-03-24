---
title: "CentOSにEmacs23をソースから入れる。"
date: "2010-07-16"
categories: 
  - "tips"
tags: 
  - "centos"
  - "emacs"
  - "ruby"
---

普通に

\# ./configure

ってすると、libpngがないとか何とか散々言われる。ので、そこで言われた通りに、

#./configure  --with-xpm=no --with-jpeg=no --with-png=no --with-gif=no --with-tiff=no

ってやると、今度はallocaが無いだなんだとぐだぐだ言われる。

configure: error: a system implementation of alloca is required

とかなんとか。仕方ないのでこれも入れてやろうと、yum search alloca で出てきた適当なパッケージを入れてみるも効果無し。

で、結局

./configure --without-x

ってやったら全て解決した。あとはmakeからのmake install。これでRubyソースに色がついた。
