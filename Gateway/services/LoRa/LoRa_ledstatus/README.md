
````markdown
# 📡 LoRa Gateway LED Status

โปรเจกต์นี้ใช้สำหรับเพิ่มสถานะ LED ให้กับ LoRa Gateway  
โดยใช้ไฟล์ `lora_pkt_fwd.c` ที่แก้ไขไว้แล้ว

---

## ⚠️ ก่อนเริ่ม

ให้ติดตั้ง WM1302 และ `sx1302_hal` ให้เรียบร้อยก่อน  
ตามคู่มือของ Seeed Studio:

https://wiki.seeedstudio.com/WM1302_module/

---

## 📁 ไฟล์ที่ใช้

ใช้ไฟล์ที่เตรียมไว้แล้วในโปรเจกต์นี้:

```bash
services/LoRa/LoRa_ledstatus/lora_pkt_fwd.c
````

> ไม่ต้องแก้โค้ดเอง
> ให้นำไฟล์นี้ไปใช้แทนไฟล์เดิมได้เลย

---

## ⚙️ ขั้นตอนใช้งาน

### 1) เข้าไปที่โฟลเดอร์ source เดิมของ packet forwarder

```bash
cd ~/sx1302_hal/packet_forwarder/src
```

---

### 2) สำรองไฟล์เดิมไว้ก่อน

```bash
cp lora_pkt_fwd.c lora_pkt_fwd.c.bak
```

---

### 3) คัดลอกไฟล์ `lora_pkt_fwd.c` ที่เตรียมไว้ ไปแทนไฟล์เดิม

ตัวอย่าง:

```bash
cp /path/to/services/LoRa/LoRa_ledstatus/lora_pkt_fwd.c ~/sx1302_hal/packet_forwarder/src/lora_pkt_fwd.c
```

> เปลี่ยน `/path/to/` ให้เป็น path จริงของโปรเจกต์คุณ

---

### 4) compile ใหม่

```bash
cd ~/sx1302_hal
make
```

---

### 5) รัน packet forwarder

```bash
cd ~/sx1302_hal/packet_forwarder
./lora_pkt_fwd
```

---

## ✅ ผลลัพธ์

เมื่อมี packet LoRa เข้ามา
LED จะแสดงสถานะตามโค้ดที่ตั้งไว้ในไฟล์ `lora_pkt_fwd.c`

---

## 📌 หมายเหตุ

* ใช้ไฟล์ `lora_pkt_fwd.c` ที่แก้ไว้แล้วในโฟลเดอร์นี้:
  `services/LoRa/LoRa_ledstatus/`
* ไม่ต้องแก้ใน `thread_up()` เอง
* ไม่ต้องเพิ่มฟังก์ชัน LED เอง
* แค่ copy ทับไฟล์เดิมแล้ว compile ใหม่

---

## 👨‍💻 ผู้พัฒนา

LoRaRice Project V3


