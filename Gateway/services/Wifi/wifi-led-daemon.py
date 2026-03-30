# !/usr/bin/env python3
import time
import signal
import RPi.GPIO as GPIO

PIN = 19
mode = "off"  # off | on | blink

def set_on():
    GPIO.output(PIN, GPIO.HIGH)

def set_off():
    GPIO.output(PIN, GPIO.LOW)

def h_on(sig, frame):
    global mode
    mode = "on"

def h_off(sig, frame):
    global mode
    mode = "off"

def h_blink(sig, frame):
    global mode
    mode = "blink"

def h_exit(sig, frame):
    set_off()
    GPIO.cleanup()
    raise SystemExit(0)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT, initial=GPIO.LOW)

signal.signal(signal.SIGUSR1, h_on)     # ON
signal.signal(signal.SIGUSR2, h_off)    # OFF
signal.signal(signal.SIGALRM, h_blink)  # BLINK
signal.signal(signal.SIGTERM, h_exit)
signal.signal(signal.SIGINT, h_exit)

try:
    while True:
        if mode == "on":
            set_on()
            time.sleep(0.5)
        elif mode == "off":
            set_off()
            time.sleep(0.5)
        else:
            set_on();  time.sleep(0.2)
            set_off(); time.sleep(0.2)
except SystemExit:
    pass