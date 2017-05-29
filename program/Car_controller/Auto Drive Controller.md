# Auto Drive Controller
自動走行車が動くようになったが，これからは学習をさせていかなければならない，そのためには学習をさせなければいけない．

その時に必要なのが人間の手による走行，ラジコンを走行させ，実際にデータを取得するのが目標．距離のデータをまずは取りたいのでデータセットを作る必要がある．

jupyter notebook上から制御ができるようになるためには，jupyter notebook上でGUIを動かさなければいけない．

当初はRaspberry pi側からTkinterなどを使用したプログラムでGUI画面をjupyter notebook上に持ってこようと思ったが，デフォルトではssh接続をしながらGUIを持ってくることができなかった．そのためTkinterを使用してラジコンのコントローラーを作成できなかった．

そのため使用したのが [こちら](https://blog.dominodatalab.com/interactive-dashboards-in-jupyter/)のサイト，どうやらjupyter notebook上でHTMLなどを利用したGUIを作成できるそう．

GitHub : https://github.com/jupyter-widgets/ipywidgets

ちなみに ipywedgets のガイドはこちら http://ipywidgets.readthedocs.io/en/latest/index.html
