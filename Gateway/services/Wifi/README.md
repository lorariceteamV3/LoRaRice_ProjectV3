

```markdown
# 📶 WiFi Auto Connect + LED Status (Ready-to-use)

โปรเจกต์นี้เป็นชุดไฟล์สำเร็จรูป สำหรับ:

- ตรวจสอบ WiFi อัตโนมัติ
- เปิด WiFi portal เมื่อยังไม่เชื่อมต่อ
- แสดงสถานะผ่าน LED (GPIO19)

---

## 📁 ไฟล์ในโปรเจกต์

```

wifi-led-daemon.py
wifi-led.service
wifi-check-or-connect.sh
wifi-check-or-connect.service
wifi-check-or-connect.timer

````

> ✅ ไฟล์ทั้งหมด “พร้อมใช้งานแล้ว”  
> ❌ ไม่ต้องสร้างไฟล์ใหม่

---

## 🔌 Wiring

- GPIO19 → LED ขายาว
- GND → LED ขาสั้น (ผ่าน R)

---

## ⚙️ ขั้นตอนติดตั้ง

### 1) copy ไฟล์ไปยัง Raspberry Pi

```bash
# python
sudo cp wifi-led-daemon.py /usr/local/bin/

# shell
sudo cp wifi-check-or-connect.sh /usr/local/bin/

# service + timer
sudo cp wifi-led.service /etc/systemd/system/
sudo cp wifi-check-or-connect.service /etc/systemd/system/
sudo cp wifi-check-or-connect.timer /etc/systemd/system/
````

---

### 2) ตั้ง permission (ทำครั้งเดียว)

```bash
sudo chmod +x /usr/local/bin/wifi-led-daemon.py
sudo chmod +x /usr/local/bin/wifi-check-or-connect.sh
```

---

### 3) reload systemd

```bash
sudo systemctl daemon-reload
```

---

### 4) เปิดใช้งาน services

```bash
# LED daemon
sudo systemctl enable --now wifi-led.service

# WiFi check timer
sudo systemctl enable --now wifi-check-or-connect.timer
```

---

## 🧪 ทดสอบ

### ทดสอบ LED

```bash
sudo systemctl kill -s SIGUSR2 wifi-led.service   # OFF
sudo systemctl kill -s SIGALRM wifi-led.service   # BLINK
sudo systemctl kill -s SIGUSR1 wifi-led.service   # ON
```

---

### ทดสอบ WiFi check

```bash
sudo systemctl start wifi-check-or-connect.service
```

---

## 💡 LED Status

| สถานะ            | LED   |
| ---------------- | ----- |
| เชื่อม WiFi แล้ว | ON    |
| ยังไม่เชื่อม     | OFF   |
| เปิด portal      | BLINK |

---

## 🔁 การทำงานอัตโนมัติ

* เริ่มทำงานหลัง boot 30 วินาที
* ตรวจ WiFi ทุก 60 วินาที
* ถ้าไม่เจอ WiFi → เปิด portal (`wifi-connect`)

---

## 📌 หมายเหตุ

* ต้องติดตั้ง `wifi-connect` ก่อน
* ใช้ GPIO19 (เปลี่ยนได้ใน python)
* ใช้ systemd + timer (เสถียร)

---

## 🔧 Debug

```bash
systemctl status wifi-led.service
systemctl status wifi-check-or-connect.timer

journalctl -u wifi-led.service -n 50
journalctl -u wifi-check-or-connect.service -n 80
```

---

## 👨‍💻

LoRaRice Project V3

```


