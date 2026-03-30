````markdown
# 🌾 LoRaRice Project V3

ระบบ **Smart Farming** สำหรับวัดระดับน้ำและควบคุมปั๊มน้ำ  
รองรับการปลูกข้าวแบบเปียกสลับแห้ง (Alternate Wetting and Drying)

---

## 🧠 ภาพรวมระบบ

```text
Sensor Node  →  Gateway  →  ThingsBoard
      ↑                          ↓
      └────── Pump Control ──────┘
````

* 🌡️ **Sensor** → วัดค่าอุณหภูมิ ความชื้น ระดับน้ำ และ GPS
* 🚪 **Gateway** → รับข้อมูล LoRa และส่งต่อไปยัง Server
* 📊 **ThingsBoard** → แสดงผลและประมวลผล (Rule Chain)
* 🚰 **Pump** → รับคำสั่งเปิด/ปิด (Auto / Manual)

---

## 📁 โครงสร้างโปรเจกต์

```text
LoRaRice_ProjectV3/
├── Gateway/        # Raspberry Pi + LoRa Gateway + services/script
├── Pump/           # ควบคุมปั๊มน้ำผ่าน LoRaWAN
├── Sensor/         # อ่านค่าเซนเซอร์และส่งข้อมูล
└── ThingsBoard/    # Dashboard และ Rule Chain
```

---

## ⚙️ การทำงาน

1. Sensor อ่านค่า → ส่งผ่าน LoRaWAN
2. Gateway ใช้ **service** สำหรับรันระบบ และ **script** สำหรับแทนที่/จัดการอุปกรณ์ (เช่น reset gateway)
3. ThingsBoard ประมวลผลข้อมูล (Rule Chain)
4. ส่งคำสั่งกลับ → Pump ทำงาน

---

## 🚀 การใช้งาน

* ตั้งค่า Gateway และ LoRaWAN Network
* Flash โค้ดใน `Sensor/` และ `Pump/`
* Import Dashboard และ Rule Chain ใน `ThingsBoard/`
* เริ่มใช้งานระบบ 🎉

---

## 🎯 จุดประสงค์

* 🌾 ระบบเกษตรอัจฉริยะ
* 🚰 ควบคุมปั๊มน้ำระยะไกล
* 📊 Monitoring แบบเรียลไทม์

---

## 👨‍💻 ผู้พัฒนา

LoRaRice Team V3

```
```
