# DRV class
import sys
import time
import smbus

class DRV_Motor:
    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.R_Motor = 0x62
        self.L_Motor = 0x64
        self.CTR = 0x00

    def L_forward(self, speed): 
        # 左モーターの正転
        cmd = 0x01
        sval = cmd | ((speed+5)<<2)
        bus.write_i2c_block_data(self.L_Motor, self.CTR, [sval])

    def L_back(speed):
    #左モーターの逆転
        cmd = 0x02
        sval = cmd | ((speed+5)<<2)
        bus.write_i2c_block_data(self.L_Motor, self.CTR, [sval])
        
    def L_stop():
        #左モーターの停止
        bus.write_i2c_block_data(self.L_Motor, self.CTR, [self.CTR])
        
    def R_forward(speed):
        #右モーターの正転
        cmd = 0x01
        sval = cmd | ((speed+5)<<2)
        bus.write_i2c_block_data(self.R_Motor, self.CTR, [sval])
        
    def R_back(speed):
        #右モーターの逆転
        cmd = 0x02
        sval = cmd | ((speed+5)<<2)
        bus.write_i2c_block_data(self.R_Motor, self.CTR, [sval])    
        
    def R_stop():
        #右モーターのストップ
        bus.write_i2c_block_data(self.R_Motor, self.CTR, [self.CTR])
        
    def Turn_L(speed):
        #左に曲がる処理
        #右のほうがspeedが左よりも10進数で15だけ大きい
        #ちなみにspeedが15よりも小さい時はspeedの半分の速さで動く
        
        left = speed - 0xF
        if left  < 0:
            left = speed / 0x2
            
        L_forward(left)
        R_forward(speed)
        
    def Turn_R(speed):
        #右に曲がる処理
        #左のほうがspeedが左よりも10進数で15だけ大きい
        #ちなみにspeedが15よりも小さい時はspeedの半分の速さで動く
        
        right = speed - 0xF
        if right  < 0:
            right = speed / 0x2
            
        L_forward(speed)
        R_forward(right)
        
    def Turn_there(speed):
        #　その場で回転することができる．
        # できれば低速の方が好ましい
        
        L_forward(speed)
        R_back(speed)


if __name__ == "__main__":
    for i in range(0x01,0x1E,1):
        try:
            L_forward(i)
            R_forward(i)
        except:
            pass
        time.sleep(0.1)
    
    L_stop()
    R_stop()    
