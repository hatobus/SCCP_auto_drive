#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
from socket import *      # Import necessary modules

top = Tk()   # Create a top window
top.title('PiCar Controller')

###########################################################################
### ソケットを用いたサーバへの接続 
###########################################################################
# 注意 : クライアントとサーバが同じローカルネットワークに存在するようにする

HOST = '192.168.100.xxx' # サーバーのIPアドレスを設定 
PORT = 20000
BUFSIZ = 1024             # buffer size
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)   # ソケットの作成
tcpCliSock.connect(ADDR)                    # 上記で設定したサーバに接続する

###########################################################################
### コマンドを送信する関数を定義
###########################################################################
def forward_fun(event):
	print 'forward'
	tcpCliSock.send('forward')

def backward_fun(event):
	print 'backward'
	tcpCliSock.send('backward')

def turn_left_fun(event):
	print 'turn_left'
	tcpCliSock.send('turn_left')

def turn_right_fun(event):
	print 'turn_right'
	tcpCliSock.send('turn_right')

def shift_up(event):
	print 'shift-up'
	tcpCliSock.send('shift-up')

def shift_down(event):
	print 'shift-down'
	tcpCliSock.send('shift-down')
        
def quit_fun(event):
	top.quit()
	tcpCliSock.send('stop')
	tcpCliSock.close()

# =============================================================================
# Create buttons
# =============================================================================
Btn0 = Button(top, width=5, text='Forward')
Btn1 = Button(top, width=5, text='Backward')
Btn2 = Button(top, width=5, text='Left')
Btn3 = Button(top, width=5, text='Right')
Btn4 = Button(top, width=5, text='Quit')

# =============================================================================
# Buttons layout
# =============================================================================
Btn0.grid(row=0,column=1)
Btn1.grid(row=2,column=1)
Btn2.grid(row=1,column=0)
Btn3.grid(row=1,column=2)
Btn4.grid(row=3,column=2)

# =============================================================================
# Bind the buttons with the corresponding callback function.
# =============================================================================
Btn0.bind('<ButtonPress-1>', forward_fun)  # When button0 is pressed down, call the function forward_fun().
Btn1.bind('<ButtonPress-1>', backward_fun)
Btn2.bind('<ButtonPress-1>', turn_left_fun)
Btn3.bind('<ButtonPress-1>', turn_right_fun)
Btn4.bind('<ButtonRelease-1>', quit_fun)


# =============================================================================
# Bind buttons on the keyboard with the corresponding callback function to 
# control the car remotely with the keyboard.
# =============================================================================
top.bind('<KeyPress-Up>', shift_up)
top.bind('<KeyPress-Down>', shift_down) 
top.bind('<KeyPress-Left>', turn_left_fun)
top.bind('<KeyPress-Right>', turn_right_fun)

def main():
	top.mainloop()

if __name__ == '__main__':
	main()

