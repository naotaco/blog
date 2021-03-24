---
layout: single
title: "twitter bot @genryo_bot のはなし"
date: "2010-10-31"
categories: 
  - "何か"
tags: 
  - "perl"
  - "twitter"
---

Syntax highlighterいれてみた。ので、コードを少し貼ってみる。

とりあえずこないだTwitterでフォロー返しに不具合があって、良く出力を見ていたらフォロワーが100人ぴったりだった。慌ててAPIとかNet::Twitterのドキュメントを見ると、1回に100ずつしか得られないとのこと。pagingかcursorを利用するかして何度かアクセスしろ（これってAPIアクセス数は増えるのかな？）とのことだったので、next\_cursorに0が帰ってくるまで何度もアクセスして、followers()で得られたuserを1つの配列に突っ込むようにしといた。

my @followers;
my $cursor = -1;
while ($cursor) {
    my $f = $nt->followers({cursor => $cursor}) or die "error while getting followers $!\\n";
    $cursor = $f->{next\_cursor};
    foreach my $u (@{$f->{users}}) {
        push @followers, $u;
    }
}

これでたぶん数百フォロワーいても大丈夫。twitter先生のことなので、2回目だけアクセス失敗とか平気であるからちゃんとチェックしておきましょう。僕はこれ忘れて100人目より後のフォロワー全部を一度リムーブしましたorz

あとはまってたのは、in\_reply\_to\_status\_idに渡すID。ステータスのIDを渡すものだと知らず、ひたすらユーザーIDを渡して、reply toが表示されないなぁおかしいなぁって思ってたorz

で、[このBOT](http://twitter.com/genryo_bot)はフォロー返しして、TLにある太りそうな発言にうっとうしいReplyを返すのが仕事。発言を全部MeCabに突っ込んで要素に分割して、あらかじめ指定した順番で太りそうな名詞と（助詞と）動詞の組み合わせが出てきてるかどうか見てるだけ。超単純なんだけど、MeCabのおかげで動詞を原形で指定できるから、けっこう幅広いパターンに引っかかっていい感じ。

文字列が太りそうか判断するパッケージ"Fat"を作ったんだけど、中身が上に書いたことくらいしかなくて100行くらいしかないしだいぶアレなのでソースは貼らないｗ
