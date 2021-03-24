---
layout: single
title: "Windows 10 Anniversary Updateを適用後、短時間のフリーズが頻発する件"
date: "2016-08-25"
categories: 
  - "tips"
  - "何か"
tags: 
  - "windows10"
  - "windows10-anniversary-update"
---

Updateしてからというもの、ちょっと何かする(アプリを立ち上げるとか、その程度)と30秒くらいOSまるごとフリーズするプチフリっぽい現象が頻発していた。かなり厳しい。

イベントビューワを見るとstorahciとかいうのが死んでいるらしい。

![storahci](https://blog.naotaco.com/assets/images/posts/2016/08/storahci.png)

Level: Warning
Source: storahci
Event ID: 129

General:
Reset to device, \\Device\\RaidPort0, was issued.

…

調べまくっていると下記フォーラムを発見。

[http://answers.microsoft.com/en-us/windows/forum/windows\_10-update/windows-10-anniversary-freezingpausing/b0c321e2-5dd5-4a5b-932e-32e5273c25ea?page=2](http://answers.microsoft.com/en-us/windows/forum/windows_10-update/windows-10-anniversary-freezingpausing/b0c321e2-5dd5-4a5b-932e-32e5273c25ea?page=2)

回避策っぽいのが書いてあったので試してみたところ、症状が治まっているようにみえる。

1. レジストリエディタを開く
2. 一応バックアップをとっておく
3. HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\storahci\\Parameters\\Device に行く
4. "NoLPM"というキーがあるはず。
5. 最後の行に、固まるSSDの名前(デバイスマネージャに表示されている名前)の末尾に\*(アスタリスク)を1文字足したものを追記する
6. 終了して再起動

![NoLPM](https://blog.naotaco.com/assets/images/posts/2016/08/NoLPM.png)

僕の環境では"SanDisk SDSSDXPS240G"がドライブ名なので、こんなかんじに"SanDisk SDSSDXPS240G\*"を足した。

理屈がまったくわからないが、再起動してみると確かに発生しなくなっている。いいのかこれで。とりあえずさっさと直して欲しいところだが。

調べてみるとLPMというのは省電力系の設定らしい。最初に調べたときは省電力系の設定が怪しいということだったのでコントロールパネルから全てオフにしていて、当然ハードディスクの電源を切る設定も無効にしていたのだが症状がでていた。NoLPMをレジストリに明記したら直ったので、この辺がばぐってるのか、仕様が変わったのか。勘弁してくれ、、
