import Rpi.GPIO as GPIO
import time

led_pin = 4

GPIO.setwarnings(False)

GPIO.setwarnings(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT)

for i in range(10):
    GPIO.output(led_pin,l)
    time.sleep(1)

    GPIO.output(led_pin, 0)
    time.sleep(1)
GPIO.cleanup()