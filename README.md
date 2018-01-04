# SCCP_auto_drive

I want to Shishi 

[![SUSHI-WARE LICENSE](https://img.shields.io/badge/license-SUSHI--WARE%F0%9F%8D%A3-blue.svg)](https://github.com/MakeNowJust/sushi-ware)

## 最初に

これは会津大学課題プロジェクト「自動車の自動運転」についてのレポジトリとなります．

### 使うもの

今回使用するものは主にamazonや秋月電子で購入できるものを軸に使用しています．

- モータードライバ DRV8830 
    秋月などで購入することができます．表面実装済みですのである程度使いやすいことが特徴です．I2Cで動かすのでそれなりに知識が必要ですが慣れてしまえば
    簡単に動かすことができます．二つ使用するのでどちらかのアドレスを変更する作業をする必要があります．
    [購入](http://akizukidenshi.com/catalog/g/gK-06489/)
    [データシート](http://akizukidenshi.com/download/ds/akizuki/AE-MOTOR8830_manual.pdf)
    
 - ~~測距モジュール HC-SR40
    Amazonで購入，超音波型です．安いのが特徴で6個程搭載しています．これはGPIOで動くのでI2Cよりは操作がしやすいと思います．~~
    [購入](http://amzn.asia/jd95G4C)
    [データシート](http://akizukidenshi.com/download/ds/sainsmar/hc-sr04_ultrasonic_module_user_guidejohn_b.pdf)
	
 - 測距モジュール LV-EZ1
 	HC-SR40を使用すると，精度が出ず，値がバラバラになる．そのため，同じ超音波を使って測距するLV-EZ1を使用した．PWM制御ができ，GPIOピンを一つしか使用しないのである程度は使いやすい．
	[購入](https://www.switch-science.com/catalog/139/)
	[データシート](http://maxbotix.com/documents/LV-MaxSonar-EZ_Datasheet.pdf)

 - ギアボックス ダブルギヤボックス 左右独立4速タイプ 
    amazonなどで購入することができます.左右独立なので小回りを利かせることができます．
    [購入](http://amzn.asia/8rwZjWK)
    
 - タイヤ 楽しい工作シリーズ（パーツ） No.111 スポーツタイヤセット （56mm径） [購入](http://www.tamiya.com/japan/products/70111/index.html)
 
 - ブレッドボード * 2
 - Raspberry pi 3
 - ジャンパケーブル
 
### 言語
  Python2系統，Raspberry piにデフォルトで入っているpythonのバージョンがpython2系統のためpython2での実装になります．
  Jupyter notebookというIPython notebookのフレームワークを用い，ssh接続などをせずブラウザ上でファイルを編集することができます．
  
  元はデータ処理のフレームワークだったこともあり，のちのディープラーニングのステップでの使用を見越した利用になります．

### Raspberry piのホスト名について
  ホスト名は，研究室で使っていて，固定IPにするとRaspberry piが死ぬことになるので，Raspberry piのホスト名をHatopiに変更．
  これにより，Bounjourを使用して，`ssh pi@Hatopi.local`でssh接続ができるようになる．
  これでIPが変更されても，sshで入ってIPを確認することができる．
  2017/11/09   Raspberry piのパスワードを変更
