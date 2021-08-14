# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 18:57:44 2019

@author: Arnald A. Martins
"""
from time import sleep
import cv2 
from flask import Flask, render_template, Response
import OPi.GPIO as GPIO

pinoRele = 37

GPIO.setboard(GPIO.PCPCPLUS)    # Orange Pi PC board
GPIO.setmode(GPIO.BOARD)        # set up BOARD BCM numbering
GPIO.setup(pinoRele, GPIO.OUT)         # set BCM7 (pin 26) as an output (LED)

app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/open_door', methods=['POST'])
def open_door():
    pinoRele = 37
    try:
    	GPIO.output(pinoRele, 1)       # set port/pin value to 1/HIGH/True
    	sleep(0.3)
    	GPIO.output(pinoRele, 0)       # set port/pin value to 0/LOW/False
    	sleep(0.3)
#        GPIO.cleanup()
    	return ("nothing")
    except:
    	GPIO.output(pinoRele, 0)


def gen():
    """Video streaming generator function."""
    # mudar para 1 quando no OrangePi
    cap = cv2.VideoCapture(1) 

    # Read until video is completed
    while(cap.isOpened()):
      # Capture frame-by-frame
        ret, img = cap.read()
        if ret == True:
            img = cv2.resize(img, (0,0), fx=1, fy=1) 
            frame = cv2.imencode('.jpg', img)[1].tobytes()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            sleep(0.1)
        else: 
            break

