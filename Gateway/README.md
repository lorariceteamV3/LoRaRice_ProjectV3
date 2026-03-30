ได้ครับ อันนี้ README สำหรับ `reset_lgw.sh` แบบสั้น กระชับ และชัดว่า “ใช้แทนของเดิม” 👇

---

```markdown
# 🔄 SX1302 Reset Script (WM1302 Gateway)

สคริปต์นี้ใช้สำหรับ reset LoRa Gateway (SX1302 / CoreCell)  
โดยใช้ GPIO ของ Raspberry Pi

---

## ⚠️ ก่อนเริ่ม

ให้ติดตั้ง WM1302 ให้เรียบร้อยก่อนตามคู่มือ:

👉 https://wiki.seeedstudio.com/WM1302_module/

---

## 📁 ไฟล์ที่ใช้

```

reset_lgw.sh

````

> ✅ ใช้ไฟล์นี้ **แทน reset script เดิม** ของ `sx1302_hal`

---

## ⚙️ วิธีใช้งาน

### 1) copy ไฟล์ไปแทนของเดิม

ไปที่โฟลเดอร์:

```bash
cd ~/sx1302_hal/packet_forwarder
````

สำรองไฟล์เดิม:

```bash
cp reset_lgw.sh reset_lgw.sh.bak
```

คัดลอกไฟล์ใหม่เข้าไป:

```bash
cp /path/to/reset_lgw.sh ~/sx1302_hal/packet_forwarder/reset_lgw.sh
```

---

### 2) ตั้ง permission (ทำครั้งเดียว)

```bash
chmod +x ~/sx1302_hal/packet_forwarder/reset_lgw.sh
```

---

### 3) ทดสอบ reset

```bash
./reset_lgw.sh start
```

หรือ:

```bash
./reset_lgw.sh stop
```

---

## 💡 การทำงานของสคริปต์

สคริปต์นี้จะ:

* reset SX1302 (LoRa chip)
* enable power (LDO)
* reset SX1261 (LBT / Spectral scan)
* reset ADC (AD5338R)

โดยใช้ GPIO ผ่าน `/sys/class/gpio`

---

## 📌 GPIO ที่ใช้

| Function     | GPIO  |
| ------------ | ----- |
| SX1302 RESET | BCM17 |
| SX1302 POWER | BCM18 |
| SX1261 RESET | BCM5  |
| ADC RESET    | BCM13 |

---

## ⚠️ หมายเหตุ

* ใช้กับ Raspberry Pi + WM1302 เท่านั้น
* GPIO mapping อาจต้องปรับตาม hardware
* ถ้า reset ไม่ทำงาน ให้เช็ค:

```bash
ls /sys/class/gpio/
```

---

## 🎯 วัตถุประสงค์

* ใช้แทน reset script เดิมที่มากับ sx1302_hal
* เพิ่มความเสถียรในการ start gateway
* แก้ปัญหา gateway ไม่ขึ้นหลัง boot

---

## 👨‍💻

LoRaRice Project V3


