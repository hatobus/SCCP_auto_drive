# Raspberry piでストリーミング

Raspberry piにWebカメストリーミング再生する方法．

### TODOリスト

- MJPG-streamerのインストール
- デーモン化（自動起動設定）

### まずはMJPG-streamerをインストールする．

参考にしたのは[こちら](http://www.hiramine.com/physicalcomputing/raspberrypi3/webcamstreaming.html)，ここに書かれているコードを一通り見ればインストールは可能．

メモ程度にコードを書き留めておく．

1. 最新のパッケージリストを取得．
	`sudo apt-get update`

2. MJPG-streamerに必要なパッケージをインストール
	`sudo apt-get install subversion libjpeg-dev imagemagick`

3. MJPG-streamerのソースファイルの取得とコンパイル（make）
	`svn co https://svn.code.sf.net/p/mjpg- streamer/code/mjpg-streamer mjpg-streamer`

	`cd mjpg-streamer`
	
	`make`
	
とりあえずこれでMJPG-Streamerが起動するようになる．
起動のためのコマンドは．
`sudo ./mjpg_streamer -i "./input_uvc.so -f 10 -r 320x240 -d /dev/video0 -y -n" -o "./output_http.so -w ./www -p 8080"`

となる．あとは同一LAN上にいるPCのブラウザで．
![](https://i.imgur.com/YnARTL1.png)

`Rasppi's IP:8080`
を入力することで，ストリーミング画面が見ることができる．

## 自動起動設定

このままだと，いつもターミナル上からコマンドを叩かなくてはいけず，起動させるのが面倒になる．そのため自動起動のためのスクリプトを作成する．

1. Raspberry pi上の`home/`に`tool`などのフォルダを作成する．

2. `tool`フォルダ内に`stream.sh`を置く．これで起動時に実行されるシェルを作成できる．


3. アクセス権を変更．

	`chmod 700 stream.sh`

4. スクリプトをデーモン化
	※デーモンは，LinuxやUNIXにおいてメモリ上に常駐して様々なサービスを提供するプロセスを指す。
	
	Supervisorによってスクリプトをデーモン化する。

	そのためにまずは、Supervisorのインストール


	`sudo apt-get update`
	`sudo apt-get install supervisor`

5. 設定ファイルを次のコマンドで作成。

	`sudo vim /etc/supervisor/conf.d/mjpg_streamer_boot.conf
`
	内容としては以下の通り
	```mjpg_streamer_boot.conf
	[program:mjpg_streamer_boot]
	command=/home/pi/tool/stream.sh
	user=root
	autostart=true
	redirect_stderr=true
	stdout_logfile=/var/log/supervisor/mjpg_streamer_boot.log
	stdout_logfile_maxbytes=1MB
	stdout_logfile_backups=1
	stdout_capture_maxbytes=1MB
	```
	
6. ひとまずこれで自動起動の設定は完了．
	
	`sudo reboot`

	コマンドでRaspberry piを再起動できるので再起動し，実際にMJPG-Streamserが起動しているかを確認する．
	
	ちなみに，MJPG-StreamerはスマホでもPCでも閲覧が可能である．
