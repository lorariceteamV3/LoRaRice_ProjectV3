#!/home/loraricev3-1/venvs/bme/bin/python
import time
import math
import random
import requests
import board
from adafruit_bme280 import basic as adafruit_bme280

i2c = board.I2C()
bme = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)

TB_HOST = "https://tboard.ngrok.app"
TB_TOKEN = "wF5IMyIONJV9AjXnoc5S"

INTERVAL_SEC = 5 * 60
start = time.time()

def send_mock():
    t = time.time() - start

    temp = bme.temperature
    humid = bme.humidity

    payload = {
        "temperature": round(temp, 2),
        "humidity": round(humid, 2),
    }

    url = f"{TB_HOST}/api/v1/{TB_TOKEN}/telemetry"
    r = requests.post(url, json=payload, timeout=5)
    print("POST", r.status_code, payload)

if __name__ == "__main__":
    print("Mock gw_temp/gw_humid -> ThingBoard started")
    while True:
        try:
            send_mock()
        except Exception as e:
            print("Error:", e)
        time.sleep(INTERVAL_SEC)