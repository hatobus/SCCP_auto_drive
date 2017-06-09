# LV-EZ1

今回のSCCPで使用しようとしていたHC-SR04は,誤差が大きく．実際に使用するとなると，誤差の分を考えなくてはいけない．

そのため当初予定していたHC-SR04を使わず，LV-EZ1を使用するということにした．

## Data sheets

データシートは[こちら](http://maxbotix.com/documents/LV-MaxSonar-EZ_Datasheet.pdf) LV-EZシリーズ共通のデータシートになっているので，他の製品のデータを見たりすることがないように注意．

入力はシリアル通信，アナログ，PWMでデータを取得できる．Arduinoの場合はアナログ入力を利用する．今回はRaspberry piで使用し，PWMを用いてデータを取得してくる．

## 配線
配線は以下の通り，今回はPWMのピンをGPIOで制御する．

![](/img/connect.png)

PWM制御なのでPWMの部分にピンを接続．

![](/img/lvez1.jpg)

左から GND(-) VCC(+) 5.0V GPIO(ここではGPIO15) に接続する．
これで接続自体は完了する．あとはプログラムを走らせるのみ．

## プログラム

実際に行っていることとしては,前までに使用していたHC-SR04のプログラムとほぼ同じである．
GPIOのピンが一本だけになったが，これ一本でも制御が可能になる．
``` distance.py
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGECHO = 15

print "Ultrasonic Measurement"

# Set pins as output and input
GPIO.setup(GPIO_TRIGECHO,GPIO.OUT)  # Initial state as output

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGECHO, False)

def measure():
  # This function measures a distance
  # Pulse the trigger/echo line to initiate a measurement
    GPIO.output(GPIO_TRIGECHO, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGECHO, False)
  #ensure start time is set in case of very quick return
    start = time.time()

  # set line to input to check for start of echo response
    GPIO.setup(GPIO_TRIGECHO, GPIO.IN)
    while GPIO.input(GPIO_TRIGECHO)==0:
        start = time.time()

  # Wait for end of echo response
    while GPIO.input(GPIO_TRIGECHO)==1:
        stop = time.time()

    GPIO.setup(GPIO_TRIGECHO, GPIO.OUT)
    GPIO.output(GPIO_TRIGECHO, False)

    elapsed = stop-start
    distance = (elapsed * 34300)/2.0
    time.sleep(0.1)
    return distance

try:

    while True:
        distance = measure()
        print "  Distance : %.1f cm" % distance
        time.sleep(1)

except KeyboardInterrupt:
    print("Stop")
    GPIO.cleanup()
```

これを実行すると，一秒間隔で値を取得できる．HC-SR04と比べた結果，LV-EZ1のほうが信頼性が高いことが分かる．
