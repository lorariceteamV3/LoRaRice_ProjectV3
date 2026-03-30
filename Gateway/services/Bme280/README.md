
````markdown
# 🌡️ BME280 Reader Auto Start Guide

โปรเจกต์นี้ใช้สำหรับรัน `bmeread.py` บน Raspberry Pi แบบอัตโนมัติหลังเปิดเครื่อง

---

## 📦 Python Libraries ที่ต้องติดตั้ง

แนะนำให้ใช้ virtual environment:

```bash
python3 -m venv /home/loraricev3-1/venvs/bme
source /home/loraricev3-1/venvs/bme/bin/activate
````

ติดตั้ง library:

```bash
pip install requests adafruit-circuitpython-bme280
```

ติดตั้ง dependency ของ hardware:

```bash
sudo apt update
sudo apt install -y python3-pip python3-smbus i2c-tools
```

---

## ⚠️ เปิด I2C ก่อนใช้งาน

```bash
sudo raspi-config
```

ไปที่:

```
Interface Options → I2C → Enable
```

แล้ว reboot:

```bash
sudo reboot
```

---

## ⚠️ ตั้ง permission ให้ไฟล์ (ทำครั้งเดียว)

```bash
chmod +x /home/loraricev3-1/bmeread.py
```

---

## ▶️ ทดสอบรัน

```bash
/home/loraricev3-1/venvs/bme/bin/python /home/loraricev3-1/bmeread.py
```

---

## ⚙️ ตั้งให้รันอัตโนมัติ (systemd)

```bash
sudo nano /etc/systemd/system/bmeread.service
```

วาง:

```ini
[Unit]
Description=BME280 Reader
After=network-online.target

[Service]
User=loraricev3-1
WorkingDirectory=/home/loraricev3-1
ExecStart=/home/loraricev3-1/venvs/bme/bin/python /home/loraricev3-1/bmeread.py
Restart=always

[Install]
WantedBy=multi-user.target
```

จากนั้น:

```bash
sudo systemctl daemon-reload
sudo systemctl enable bmeread.service
sudo systemctl start bmeread.service
```

---

## 📌 หมายเหตุ

* ใช้ I2C address: `0x76`
* ถ้าอ่านค่าไม่ได้ ให้เช็ค:

```bash
i2cdetect -y 1
```

---

## 👨‍💻

LoRaRice Project V3

```


