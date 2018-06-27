# PIR sensor with LED, buzzer and Picamera (Raspberry Pi 3)

Introduction
------------
Get push notification message and image from raspberry pi using PIR motion sensor and Picamera via Pushbullet on any device.

When motion is detected , turn on the buzzer, LED(red) and capturing image. Meanwhile, sending alarm message and picture to your device.

When there is no intruder , make the green one LED light up.

Installation
------------

    pip install pushbullet.py

Requirements
-----------    
* Raspberry Pi 3
* PIR Sensor
* Buzzer
* LED*2 (red and green)
* Picamera
* Breadboard
* Jumpers

Circuit Diagram
-----------  
    
![IMGUR](https://i.imgur.com/ASNSyyS.png)

[Pushbullet](https://www.pushbullet.com/)
------------
1. Sign up an account
2. Go to [setting page](https://www.pushbullet.com/#settings) and get access token (your api key)
3. You can receive the notification on pc, add pushbullet chrome extension on browser. On your phone or tablet, you can install pushbullet app

* Python library for Pushbullet service : 
https://github.com/randomchars/pushbullet.py

* Alert message and image :

![IMGUR](https://i.imgur.com/TztrAcz.png)

Video Demo
-----------

https://www.youtube.com/watch?v=H_8BblMJKng
