# Amazon Dashボタンで今日は休みますメールや、HDDを消したりします

Amazonのセールなどが行われると、Dash Buttonが100円という破格の値段で解放されます　　
Wifiにボタンを押すとアクセスして、Amazon社に対してあらかじめハードウェアに紐づいている商品を購入するものです  

これを多少いじると、LinuxやUnixマシンで任意のコマンドを実行することができ、大変便利です  

nodejsでやられている方が多いですが、私は簡単なことにはPythonをよく使うので、Pythonで簡単に構築できるので、構築します  

## Amazon Dash Buttonの登録
まずは、Amazon Dash Buttonを登録します　

登録にはiOSかAndroidのスマホかタブレットが必要です　　

手順を忘れそうになるので、写真で記載します　　

注意点としては、普通に手順を進めると商品をボタンを押すたびに買わされてしまうので、最後の商品選択の画面で、右上のバツボタンを押すことです　　

<p align="center">
  <img width="100%" src="https://bytebucket.org/snippets/nardtree/6k6prr/raw/aaf3704e30161630a8cc60c46fe8ecf63abd6967/dash.png">
</p>

<p align="center">
  <img width="100%" src="https://bytebucket.org/snippets/nardtree/6k6prr/raw/aaf3704e30161630a8cc60c46fe8ecf63abd6967/dash2.png">
</p>

## amazon-dashモジュール
Pypiにはamazon-dashモジュールが公開されており、yml形式で命令を指定すれば、任意のコマンドが実行可能です

```console
$ sudo pip3 install amazon-dash
```

YML形式はこのようになっており、amazon-dashボタンごとにユニークなMACアドレスが振られていて、それを指定して、コマンドを記述できます  

今回は、今日は会社休みますメール（ポカリスエットのダッシュボタン）と、ホームフォルダ以下を全消去するコマンド（フルグラのダッシュボタンの設定です）
```yml
settings:
  delay: 10
devices:
  50:f5:da:95:d2:24:
    name: フルーツグラノーラ
    user: alice
    cmd:  rm -rf /home/alice/*
  fc:a6:67:35:17:81:
    name: ポカリスエット
    user: bob
    cmd: /home/bob/sdb/amazon-dush-hack/amazon-dash-hack/scripts/attendance.py
```
