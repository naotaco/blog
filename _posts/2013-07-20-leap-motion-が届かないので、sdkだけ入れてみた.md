---
layout: single
title: "Leap motion が届かないので、SDKだけ入れてみた"
date: "2013-07-20"
categories: 
  - "tips"
  - "何か"
tags: 
  - "c"
  - "leap"
  - "vs2012"
---

Leap motionが発送されるとかされたとか話題になってるけど、特に俺の所に届く気配がない。おもしろくないので、SDKでも入れてみようと思った。

とは言っても3Dとかグラフィックとかまったくわからないし、そもそもWin環境のアプリなんて書いたことないので、どっから手を付けたらいいかわからない。

VC++のsampleがあったので、ビルドできるまでの環境を整えることにした。Unityとかわかる気がしないし、Pythonもアレだしなあ。

1. SDKをダウンロード・解凍
2. VS2012を入れる
3. Boostを入れる
4. cinderを入れる
5. .NET Framework 4.0 SDKを入れる
6. いろんな設定を適当にいじる

としたら、やっと SDK\\Examples\\GesturesDemo が動くようになった。

### 1\. SDK

Leap motionに行ってDeveloper登録して、SDKをダウンロード。解凍して適当なところに置く。

このときいろいろ面倒だから、ExamplesとSDKの位置関係を壊さずに配置したほうがよい（自戒）

### 2\. VS2012

いれる。VS2012 for Windows Phoneは既にインストールしてあるのだが、for Windows desktopというのがあったので、そっちもインストールしてみた。違いはよくわからない。

両方いれたせいか前者の設定が一部desktopの方にも入っていたりして、かなりアレ

### 3\. Boost

いれる。

[http://rexpit.blog29.fc2.com/blog-entry-89.html](http://rexpit.blog29.fc2.com/blog-entry-89.html)

を参考に、ごりごりビルドする。

### 4\. Cinder

なにこれ？

とりあえず言われるままに入れる。

環境変数 LIBRARIES\_PATH を設定して、そこに置く。

ただREADMEにも書いてあるように、cinder\_0.8.4/を見に行くよう決め打ちで設定されてるので、頭をかかえつつ、VSからソリューションの設定を変える（後述）。

ここまではよかった。

###  5. .NET 4.0 SDK

とりあえずビルドしてみると、GL/gl.h がないとかいちゃもんをつけられる。

.NETのSDKを入れると手に入るとのことだったので、

[http://www.microsoft.com/en-us/download/details.aspx?id=8279](http://www.microsoft.com/en-us/download/details.aspx?id=8279)

これを入れると、

C:\\Program Files\\Microsoft SDKs\\Windows\\v7.1\\Include

ここにヘッダができるので、これを設定に追加（後述）。

ちなみに、cinder\_0.8.5\\include\\cinder\\gl\\　にもgl.hがあるが、こっちにパスを通してもだめだった。よくわからない。

### 6\. 設定かえる

だいぶ心が折れてきて、Perl@Ubuntuな世界に帰りたくなる。

まずcinderの参照先を片っ端から変えて回る。

GestureDemoを右クリックしてプロパティを開き、構成プロパティの中身をぜんぶみる。

悲しいことに何カ所もcinder\_0.8.4ってべた書きしてあるので、ぜんぶ0.8.5に変えたらなんとかなったっぽい。

最初からcinderのフォルダ名を0.8.4に変えて置けばよかった…

 

次にgl.hのために

C:\\Program Files\\Microsoft SDKs\\Windows\\v7.1\\Include

をC/C++ -> Additional Include Directories あたりに追加する。

あと

C:\\Program Files\\Microsoft SDKs\\Windows\\v7.1\\Lib

をLinker -> Additional Library Directories あたりに追加する。他にも必要かもしれない。

 

そしてこれが必要かはわからんのだが、General -> Platform toolset がなぜかWindowsPhoneになってたので、Visual Studio 2012 (v110)にしてやる。

そしたらこんどVectorがないとかRamdomがないとかわけのわからないことを言いだしたので、

gl.hのときと同様、

C/C++のincludeに、 C:\\Program Files (x86)\\Microsoft Visual Studio 11.0\\VC\\include

Linkerに　C:\\Program Files (x86)\\Microsoft Visual Studio 11.0\\VC\\lib;

を足してやる。

あとLinkだかDebugのあたりで、

module machine type 'x64' conflicts with target machine type 'X86'

とか言われる（逆かも）ので、

Linker -> Advanced -> Target Machine を MachineX86 (/MACHINE:X86) にしてやる。

これでやっとbuildとlinkが通った。

最後、Debugのところで

_error MSB3073_: copy /Y　～～～　はコード1で終了しました

とか言われてこけたが、これはこのcopyするファイルが存在しないというだけだったので、

コピー元の場所（..\\..\\..\\..\\LeapSDK 的なところだった）にSDKを置いて終了。

SDKが物理的に何カ所かにあることになってしまってアレだけどなんかもう面倒だからいいや。

無事ビルドが通り、デバッグ開始と押すと、サンプルが動作した。

 

あとはLeapが届けば遊べるはず。GLぜんぜんわからないけど。
