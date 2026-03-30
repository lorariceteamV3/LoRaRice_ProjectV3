
# 🌾 LoRaRice Project V3

ระบบ **Smart Farming** สำหรับวัดระดับน้ำและควบคุมปั๊มน้ำ  
รองรับการปลูกข้าวแบบเปียกสลับแห้ง (Alternate Wetting and Drying)

---

## 🧠 ภาพรวมระบบ

```

Sensor Node  →  Gateway  →  ThingsBoard
↑                          ↓
└────── Pump Control ──────┘

```

- 🌡️ **Sensor** → วัดอุณหภูมิ ความชื้น ระดับน้ำ และ GPS  
- 🚪 **Gateway** → รับข้อมูล LoRa และส่งต่อไปยัง Server  
- 📊 **ThingsBoard** → แสดงผลและประมวลผล (Rule Chain)  
- 🚰 **Pump** → รับคำสั่งเปิด/ปิด (Auto / Manual)  

---

## 📁 โครงสร้างโปรเจกต์

```

LoRaRice_ProjectV3/
├── Gateway/
├── Pump/
├── Sensor/
└── ThingsBoard/

```

---

## ⚙️ การทำงาน

1. 🌡️ Sensor อ่านค่า → ส่งผ่าน LoRaWAN  
2. 🚪 Gateway ใช้ service และ script จัดการระบบ  
3. 📊 ThingsBoard ประมวลผลข้อมูล  
4. 🚰 Pump รับคำสั่งและทำงาน  

---

## 🎯 จุดประสงค์

- 🌾 ระบบเกษตรอัจฉริยะ  
- 🚰 ควบคุมปั๊มน้ำระยะไกล  
- 📊 Monitoring แบบเรียลไทม์  

---

## 👨‍💻 ผู้พัฒนา

LoRaRice Team V3

