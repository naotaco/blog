---
layout: single
title: "Net::TwitterでIncorrect signatureが止まらない"
date: "2010-07-10"
categories: 
  - "ダメ"
tags: 
  - "cpan"
  - "perl"
  - "ruby"
  - "twitter"
---

Net::Twitterを使って日本語をつぶやきたいが、OAuthを使うと日本語がつぶやけないという話。

普通にBASIC認証でIDとパスワードを渡すと英語・日本語(UTF-８)どっちでもツイートできるのに、OAuthを使うと日本語の時だけIncorrect signatureなどと意味不明な供述をしやがる。ちなみにPerlは5.10.1。

\[perl\] my $nt = Net::Twitter->new( traits          => \['API::REST', 'OAuth'\], consumer\_key    => 'コンシューマキー', consumer\_secret => 'しーくれっと' ); $nt->access\_token('トークン'); $nt->access\_token\_secret('しーくれっととーくん'); \[/perl\]

こうして、あとは $nt->update('hoge'); でつぶやける。但し英語のみ。

ぐぐってみると、同じ問題がNet::Twitter 3.13003+Net::OAuthで発生するという話がたくさん引っかかるのだが、どれもこれらを最新版にアップデートしたら直ったと書いてある。とっくに3.13006まで上げてるが、まったく直る気配がない。どうしてこうなった。現在は3.13007になっているが、変わらなかった。

英語ならツイートできるわけで、OAuth自体に問題があるとはどうしても思えない。ので、きっとどっかで何かがUTF-8あたりと喧嘩か何かしてるか何かなんだろうなぁ。なんもわからん。ソースを読みにいくという選択肢が無いへっぽこ学生。

一番安直な解決法としては、既にgem twitterをインストールし、OAuthでのあれやこれやの方法を確認できているRubyに移植することなんだが、今ひとつ踏み切れないところ。大したBOTでもないから1日あれば全部移植できるとは思うんだけど、んー。

てことで劇的なNet::TwitterのアップデートがtwitterのBasic認証廃止までにくることを夢見て、今日も寝て待つ俺なのであった。

→つづき：[https://blog.naotaco.com/archives/101](https://blog.naotaco.com/archives/101)
