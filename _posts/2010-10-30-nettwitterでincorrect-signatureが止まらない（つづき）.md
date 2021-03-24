---
layout: single
title: "Net::TwitterでIncorrect signatureが止まらない（つづき）"
date: "2010-10-30"
categories: 
  - "tips"
  - "ダメ"
tags: 
  - "perl"
  - "twitter"
---

どうせ忘れるだろうからメモ。

Net::OAuthだかNet::Twitterだかのバグで表題のエラーが出ていた件は、十分に新しいバージョン（3.14\*\*以降？）では直っているはずだ。にもかかわらずこれが出るというのは、単にutf-8として適切ではないデータが渡されているだけのことらしい。orz

BasicのときはいけたのにOAuthになったら通らなくなるのは不可解だが、TwitterのAPIなんて不可解なことだらけなので考えても仕方がない。まあもうBasic認証使えないしね。もしかしてあれか？OAuthになったついでに化けないようにutf-8のチェックをちゃんとしてくれてるとか？

結論から言うと、

use encoding("utf-8");

を消したら直った。ふしぎだ。orz

[御大の言うよう](http://blog.livedoor.jp/dankogai/archives/51221731.html)に、ソースは全てuse utf8;してutf-8で書く。encodingはもう使わない。

で、読み込んできた文字列は全部Encode::decode\_utf8で処理する。（http://blog.livedoor.jp/dankogai/archives/51290188.html）

そうすればソース中の文字列も外から入ってきた文字列も全部中身が正しいutf-8で（←これ大事）、かつutf-8フラグも立つ（←これも大事）ので化けない（少なくともNet::Twitterさんに怒られることはない）。もう文字コードでは悩まなくて済むはずだ・・・
