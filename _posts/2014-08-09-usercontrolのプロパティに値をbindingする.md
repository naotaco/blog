---
title: "UserControlのプロパティに値をBindingする"
date: "2014-08-09"
categories: 
  - "tips"
tags: 
  - "csharp"
  - "windowsphone"
---

BindingとUserControlはとても便利なのであわせてWPアプリ開発でも使いたいところ。詰まったところをメモしておきます。どうでもよいですがWindows関係は、.NETで使えるのかSilverlightで使えるのかStore appで使えるのかPhoneで使えるのかぱっと見分からない情報が多くて困りますね。なおWP8に関する日本語の情報はほぼ存在しない模様。

### Binding

やり方はいろいろあるようですが、UIElementのDataContextにオブジェクトをセットする方法を使っています。DataContextが内外から変更できてしまうからイマイチとかいう向きもあるようですが、楽なので。

pageのXAMLに置いてあるButtonやらRectangleやらのプロパティに、設定したい値を持ってるINotifyPropertyChangedなオブジェクトのプロパティをセットして、値の更新をUIに即時反映するようなアレです。らくちん。多用しまくるとパフォーマンス大丈夫なのかなと心配になりますが、ユーザが新しい端末を買い続けてくれれば問題ありません。詳しいことは意味の分からない[MSDNのページ](http://msdn.microsoft.com/ja-jp/library/ms184414%28v=vs.110%29.aspx)をどうぞ。

Buttonとか、組み込みのUIElementたちにはこれで好きな値をBindingすればいいだけなので、弊プロジェクトでは多用しています。

よくわからなくなったので（後述）、サンプルアプリを作って試しました。

[https://github.com/naotaco/BindingTest](https://github.com/naotaco/BindingTest)

### Binding on UserControl

UserControlは特定のUI部品を作りたいときに超便利なのでしょっちゅう使ってます。だんだんエスカレートして、組み込みのUIElementみたいにプロパティにBindingさせろよという気になってきたのでちょっと調べました。

まず、Bindingなしで、固定値をpageのXAMLから設定するときは、UserControlのプロパティをpublicにしてあげればそれだけでOKです。

 

\[csharp title="UserControlのコードビハインド"\] public partial class MyBrandNewSlider : UserControl { ... public bool Checked { get; set; }

... \[/csharp\]

\[xml title="pageのXAML"\] <phone:PhoneApplicationPage xmlns:controls="clr-namespace:BindingTest.Control" ... <controls:CheckboxControl Name="ControlCheckbox" Checked="false" />

... \[/xml\]

 

こんなかんじで。

だがうきうきして下記みたいにプロパティにBindingを使ったらExceptionが起きて死んだ。

 

\[xml title="pageのXAML"\] <phone:PhoneApplicationPage xmlns:controls="clr-namespace:BindingTest.Control" ... <controls:CheckboxControl Name="ControlCheckbox" Checked="{Binding Checked, Mode=TwoWay}" />

... \[/xml\]

ここでBindingしてるのは値を抱えてるINotifyPropertyChangedを実装したオブジェクトのプロパティで、このオブジェクトは既に親のUIElementのDataContextにセットされてる。UserControlにBindingしたときだけ落ちる…

で、調べて見つけた今回の参考文献：[http://www.geekchamp.com/tips/how-to-expose-properties-of-a-user-control-in-windows-phone](http://www.geekchamp.com/tips/how-to-expose-properties-of-a-user-control-in-windows-phone)

言われるがままに、UserControlにコードを足す。

 

\[csharp title="UserControlのコードビハインド（Binding対応版）"\]

public bool Checked { /\* get; set; このままだとNG. 末尾参照のこと。 \*/ get { return (bool)GetValue(CheckboxProperty); } set { SetValue(CheckboxProperty, value); \_CheckBox.IsChecked = value; } }

public static readonly DependencyProperty CheckboxProperty = DependencyProperty.Register( "Checked", typeof(bool), typeof(CheckboxControl), new PropertyMetadata(false, new PropertyChangedCallback(CheckboxControl.StateChanged)));

private static void StateChanged(DependencyObject d, DependencyPropertyChangedEventArgs e) { (d as CheckboxControl).Checked = (bool)e.NewValue; }

... \[/csharp\]

こんなかんじ。

こうするとDataContextのプロパティが変わったらUserControlに用意したコールバックが呼ばれます。なんで自分でセットしなきゃならんのじゃという気もするが。（なにかいい方法ないのか）

誤りとかもっとよい方法などあったら教えてくださいませ。

 

* * *

### 追記(2014/11/09)

初出時、変更後もプロパティを get; set; のままとしていましたが、下記コメントをいただきました。

<blockquote class="twitter-tweet" lang="ja"><a href="https://twitter.com/naotaco">@naotaco</a> UserControlにバインディングするやつ、アクセサの中身は DependencyObject.Get/SetValue() にしとかないと TwoWay バインドのときにおかしくなるようなきがするんだけど大丈夫なのかな（自分で試してない。。）<div></div>— hal1932 (@hal1932) <a href="https://twitter.com/hal1932/status/528554584352882689">2014, 11月 1</a></blockquote>
<script src="//platform.twitter.com/widgets.js" async charset="utf-8"></script>

 

[試してみたところ](https://github.com/naotaco/BindingTest)、おっしゃるようにTwowayでバインドするとうまく動きませんでした（Controlのプロパティの変更がDataContextのプロパティに伝わらない）。ありがとうございます！
