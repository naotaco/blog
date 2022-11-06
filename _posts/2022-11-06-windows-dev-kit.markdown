---
layout: single
title: Windows開発キット2023を買った
date: 2022-11-06 18:40:35 +09:00
categories: PC Windows ARM64
header:
  image: /assets/images/posts/20221027223858-N0108580-converted.webp
---

突然[Windows開発キット2023](https://www.microsoft.com/ja-jp/d/windows-%E9%96%8B%E7%99%BA%E3%82%AD%E3%83%83%E3%83%88-2023/94k0p67w7581?activetab=pivot:%E6%A6%82%E8%A6%81tab)なるものが発売されたので、いったいこれはなんだと思っていたのだがどうやらARMマシンらしいので、とりあえず勢いよく買ってみた。ストアで値段がめちゃくちゃな設定になっていたりして話題になっていたが、99880円が正しい値段である。安くはないが、ついうっかりを防ぐ値段ではない。

さて、これは以前Project Volterraとして発表されていたやつが発売されたものらしく、Snapdragon 8cx Gen3が乗っているらしい。SoCだけでいえばThinkPad X13s Gen 1と同じだ。発表されたときはWindowsにもついにARMがみたいな雰囲気もなくはなかったが、当然というべきかそれ以降続いて出てきた話は聞かない。ノートPCだと扱いに困るが、コンパクトなデスクトップならなんとかならんか……？という期待で買った。

[![Snapdragon Compute PlatformとCPU名が表示されているタスクマネージャの画面](/assets/images/posts/2022-11-06-23-33-36.png){:width="80%" .align-center} ](/assets/images/posts/2022-11-06-23-33-36.png)

単にARMネイティブアプリの開発に加えて、Snapdragonに搭載されているNPUで高速に推論ができて、その開発もこのDev Kitならできますよというのが売りっぽい。ARMのところはわかるが、NPUのほうはさっぱりわからん。もともとPCでもGPUコードだと環境差分がありそうなんだけどどうやって開発してるんだろうか。

### 開封

Dev Kitとは言うものの、ほとんど普通の（シュッとした見た目のせいでポートが貧弱な）PCと変わらない気がする。ACアダプタが冗談みたいに大きいのはなんなんだ。PD 100Wで動くくらいにしてくれればよかったのに……。

[![Dev Kitの梱包。無地の段ボール箱。](/assets/images/posts/20221027223812-N0108578-converted.webp){:width="80%" .align-center} ](/assets/images/posts/20221027223812-N0108578-converted.webp)

[![Dev Kitを開封したところ。Microsoftロゴの入った不織布に覆われた本体が見える。](/assets/images/posts/20221027223753-N0108577-converted.webp){:width="40%" .align-center} ](/assets/images/posts/20221027223753-N0108577-converted.webp)

[![Dev Kitを出したところ。黒い本体にMicrosoftロゴが入っている。](/assets/images/posts/20221027223858-N0108580-converted.webp){:width="80%" .align-center} ](/assets/images/posts/20221027223858-N0108580-converted.webp)

唯一Dev感があったのはこの説明書きで、USB-Cからの起動をする専用のボタンがあるらしい。USB-Cからの起動と言われてもピンとこないが、起動するSSDをUSB-Cにつなげば、都度起動するのに便利ということなのだろうか。

[![同梱の説明書き。各ポートやボタンの名称が書いてある。](/assets/images/posts/20221106_win-devkit-guide.webp){:width="50%" .align-center} ](/assets/images/posts/20221106_win-devkit-guide.webp)

画面出力はminiDP（どうして……）とUSB-Cなのだが、POST画面はminiDPにしか出ないのでそちらが推奨とのこと（[公式FAQ](https://www.microsoft.com/ja-jp/d/windows-%E9%96%8B%E7%99%BA%E3%82%AD%E3%83%83%E3%83%88-2023/94k0p67w7581?activetab=pivot:faqtab#tab2e59d3230-b6e3-47be-99f6-f2aee9652077)より）。アクティブタイプのHDMI変換を使うようにとも書いてあったので、Amazonで適当に買ってHDMI変換して画面に出している。4Kだが当たり前のように動く。

ネットワークは有線のみなのかなと思ってセットアップのときはLANケーブルをさしていたのだが、あとから設定を見ると普通にWi-Fiが使えている。これ最初から使えたっけか…？とりあえず、クソデカACアダプタをのぞけば設置は容易そうである。

ちなみにFAQで笑ったのはこれ。

> Q: より効率的なラボテストを行うために、複数の Windows 開発キット 2023 デバイスを積み重ねて使用することはできますか?  
> 可能な場合、何台積み重ねることができますか?  
> A: このデバイスは、独自のオンサイト開発やラボテスト用に配置して積み重ねることができます。  
> 最大2台のデバイスを積み重ねて効率的なテストを行うことができます。  

[Project Volterra発表時に積み重ねられることにしてしまった](https://www.itmedia.co.jp/news/articles/2205/25/news073.html)からこういうFAQになったようだが、結局スタックはなぜか2台までに制限されている。そんなに重くもないし華奢な筐体にも思えないので、放熱の都合だろうか。

### 環境構築

起動すると普通のWindows 11の初回起動と（たぶん）同じように動いて、特にARMであることは感じられない[^1]。適当にWebからソフトをソフトを落としてインストールすると、x86/AMD64でも普通にエミュレーションで動いてしまうので意外とARMであることが感じられない。いくつか試した範囲だと次のような状況であった。

- Firefox: WebからダウンロードするとデフォルトでARM版がインストールされる。当然のように動く
  - が、ときどき固まったりするのであまり安定しているとは言いがたい
- VS Code: ARM64版をダウンロード時に選択可能
- Windows Terminal: ストアからダウンロードしたら普通に動く。ネイティブARMなのかどうかすらわからない
- Slack: よくわからんが普通に動いている
- Sublime Text: x64版しかないが、おそらくエミュレーションで普通に動く
- Visual Studio: Preview版だがCommunity一式がインストールできて動き、ARMネイティブターゲットのデバッグが普通にできる
- MSYS2: [普通にサポート](https://www.msys2.org/wiki/arm64/)されている（後述）
- ATOK: 試した範囲では唯一動かなかった
  - インストーラは正常終了するが、IME切り替えでエラーになっているような挙動（ATOKに変更できず、操作前の言語に戻る）
  - JustSystemの対応一覧表にはARMのAの字もなく、残念ながら当然
- YubiKey: 特にドライバ設定等の操作をしたわけではないが、普通に動いてGitHub, GoogleにFirefoxでログインできた。

Windows名物のProgram Filesフォルダも、`Program Files`, `Program Files (Arm)`, `Program Files (x86)` の3種類に増えておりキモさも3倍である。

[![](/assets/images/posts/2022-11-07-00-39-00.png){:width="40%" .align-center} ](/assets/images/posts/2022-11-07-00-39-00.png)

しかもインストール場所の選択がまちまちっぽく、ネイティブARM64のFirefoxもx64のSublime TextもProgram Files無印にインストールされている。これもうわかんねえな。ちなみにバイナリファイルがなんのアーキテクチャなのかを表示するような機能がExplorer近辺には見当たらず、MSYSから `file` を叩いている有様。

```console
win-arm-devkit CLANGARM64 ~/blog
$ file /c/Program\ Files/Mozilla\ Firefox/firefox.exe
/c/Program Files/Mozilla Firefox/firefox.exe: PE32+ executable (GUI) Aarch64, for MS Windows

win-arm-devkit CLANGARM64 ~/blog
$ file /c/Program\ Files/Sublime\ Text\ 3/subl.exe
/c/Program Files/Sublime Text 3/subl.exe: PE32+ executable (console) x86-64, for MS Windows
```

Visual StudioでC++アプリを開発すると、見慣れた逆アセンブルが見られる。

[![Visual Studioの画面。ターゲットにarm64が選択されている。](/assets/images/posts/2022-11-07-01-35-45.png){:width="80%" .align-center} ](/assets/images/posts/2022-11-07-01-35-45.png)

[![Visual Studioで逆アセンブルした画面。add, ldrなどの命令とx8などのレジスタが使われている。](/assets/images/posts/2022-11-07-01-36-16.png){:width="80%" .align-center} ](/assets/images/posts/2022-11-07-01-36-16.png)

C#アプリでもみられるのだが、ターゲットがAny CPUなので、何が起きているのかはよくわからない（普段の開発のときも見たことがないし）。エミュレータの変換後のコードなのかな。

[![C#コードの逆アセンブル。よくわからない](/assets/images/posts/2022-11-07-01-39-28.png){:width="80%" .align-center} ](/assets/images/posts/2022-11-07-01-39-28.png)

これで一通りの環境がセットアップできてしまい、なんだかんだ普通に使えるようになってしまった（ブラウザがたまに固まるのは良いのかという話はあるが）。仮にも10万円出すならもちろんまともなPCの選択肢があるはずではあるが、そういうのは何台もすでに手元にあるので考えないことにする。

#### MSYS2の対応

先述のように普通に対応されていて、[公式のwiki](https://www.msys2.org/wiki/arm64/)の通りにするとCLANGARM64で起動する。といってもtoolchain以外は元のバイナリがエミュレーションで動いているって感じではあるが、すくなくともllvmはネイティブARM版が動く。git, opensshはMSYS版のままのようだ。

```console
win-arm-devkit CLANGARM64 ~/blog
$ file `which clang`
/clangarm64/bin/clang: PE32+ executable (console) Aarch64, for MS Windows
```

clangがARM版でインストールされるので、ARMネイティブC++コードのコンパイルができる。

普通にCLANGARM64で起動するためにはインストールフォルダにある `clangarm64.exe`  を実行すればよいのだが、Windows Terminalから使う場合はもう1か所変更が必要っぽい。

普段x64マシンの私の環境ではWindows Terminalから起動させるために次の設定が書いてある。

```json
            {
                "closeOnExit": true,
                "colorScheme": "Campbell",
                "commandline": "cmd.exe /c \"set MSYSTEM=MINGW64&& set MSYS=winsymlinks:nativestrict&& set MSYS2_PATH_TYPE=inherit&& C:/msys64/usr/bin/bash.exe --login\"",
                "guid": "{xxx}",
                "historySize": 9001,
                "icon": "C:\\msys64\\msys2.ico",
                "name": "MSYS2",
                "padding": "0, 0, 0, 0",
                "snapOnInput": true,
                "startingDirectory": "%USERPROFILE%",
              }
```

これはぐぐって出てくるどっかのForumの回答からのコピペなのだが（……）これだとARM環境でもMINGW64が起動してしまうので、 `commandline` 行の `MSYSTEM=MINGW64` の箇所を `MSYSTEM=CLANGARM64`  と書き換えてやる必要がある。

```json
"commandline": "cmd.exe /c \"set MSYSTEM=CLANGARM64&& set MSYS=winsymlinks:nativestrict&& set MSYS2_PATH_TYPE=inherit&& C:/msys64/usr/bin/bash.exe --login\"",
```

余談だが、デフォルトの設定が最近MINGW64からUCRT64に変更になったらしい。詳しいことはわからんが、そっちに乗り換えておく方がよさそうな気がするので一通り変更した。といってもARMの場合と同じで、普段使いのバイナリがUCRT64版になるのかというとほとんどそういうこともなさそうなのであるが。



### さらに余談

この記事はお約束通りDev Kitから書いている。ATOKが動いていないので日本語入力が地獄のような体験（変換精度がどうしようもないのに加え、On/OffのキーアサインがShift + Spaceに変更できないのがつらすぎる）ではあるが、それ以外は意外と何とかなっている。

そして今回は画像をWebPにしてみた（スクリーンショット以外）。適当にスマホで撮った写真をいい感じにこのマシン上で縮小する方法がなかったので、新しいアプリを探すことにしたのだが、どうせならWebPにしてみるか、という感じで。Microsoft Storeで検索して出てきた[to WebP](https://www.microsoft.com/store/productId/9N36BR61NLR7)を使ってみたのだが、かなり快適にリサイズ＆WebP変換ができた。メインマシンで書く時もこれでいいじゃんって感じだったのでそっちにもインストールした。MS Storeにまともに使えるアプリってあるんだなあ。

で、WebP表示をブラウザから確認してみると、画像をクリックしたときのLightBox的な動き？にならずに、単なるファイルへのリンクとして動いているっぽい。PNG/JPGの場合はそれっぽく表示してくれるので、できれば同じように動いてほしかったが。フィードバックしてみるか、と思ったがとっくに修正済みで、テーマをアップデートすればよかった。パーマリンクの仕様も変わったような気がしなくもないが、いちおうリダイレクトされているようなので考えるのをやめた。

[^1]: 最初にWindows UpdateをあてるまではSettingが開かないなどバグっぽい動きがちらほら見えていたが、ちゃんとアップデートしたら普通に動くようになった
