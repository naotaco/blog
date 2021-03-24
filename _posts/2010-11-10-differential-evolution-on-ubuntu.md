---
layout: single
title: "Differential Evolution on Ubuntu"
date: "2010-11-10"
categories: 
  - "tips"
  - "何か"
tags: 
  - "c"
  - "cpp"
  - "de"
  - "differencial_evolution"
---

Differential Evolution という手法があって、GAより少ない計算量で良い結果が出るかもしれないという話を聞いたので、試してみることにした。 とりあえず[http://www.icsi.berkeley.edu/~storn/code.html](http://www.icsi.berkeley.edu/~storn/code.html)でC++（けっこう種類があるのにPerlはなかった）のソース(devcpp.zip)を落としてきて、コンパイルしてみる。C++をまともに自分でコンパイルしたことがほとんど無かったので困った。Makefileくらいつけといてくれたらいいのに。仕方ないのでMakefileの書き方を勉強して書いた。

CXXFLAGS = -Wall
testobjs = DETest.o DESolver.o
bin = test

all: $(testobjs)
	$(CXX) $(CXXFLAGS) -o $(bin) $^

DESolver.o: DESolver.h DESolver.cpp
	$(CXX) $(CXXFLAGS) -c $^

DETest.o: DETest.cpp
	$(CXX) $(CXXFLAGS) -c $^

clean:
	rm $(testobjs) $(bin)

で、これでmake叩くがコンパイルは通らない。このページを良く読むと、MS Visual C++ 5.0とか書いてある。えー。g++じゃないんですか。僕の環境は、Ubuntu 10.04 + gcc 4.4.3です。VC++なんてもちろんないです。

$ make g++ -Wall -c DETest.cpp DETest.cpp:71: error: ‘::main’ must return ‘int’ DETest.cpp: In function ‘int main()’: DETest.cpp:96: error: return-statement with no value, in function returning ‘int’ make: \*\*\* \[DETest.o\] エラー 1

これはまあいい。main()がvoidじゃ嫌だというので、int型に直して、return 0;してあげればおｋ。

int main(void)
{
　　（中略）
	return 0;
}

で、またmake叩くが通らない。

$ make g++ -Wall -c DETest.cpp g++ -Wall -c DESolver.h DESolver.cpp DESolver.cpp: In member function ‘void DESolver::Setup(double\*, double\*, int, double, double)’: DESolver.cpp:57: error: argument of type ‘void (DESolver::)(int)’ does not match ‘void (DESolver::\*)(int)’ DESolver.cpp:61: error: argument of type ‘void (DESolver::)(int)’ does not match ‘void (DESolver::\*)(int)’ ・・・・・ （後略） えー。で、いろいろ調べて、そもそもこの::\*的な何かは関数ポインタ的な何かではないのか、とか勉強して、そもそも型が違うじゃないかと。とりあえず&つけとけばいいんじゃない？と思ってつけたら、コンパイラに&DESolver::hoge ってしろ、と言われたので、ぜんぶこうした。

    // 略
		case stBest1Exp:
		    calcTrialSolution = Best1Exp;
			break;

                //↑before after↓

		case stBest1Exp:
		    calcTrialSolution = &DESolver::Best1Exp;
			break;
    // 略

そしたらmake通って、無事Testプログラムも動作した。めでたしめでたし。まあ、この計算結果が正しいのかどうかは知らん。つーかDifferencial Evolutionって日本語だとあんまり情報無いんだけど、いまいちなのかな？あんまり新しい手法でもないみたいだし。まあ試してみるけど。
