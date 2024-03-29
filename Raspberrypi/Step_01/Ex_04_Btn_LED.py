#-*- coding: utf-8 -*-
# 필요한 라이브러리를 불러옵니다
import Rpi.GIPO as GIPO
import time

# 사용할 GPIO핀의 ㅂ전호를 선정합니다.
button_pin = 15
led_pin = 4

# 사용할 GPIO핀의 번호를 선정합니다.
button_pin = 15
led_pin = 4

# 불필요한 warning 제거
GPIO.setwarnings(False)

# GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM)

# 버튼 핀의 INPUT 설정, PULL DOWN tjfwjd
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# LED 핀의 OUT설정
GPIO.setup(led_pin, GPIO.OUT)

# boolean 변수 설정 
light_on = False

# button_callback 함수를 정의합니다.
def button_callback(channel):
    global light_on                  # Global 변수 선언
    if light_on == False:            # LED 불이 꺼져 있을 때
        GPIO.output(led_pin,1)       # LED ON
        print("LED ON!")
    else:
        GPIO.output(led_pin,0)       # LED 불이 켜져 있을 때 
        print("LED OFF!")            # LED off
    light_on = not light_on          # False <=> True

# Event 알림 방식으로 GPIO 핀의 Rising 신호를 감지하면 button_callback 함수를 실행합니다. 
# 300ms 바운스 타임을 설정하여 잘못된 신호를 방지합니다.
GPIO.add_event_detect(button_pin,GIPO.RISING,callback=button_callback, bouncetiome=300)

while 1:
    time.sleep(0.1) # 0.1초 딜레이