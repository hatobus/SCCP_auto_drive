# -*- coding: utf-8 -*- 
import smbus
import time
import RPi.GPIO as GPIO
import sys


## DRV8830 Default I2C slave address
Right_ADDRESS = 0x62 # right moter
Left_ADDRESS = 0x64 # left moter

''' DRV8830 Register Addresses '''
## sample rate driver
CONTROL = 0x00

## Value motor.
FORWARD = 0x01
BACK = 0x02
STOP = 0x00

## smbus
bus = smbus.SMBus(1)

class Car():   
    flg = True

    def ard_map(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
    #mapで1-100のスケールを1-58までに対応させている．(言うなればAからBへ一対一対応)

    def __init__(self):
        pass
    
    ########################################
    #                                                                  #
    #                     Right side Motor                         #
    #                                                                  #
    ########################################
          
    # speedは1-100で指定
    def R_forward(self, speed):

        self.direction = FORWARD
        s = self.ard_map(speed, 1, 100, 1, 58)
        sval = FORWARD | ((s+5)<<2) #スピードを設定して送信するデータを1Byte作成
        bus.write_i2c_block_data(Right_ADDRESS,CONTROL,[sval]) #生成したデータを送信

    def R_stop(self):
        bus.write_i2c_block_data(Right_ADDRESS,CONTROL,[STOP]) #モータへの電力の供給を停止(惰性で動き続ける)
        
    # speedは0-100で指定
    def R_back(self, speed):
        
        self.direction = BACK
        s= self.ard_map(speed, 1, 100, 1, 58)
        sval = BACK | ((s+5)<<2) #スピードを設定して送信するデータを1Byte作成
        bus.write_i2c_block_data(Right_ADDRESS,CONTROL,[sval]) #生成したデータを送信

    def R_brake(self):
        bus.write_i2c_block_data(Right_ADDRESS,CONTROL,[0x03]) #モータをブレーキさせる
        
    
    ########################################
    #                                                                  #
    #                      Left side Motor                          #
    #                                                                  #
    ########################################
    
    # speedは1-100で指定
    def L_forward(self, speed):

        self.direction = FORWARD
        s = self.ard_map(speed, 1, 100, 1, 58)
        sval = FORWARD | ((s+5)<<2) #スピードを設定して送信するデータを1Byte作成
        bus.write_i2c_block_data(Left_ADDRESS,CONTROL,[sval]) #生成したデータを送信

    def L_stop(self):
        bus.write_i2c_block_data(Left_ADDRESS,CONTROL,[STOP]) #モータへの電力の供給を停止(惰性で動き続ける)
        
    # speedは0-100で指定
    def L_back(self, speed):
        if speed < 0:
            raise ValueError("value is under 1,  must define 1-100 as speed.")
        elif speed > 100:
            raise ValueError("value is over 100,  must define 1-100 as speed.")

        self.direction = BACK
        s= self.ard_map(speed, 1, 100, 1, 58)
        sval = BACK | ((s+5)<<2) #スピードを設定して送信するデータを1Byte作成
        bus.write_i2c_block_data(Left_ADDRESS,CONTROL,[sval]) #生成したデータを送信

    def L_brake(self):
        bus.write_i2c_block_data(Left_ADDRESS,CONTROL,[0x03]) #モータをブレーキさせる
        
     ########################################
    #                                                                  #
    #                      Both side Motor                         #
    #                                                                  #
    ########################################

    #前進
    # speedは1-100で指定
    def forward(self, speed):

        self.direction = FORWARD
        s = self.ard_map(speed, 1, 100, 1, 58)
        sval = FORWARD | ((s+5)<<2) #スピードを設定して送信するデータを1Byte作成
        bus.write_i2c_block_data(Left_ADDRESS,CONTROL,[sval]) #生成したデータを送信
        bus.write_i2c_block_data(Right_ADDRESS,CONTROL,[sval])
    #停止(ブレーキはかけない)
    def stop(self):
        bus.write_i2c_block_data(Left_ADDRESS,CONTROL,[STOP]) #モータへの電力の供給を停止(惰性で動き続ける)
        bus.write_i2c_block_data(Right_ADDRESS,CONTROL,[STOP])
    #後進
    # speedは0-100で指定
    def back(self, speed):
        if speed < 0:
            raise ValueError("value is under 1,  must define 1-100 as speed.")
        elif speed > 100:
            raise ValueError("value is over 100,  must define 1-100 as speed.")

        self.direction = BACK
        s= self.ard_map(speed, 1, 100, 1, 58)
        sval = BACK | ((s+5)<<2) #スピードを設定して送信するデータを1Byte作成
        bus.write_i2c_block_data(Left_ADDRESS,CONTROL,[sval]) #生成したデータを送信
        bus.write_i2c_block_data(Right_ADDRESS,CONTROL,[sval])
    
    #ブレーキ
    def brake(self):
        bus.write_i2c_block_data(Left_ADDRESS,CONTROL,[0x03]) #モータをブレーキさせる
        bus.write_i2c_block_data(Right_ADDRESS,CONTROL,[0x03])
    
    #左回転
    #speed -100から100までスピードを変化
    #pitch 1から10まで曲がる角度を変化
    def left(self,speed,pitch):
        if speed < -100:
            raise ValueError("value is under -100,  must define -100~100 as speed.")
        elif speed > 100:
            raise ValueError("value is over 100,  must define -100~100 as speed.")
        
        if pitch < 1:
            raise ValueError("value is under 1,  must define 1-10 as pitch.")
        elif pitch > 10:
            raise ValueError("value is over 10,  must define 1-10 as pitch.")
        
        #斜め後ろに移動
        if speed <0:
            tforward = BACK
            tback = FORWARD
            speed *= -1
        #停止
        elif speed == 0:
            bus.write_i2c_block_data(Right_ADDRESS,CONTROL,[STOP]) #生成したデータを送信
            bus.write_i2c_block_data(Left_ADDRESS,CONTROL,[STOP])
            return
        #斜め前に移動
        else:
            tforward = FORWARD
            tback = BACK
        
        self.direction = tforward
        
        s = self.ard_map(speed*(5-pitch)/5, 1, 100, 1, 58)
        #s -= (pitch) * (58/5)
        if s > 0:
            sval = tforward | ((s+5)<<2) #スピードを設定して送信するデータを1Byte作成
        elif s == 0:
            sval = STOP #スピードを設定して送信するデータを1Byte作成
        else:
            sval = tback | ((-s+5)<<2) #スピードを設定して送信するデータを1Byte作成

        bus.write_i2c_block_data(Left_ADDRESS,CONTROL,[sval]) #生成したデータを送信
        
        s = self.ard_map(speed, 1, 100, 1, 58)
        sval = tforward | ((s+5)<<2) #スピードを設定して送信するデータを1Byte作成
        bus.write_i2c_block_data(Right_ADDRESS,CONTROL,[sval])
        
    #右回転
    #speed -100から100までスピードを変化
    #pitch 1から10まで曲がる角度を変化
    def right(self,speed,pitch):
        if speed < -100:
            raise ValueError("value is under -100,  must define -100~100 as speed.")
        elif speed > 100:
            raise ValueError("value is over 100,  must define -100~100 as speed.")
        
        if pitch < 1:
            raise ValueError("value is under 1,  must define 1-10 as pitch.")
        elif pitch > 10:
            raise ValueError("value is over 10,  must define 1-10 as pitch.")
        
        #斜め後ろに移動
        if speed <0:
            tforward = BACK
            tback = FORWARD
            speed *= -1
        #停止
        elif speed == 0:
            bus.write_i2c_block_data(Right_ADDRESS,CONTROL,[STOP]) #生成したデータを送信
            bus.write_i2c_block_data(Left_ADDRESS,CONTROL,[STOP])
            return
        #斜め前に移動
        else:
            tforward = FORWARD
            tback = BACK

        self.direction = tforward
        
        s = self.ard_map(speed*(5-pitch)/5, 1, 100, 1, 58)

        #s -= (pitch) * (58/5)
        if s > 0:
            sval = tforward | ((s+5)<<2) #スピードを設定して送信するデータを1Byte作成
        elif s == 0:
            sval = STOP #スピードを設定して送信するデータを1Byte作成
        else:
            sval = tback | ((-s+5)<<2) #スピードを設定して送信するデータを1Byte作成

        bus.write_i2c_block_data(Right_ADDRESS,CONTROL,[sval]) #生成したデータを送信
        
        s = self.ard_map(speed, 1, 100, 1, 58)
        sval = tforward | ((s+5)<<2) #スピードを設定して送信するデータを1Byte作成
        bus.write_i2c_block_data(Left_ADDRESS,CONTROL,[sval])
        