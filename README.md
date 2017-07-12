# Amazon Dashボタンで今日は休みますメールや、HDDを消したりします

Amazonのセールなどが行われると、Dash Buttonが100円という破格の値段で解放されます　　
Wifiにボタンを押すとアクセスして、Amazon社に対してあらかじめハードウェアに紐づいている商品を購入するものです  

これを多少いじると、LinuxやUnixマシンで任意のコマンドを実行することができ、大変便利です  

nodejsでやられている方が多いですが、私は簡単なことにはPythonをよく使うので、Pythonで構築します  

## 必要用件
- Amazon Dash Button
- Bluetooth対応のiOS or Androidデバイス
- Wifi環境
- Linux or Unixマシン
Amazon Dash Buttonの特徴から、ネットワークのAmazon　Dash Buttonの通信を検知するので自宅サーバがなければ運用できないです。Rasphberry PIとかいいかも  

## Amazon Dash Buttonの登録
まずは、Amazon Dash Buttonを登録します　

登録にはiOSかAndroidのスマホかタブレットが必要です　　

手順を忘れそうになるので、写真で記載します　　

注意点としては、普通に手順を進めると商品をボタンを押すたびに買わされてしまうので、最後の商品選択の画面で、右上のバツボタンを押すことです　　

<p align="center">
  <img width="100%" src="https://bytebucket.org/snippets/nardtree/6k6prr/raw/aaf3704e30161630a8cc60c46fe8ecf63abd6967/dash.png">
</p>

<p align="center">
  <img width="100%" src="https://bytebucket.org/snippets/nardtree/6k6prr/raw/488a7a6b7d7bb97b4fbce1f4fa96b4e23c0e28be/amazon-dash3.png">
</p>

## amazon-dashモジュール
Pypiにはamazon-dashモジュールが公開されており、yml形式で命令を指定すれば、任意のコマンドが実行可能です

```console
$ sudo pip3 install amazon-dash
```

まず、Amazon Dash ButtonのMACアドレスを調べます  
このアドレスに紐づけて後述のymlで動作を指定しますので、メモ帳に記録しておきます  
```console
$ sudo amazon-dash discovery
20:3c:ae:66:d8:02
c0:25:a2:f4:62:b0
fc:a6:67:35:17:81 <- ボタンを押して直後に現れたMACアドレスが該当のAamazon Dash Button
...
```

命令をYML形式のファイルを作成し、rootのオーナーに変更します
```console
$ touch amazon-dash.yml
$ sudo chown root:root amazon-dash.yml
```

YMLはこのようになっており、amazon-dashボタン毎にユニークなMACアドレスが振られていて、それを指定して、コマンドを記述できます  
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

## pythonでメールを送る
本題ではないですが、gmailのSMTPサーバ経由で、「今日は会社を休みます」のメールを送ります　　
(正しいパスワードの運用はあまりわからないので、簡易的に別ファイルに、userid, password, mailaddressを保存してそこを参照しています)
```python
#! /usr/bin/python3
import smtplib

SECRET = { x:y  for x,y in map(lambda x:x.split('='), filter(lambda x:x!='', open('/opt/google_account1').read().split('\n') ) ) }
MAILS  = { x:y  for x,y in map(lambda x:x.split('='), filter(lambda x:x!='', open('/opt/mailaddrs').read().split('\n') ) ) }

msg = bytes("""
体調不良により、本日お休みをいただきたく思います。
どうぞよろしくお願いします。
""", 'utf8')
fromaddr = SECRET['GOOGLE_ACC']
toaddrs  = MAILS['KINTAI'] 

username = SECRET['GOOGLE_ACC']
password = SECRET['GOOGLE_PWD']
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
print('正常に送信が終了しました')
```
