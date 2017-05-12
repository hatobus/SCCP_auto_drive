# SCCP_auto_drive

## 最初に

これは会津大学課題プロジェクト「自動車の自動運転」についてのレポジトリとなります．

### 使うもの

今回使用するものは主にamazonや秋月電子で購入できるものを軸に使用しています．

  - モータードライバ DRV8830 
    秋月などで購入することができます．表面実装済みですのである程度使いやすいことが特徴です．I2Cで動かすのでそれなりに知識が必要ですが慣れてしまえば
    簡単に動かすことができます．二つ使用するのでどちらかのアドレスを変更する作業をする必要があります．
    [購入](http://akizukidenshi.com/catalog/g/gK-06489/)
    [データシート](http://akizukidenshi.com/download/ds/akizuki/AE-MOTOR8830_manual.pdf)
    
  - 測距モジュール HC-SR40
    Amazonで購入，超音波型です．安いのが特徴で6個程搭載しています．これはGPIOで動くのでI2Cよりは操作がしやすいと思います．
    [購入](http://amzn.asia/jd95G4C)
    [データシート](http://akizukidenshi.com/download/ds/sainsmar/hc-sr04_ultrasonic_module_user_guidejohn_b.pdf)

  - ギアボックス ダブルギヤボックス 左右独立4速タイプ 
    amazonなどで購入することができます.左右独立なので小回りを利かせることができます．
    [購入](http://amzn.asia/8rwZjWK)
    
  - ブレッドボード * 2
  - Raspberry pi 3
  - ジャンパケーブル
 
### 言語
  Python2系統，Raspberry piにデフォルトで入っているpythonのバージョンがpython2系統のためpython2での実装になります．
  Jupyter notebookというIPython notebookのフレームワークを用い，ssh接続などをせずブラウザ上でファイルを編集することができます．
  
  元はデータ処理のフレームワークだったこともあり，のちのディープラーニングのステップでの使用を見越した利用になります．
