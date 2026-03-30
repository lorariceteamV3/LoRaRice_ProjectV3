
````markdown
# 🚪 Gateway

โฟลเดอร์นี้ใช้สำหรับเก็บไฟล์ที่เกี่ยวข้องกับการทำงานของ **Raspberry Pi Gateway**  
เช่น สคริปต์รีเซ็ต LoRa Gateway และ service ต่าง ๆ สำหรับเซนเซอร์, LoRa และ Wi-Fi

---

## 📁 โครงสร้างโฟลเดอร์

```text
Gateway/
├── README.md
├── reset_lgw.sh
└── services/
    ├── Bme280/
    │   ├── README.md
    │   ├── bmeread.py
    │   └── bmeread.service
    │
    ├── LoRa/
    │   ├── README.md
    │   ├── lora-packet-forwarder.service
    │   ├── watch-lora.sh
    │   └── LoRa_ledstatus/
    │       ├── README.md
    │       └── lora_pkt_fwd.c
    │
    └── Wifi/
        ├── README.md
        ├── wifi-check-or-connect.service
        ├── wifi-check-or-connect.sh
        ├── wifi-check-or-connect.timer
        ├── wifi-led-daemon.py
        └── wifi-led.service
````

---

## 🔄 reset_lgw.sh

สคริปต์นี้ใช้สำหรับ reset LoRa Gateway (SX1302 / CoreCell)
โดยใช้ GPIO ของ Raspberry Pi

> ✅ ใช้ไฟล์นี้แทน reset script เดิมของ `sx1302_hal`

---

## ⚠️ ก่อนเริ่ม

ให้ติดตั้ง WM1302 ให้เรียบร้อยก่อนตามคู่มือ:

👉 [https://wiki.seeedstudio.com/WM1302_module/](https://wiki.seeedstudio.com/WM1302_module/)

---

## ⚙️ วิธีใช้งาน

### 1) คัดลอกไฟล์ไปแทนของเดิม

ไปที่โฟลเดอร์:

```bash
cd ~/sx1302_hal/packet_forwarder
```

สำรองไฟล์เดิม:

```bash
cp reset_lgw.sh reset_lgw.sh.bak
```

คัดลอกไฟล์ใหม่เข้าไป:

```bash
cp /path/to/reset_lgw.sh ~/sx1302_hal/packet_forwarder/reset_lgw.sh
```

---

### 2) ตั้ง permission

```bash
chmod +x ~/sx1302_hal/packet_forwarder/reset_lgw.sh
```

---

### 3) ทดสอบการทำงาน

```bash
./reset_lgw.sh start
```

หรือ

```bash
./reset_lgw.sh stop
```

---

## 💡 การทำงานของสคริปต์

สคริปต์นี้ใช้สำหรับ:

* 🔁 reset SX1302
* 🔋 enable power (LDO)
* 📡 reset SX1261
* 🎛️ reset ADC

โดยควบคุมผ่าน GPIO ที่ `/sys/class/gpio`

---

## 📌 GPIO ที่ใช้

| Function     | GPIO  |
| ------------ | ----- |
| SX1302 RESET | BCM17 |
| SX1302 POWER | BCM18 |
| SX1261 RESET | BCM5  |
| ADC RESET    | BCM13 |

---

## 📝 หมายเหตุ

* ใช้กับ Raspberry Pi + WM1302
* GPIO mapping อาจต้องปรับตาม hardware
* หาก reset ไม่ทำงาน ให้ตรวจสอบ GPIO ด้วยคำสั่ง:

```bash
ls /sys/class/gpio/
```

---

## 🎯 วัตถุประสงค์

* ใช้แทน reset script เดิมของ `sx1302_hal`
* เพิ่มความเสถียรในการ start gateway
* ช่วยแก้ปัญหา gateway ไม่ทำงานหลัง boot

---

## 👨‍💻 ผู้พัฒนา

LoRaRice Project V3


