# 📡 LoRaRice Project V3 - ThingsBoard Configuration

โปรเจกต์นี้เป็นชุดไฟล์สำหรับตั้งค่า **ThingsBoard** ของระบบ **LoRaRice Project V3**
โดยใช้สำหรับ **Import Dashboard และ Rule Chain เข้าไปใน ThingsBoard**

---

## 📁 โครงสร้างโปรเจกต์

```
ThingsBoard/
│
├── Dashboard/
│   ├── lora_admin.json
│   └── lora_user.json
│
└── RuleChain/
    ├── alarms.json
    ├── lora-pump-auto.json
    ├── lora-pump-manual.json
    ├── root_rule_chain.json
    └── signals_status.json
```

---

## ⚙️ วิธี Import เข้า ThingsBoard

### 1. Import Dashboard

ไปที่เมนู:

```
ThingsBoard → Dashboards → "+"
```

จากนั้น:

1. กด **Import dashboard**
2. อัปโหลดไฟล์ JSON จากโฟลเดอร์:

```
ThingsBoard/Dashboard/
```

ไฟล์ที่ใช้:

* lora_admin.json
* lora_user.json

---

### 2. Import Rule Chain

ไปที่เมนู:

```
ThingsBoard → Rule Chains → "+"
```

จากนั้น:

1. กด **Import rule chain**
2. อัปโหลดไฟล์ JSON จากโฟลเดอร์:

```
ThingsBoard/RuleChain/
```

📌 ลำดับการ Import ที่แนะนำ:

1. root_rule_chain.json
2. signals_status.json
3. alarms.json
4. lora-pump-auto.json
5. lora-pump-manual.json

---

## ⚠️ หมายเหตุสำคัญ

* ควร Import **Rule Chain ก่อน Dashboard**
* หลังจาก Import root_rule_chain.json แล้ว:

  * ต้องตั้งค่าให้เป็น **Root Rule Chain**
* อาจต้องสร้าง Device / Asset ใน ThingsBoard เพิ่มเอง
* ตรวจสอบการเชื่อมต่อของ Rule Chain หลัง Import

---

## 🧪 เวอร์ชันที่ทดสอบ

* ThingsBoard CE / PE (แนะนำเวอร์ชัน 3.x)

---

## 📌 วัตถุประสงค์ของโปรเจกต์

ระบบนี้ใช้สำหรับ:

* 🌾 เกษตรอัจฉริยะ (Smart Farming ด้วย LoRa)
* 🚰 ควบคุมปั๊มน้ำ (Auto / Manual)
* 🚨 ระบบแจ้งเตือน (Alarm)
* 📊 แสดงผลข้อมูลผ่าน Dashboard แบบเรียลไทม์

---

## 👨‍💻 ผู้พัฒนา

LoRaRice Team V3

