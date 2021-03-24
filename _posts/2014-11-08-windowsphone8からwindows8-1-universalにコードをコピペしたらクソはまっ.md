---
title: "WindowsPhone8からWindows8.1 universalにコードをコピペしたらクソはまった話"
date: "2014-11-08"
categories: 
  - "tips"
  - "何か"
tags: 
  - "csharp"
  - "visualstudio"
  - "windows"
  - "windowsphone"
---

愚痴です。

[UserControlを作ってそのプロパティにデータをbindすること](https://blog.naotaco.com/archives/534 "UserControlのプロパティに値をBindingする")はたくさんあると思いますが、WindowsPhone8用に書いてたプロジェクトからWindows 8.1 Universal (Phone/Windows)のプロジェクトにコードをコピペしたらドはまりした愚痴です。

PropertyMetadataのコンストラクタのオーバーロードが、PhoneとUniversalで違っているっぽいです。[MSDNのページ](http://msdn.microsoft.com/ja-jp/library/ms557330%28v=vs.110%29.aspx)には記載が見当たりませんが、PropertyChangedCallback 1引数のみのコンストラクタがUniversalには無くなっています。

### Windows Phone 8 project (VS2012)

[![2012_1](https://blog.naotaco.com/assets/images/posts/2014/11/2012_1.png)](https://blog.naotaco.com/assets/images/posts/2014/11/2012_1.png) [![2012_2](https://blog.naotaco.com/assets/images/posts/2014/11/2012_2.png)](https://blog.naotaco.com/assets/images/posts/2014/11/2012_2.png) [![2012_3](https://blog.naotaco.com/assets/images/posts/2014/11/2012_3.png)](https://blog.naotaco.com/assets/images/posts/2014/11/2012_3.png)

 

### Windows 8.1 universal project (VS2013)[![2013_1](https://blog.naotaco.com/assets/images/posts/2014/11/2013_1.png)](https://blog.naotaco.com/assets/images/posts/2014/11/2013_1.png) [![2013_2](https://blog.naotaco.com/assets/images/posts/2014/11/2013_2.png)](https://blog.naotaco.com/assets/images/posts/2014/11/2013_2.png)

 

 

なんやこれ。

もともとWP8アプリで2 of 3のコンストラクタを使っていたぼくは思いっきりコードをコピペして2時間くらい悩んでいたのですが、1引数で渡していたCallbackがいつのまにかデフォルト値になっていただけだったのでした。せめてPropertyChangedCallbackをintにキャストした段階でException投げてくれよ。。。。

つらかった。

真に型安全な世界を探して生きていきたいです。
