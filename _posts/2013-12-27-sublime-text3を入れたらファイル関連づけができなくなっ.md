---
layout: single
title: "Sublime text3を入れたらファイル関連づけができなくなってクソッってなった話"
date: "2013-12-27"
categories: 
  - "tips"
tags: 
  - "sublimetext"
---

Sublime text3が出たというので入れた。（2が既にインストールしてあったが、別のプログラムとしてインストールされた）

各種ファイルの関連づけを3の方にしようとしたのだが、何度やっても起動するのは2でどうにもならない。

ぐぐったらSublimeのフォーラムに解決策が。

[http://www.sublimetext.com/forum/viewtopic.php?f=3&t=10800](http://www.sublimetext.com/forum/viewtopic.php?f=3&t=10800)

> FIX: Open Regedit Navigate to HKEY\_CLASSES\_ROOT\\Applications\\sublime\_text.exe\\shell\\open\\command
> 
> The Data field in this string key is probably mapped to the old version. Change this to the correct filepath
> 
> C:\\Program Files\\Sublime Text 3\\sublime\_text.exe
> 
>  

たしかに、このレジストリキーの値にsublime text2のパスが書いてあったから3のに変更したら直った。うーむ

関係ないですが、sublemacsproを入れるとemacs風キーバインドとSublimeキーバインドがまざって大変なことになってるので、 設定ファイル[(https://github.com/grundprinzip/sublemacspro/blob/master/Default.sublime-keymap)](https://github.com/grundprinzip/sublemacspro/blob/master/Default.sublime-keymap) を読んで操作を把握してるんですけどなんかいい方法ないですかね？

デフォルトにemacs風カーソル移動だけ足そうかなあ。
