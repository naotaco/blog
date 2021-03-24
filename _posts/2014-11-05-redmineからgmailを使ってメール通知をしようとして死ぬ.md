---
title: "RedmineからGmailを使ってメール通知をしようとして死ぬほどはまった"
date: "2014-11-05"
categories: 
  - "tips"
  - "何か"
tags: 
  - "ipv6"
  - "redmine"
  - "smtp"
  - "ubuntu"
---

はい。

環境はUbuntu 14.04 + nginx + unicorn, Redmine 2.5.1、さくらのVPS。

とりあえず普通にconfig/configuration.ymlに設定を書いて管理画面からテストメールを送信してみるのだが、Execution expiredとエラーが出る。時間がかかるのでタイムアウトっぽい。sendmail代替のssmtpを入れて、そこからメールを送ってみるがダメ。

結論から言うと問題が2つあった。

- hostnameを後から変えていたので、IPアドレスから逆引きできるものと違っていた
- うちのプロバイダのDNSサーバでsmtp.gmail.com をIPv6で解決できなかった サーバからsmtp.gmail.comへv6で繋がらなかった (2014/11/09 訂正)

つらい。

前者の問題は割とぐぐると出てきたので、すぐに気付いて修正した。hostnameをデフォルトのものに戻してあげたところ、ssmtpから送れるようにはなった。但し2分くらいかかる。なんぞ。Redmineは気が短いのかExecution expiredに落ちる。

ssmtpにvオプションをつけて実行してみると、

user@hostnamee~$ echo "test mail 4321"|ssmtp -v "test" \*\*\*@gmail.com
(ここで2分かかる)
\[<-\] 220 mx.google.com ESMTP \*\*\*\*\*\*\*.68 - gsmtp 
\[->\] EHLO hostname.sakura.ne.jp
\[<-\] 250 SMTPUTF8 
\[->\] STARTTLS
(以下正常に進む)

 

ふむ。

いろいろ調べてみるがわからず、telnetなど試していたところ、smtp.gmail.comが解決できないことがあることがわかった。pingは解決できるけどping6はできない。resolv.confを見直せ、というのは散々見かけたのでnslookupはしていたのだが、v6だけ解決できないというのは盲点であった。v6で試して、タイムアウト後にv4にフォールバックしていたんですかね。つらかった。sysctlをいじってv6まるごと無効にして解決（すいません）。こうしてv6の普及は遅々として進まないんですね（他人事）。

ちなみに、Gmailを諦めてOutlook.comのメール(\*\*@live.jp)で試してみたところ、一瞬で接続できて送信できたんですが、

 

Requested action not taken; We noticed some unusual activity in your Hotmail account. To help protect you, we've temporarily blocked your account.

と出て一発でアカウントをロックされました。マジかよ……。とりあえず解除申請しようとしたんですが、携帯キャリアのメールアドレスがないとだめらしいです。シンジラレナイ。サポートセンターにメールしましたが使えるのはいつになることやら。やっぱGoogle様ですね。とりあえず、僕のようにIIJに移行してしまったような人はOutlookに無茶なアクセスをするのはやめたほうがよさそうです。

ここまで7時間。つらい。v6が普及するのが先かメールが滅びるのが先か。どっちも来ないのかもしれない。
