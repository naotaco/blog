---
layout: single
title: "ムームーDNS+Google appsを使うという話"
date: "2010-07-07"
categories: 
  - "tips"
tags: 
  - "dns"
  - "web"
---

![](file:///C:/Documents%20and%20Settings/NaoMatsumura/%E3%83%87%E3%82%B9%E3%82%AF%E3%83%88%E3%83%83%E3%83%97/dns1.jpg)WEBはヘテムル、メールはGoogle appsのGmail、と分けたい。ぐぐって出てきたように適当にやってみたが、どうも安定しない。たまにドメイン売ります的なページに飛んじゃう。ndparking.comとか、そういうぁゃιぃページに。

結論から言うと、ドメインをIPに結びつけるAレコードを追加しないとならんという話。正しく見られるときと変なとこに飛ばされるときがある理由はよくわからないが、これで安定した。ぐぐってもあんまり情報がなかったので、記録を残してみる。

![](https://blog.naotaco.com/assets/images/posts/2010/07/dns11.png "dns1")

もし、種別が「メール」っていうところがあったら、利用しない、でOK。

![](https://blog.naotaco.com/assets/images/posts/2010/07/dns22.png "dns2")

カスタム設定が、こんなかんじ。

無サブドメインと、wwwサブドメインをサーバーのIPアドレスにAでくっつける。サーバーのIPアドレスは、コントロールパネルから見られるはず。FTPかSSHあたりのサーバ情報と同じでOKでした。
