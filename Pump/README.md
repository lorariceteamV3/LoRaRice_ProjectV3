
# 🚰 Pump Controller (LoRaWAN)

โค้ดนี้ใช้สำหรับควบคุม **ปั๊มน้ำผ่าน LoRaWAN**  
รองรับทั้งโหมด **Auto** และ **Manual** พร้อมส่งข้อมูลเซนเซอร์กลับไปยัง ThingsBoard

---

## 📁 โครงสร้างโฟลเดอร์

```text
Pump/
└── Pump.ino
````

---

## ⚙️ ความสามารถหลัก

* 📡 ส่งข้อมูลผ่าน LoRaWAN (OTAA / ABP)
* 🌡️ อ่านค่าอุณหภูมิ + ความชื้น (BME280)
* 🔋 วัดแรงดันแบตเตอรี่
* 🚰 ควบคุมปั๊มน้ำ (Relay)
* 📥 รับคำสั่ง Downlink จาก Server
* 🔄 รองรับโหมด:

  * AUTO
  * MANUAL

---

## 📤 ข้อมูลที่ส่ง (Uplink Payload)

ข้อมูลที่ส่งขึ้น ThingsBoard:

| Byte | ข้อมูล                |
| ---- | --------------------- |
| 0-1  | Temperature (°C x100) |
| 2-3  | Humidity (% x100)     |
| 4-5  | Battery (mV)          |
| 6    | Pump Status (0/1)     |

📌 ตัวอย่างในโค้ด: 

---

## 📥 คำสั่งควบคุม (Downlink)

รูปแบบข้อมูลที่รับ:

| Byte | ค่า  | ความหมาย |
| ---- | ---- | -------- |
| 0    | 0x00 | AUTO     |
|      | 0x01 | MANUAL   |
| 1    | 0x01 | Pump ON  |
|      | 0x00 | Pump OFF |

### ตัวอย่าง

* `00 01` → Auto + เปิดปั๊ม
* `00 00` → Auto + ปิดปั๊ม
* `01 01` → Manual + เปิดปั๊ม
* `01 00` → Manual + ปิดปั๊ม

---

## 🔌 Pin ที่ใช้

| Function    | Pin |
| ----------- | --- |
| ACTIVE_PUMP | 8   |
| LED_AUTO    | 13  |
| RELAY_ON    | 16  |
| RELAY_OFF   | 33  |
| Battery ADC | 4   |

---

## 🧠 Logic การทำงาน

### AUTO Mode

* รับคำสั่งจากระบบ (เช่น RuleChain / Sensor)
* เปิด/ปิดปั๊มอัตโนมัติ

### MANUAL Mode

* ควบคุมผ่าน Dashboard (ThingsBoard)
* เปิด/ปิดปั๊มตามคำสั่งผู้ใช้

---

## ⏱️ การส่งข้อมูล

* ส่งข้อมูลทุก **15 วินาที**

```cpp
uint32_t appTxDutyCycle = 15000;
```

---

## 🌍 LoRaWAN Settings

* Region: `AS923`
* Class: `CLASS_C`
* Activation: OTAA (ค่าเริ่มต้น)

---

## ⚠️ หมายเหตุ

* ต้องตั้งค่า Device ใน ThingsBoard ให้ตรงกับ DevEUI / AppKey
* ตรวจสอบ Gateway และ Network Server ก่อนใช้งาน
* Downlink ต้องส่งมาอย่างน้อย 2 byte

---

## 🎯 วัตถุประสงค์

* 🚰 ควบคุมปั๊มน้ำระยะไกล
* 🌾 ใช้ในระบบ Smart Farming
* 📊 เชื่อมต่อกับ Dashboard และ Rule Chain

---

## 👨‍💻 ผู้พัฒนา

LoRaRice Project V3


