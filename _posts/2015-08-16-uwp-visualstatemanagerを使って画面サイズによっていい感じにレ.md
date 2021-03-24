---
layout: single
title: "[UWP] VisualStateManagerを使って画面サイズ, 向きによっていい感じにレイアウトを変える"
date: "2015-08-16"
categories: 
  - "tips"
  - "何か"
tags: 
  - "uwp"
  - "windows10"
  - "windows10-mobile"
---

Windows10, Windows 10 mobileそれぞれで、同じプロジェクトのアプリケーションが動作するようになった。ここだけ聞くと夢の国に聞こえるが、例によって画面サイズの問題がついてまわる。はぁ。

VisualStateTriggerを使うと、groupごとにstateを定義して、画面サイズの変化によってstateを遷移させることができる。このときにXAMLのプロパティを変えたり、コードビハインドでハンドラを叩いたりさせることができる。

XAMLで定義した方がわかりやすそうなので試す:

https://gist.github.com/naotaco/f4d87b0d110e019faf7c

2つのVisualStateGroup(WindowWidthStates, WindowHeightStates)を定義して、その中にstate, それぞれの遷移トリガを設定しておく。いまのところAdaptiveTriggerのプロパティとして使えるのはMinWindowsHeightとMinWindowWidthだけっぽいので、画面サイズくらいにしか使えなさそう。

こうしておくと、State遷移時にSetterに書いておいたプロパティを設定してくれるので、動的レイアウトを簡単に実現できる。

このVisualStateGroupの指定はUI Elementごとなので、書く場所を間違える（Gridの外に書くとか）すると動かない。

 

で、stateの遷移をコードビハインドでも知りたいのが人情なので、こうする:

https://gist.github.com/naotaco/ece74f2c3b785e33eba9

こんなかんじでVisualStateManagerに対してハンドラを追加できる。groupごとに指定できるので、(少なくとも今は幅・高さしか指定できないが)トリガごとにハンドラを分けることができる。いい感じである。groupやstateを動的に足したりすることも出来そう(試してない)。

* * *

手元のWindows10 desktopで試してみたら、ウィンドウの画面サイズ変更でもちゃんとレイアウトが変化する。またWindows 10 mobileだと画面の縦横回転でも判定がちゃんと走る。よしよし。

(追記: 2015/10/03)

5inch Full HDのLumia 930だと360x600くらいの画面サイズになった。さすがに5インチの画面でPCと同じレイアウトにしてしまうとアレなので、おとなしく[MSの言うsize classes](https://msdn.microsoft.com/en-us/library/windows/apps/dn958435.aspx#sizeclasses)に従って720を閾値にPhoneとTablet/PCで分けることにした。Windows10 desktopならアプリがウィンドウで起動するから全画面で使う人もそう多くないだろうし、Tabletと同じでよさそう。

またPhoneだと画面の縦横が気になるが、これはDisplayInformationクラスから取得できる。(GetForCurrentView()に気付かず30分くらいはまった)

https://gist.github.com/naotaco/e8c5a46d915777b29b54

かんたん。

デスクトップでウィンドウを縦長にされたときのこととかも考えると、画面の向きより縦横比で実装した方が汎用性があってよさそうだが。

ということで、いまのアプリでは、画面の幅が720以下になったら右ペインを非表示(ボタン押したら出てくる), 画面の高さが720以下になったら下のGridを非表示にすることにした。だいぶいい感じである。

ほんとは360と720を両方閾値に使って、Phoneにおける縦横もVisualStateManagerで別のレイアウトにしたいところなのだが、さすがに縦横3サイズで9パターンのレイアウトはテストが面倒すぎるので見送った。5インチは十分小さいからあんまり情報を出したくない。
