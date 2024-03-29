from flask import Flask, request
from flask import render_template
import RPi.GPIO as GPIO

app = Flask(__name__)
GPIO.setmode(GPIO.BOARD) #BOARD는 커넥터 pin번호 사용
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/led/on")
def led_on():
    try:
        GPIO.output(9, GPIO.HIGH) # Pin 번호를 9번으로 변경
        return "ok"
    except expression as indentifier:
        return "fail"

@app.route("/led/off")
def led_off():
    try:
        GPIO.output(9, GPIO.LOW)
        return "ok"
    except expression as indentifier:
        return "fail"

if __name__=="__main__":
    app.run(host="0.0.0.0")