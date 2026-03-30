````markdown
# 🌡️ Sensor Node (LoRaWAN)

โค้ดนี้ใช้สำหรับ **Node วัดค่าจากเซนเซอร์หลายชนิด**  
และส่งข้อมูลผ่าน **LoRaWAN ไปยัง ThingsBoard**

---

## 📁 โครงสร้างโฟลเดอร์

```text
Sensor/
└── Sensor.ino
````

---

## ⚙️ ความสามารถหลัก

* 📡 ส่งข้อมูลผ่าน LoRaWAN (OTAA / ABP)
* 🌡️ วัดอุณหภูมิ + ความชื้น (BME280)
* 📏 วัดระดับน้ำ / ระยะ (VL53L1X)
* 🔋 วัดแรงดันแบตเตอรี่
* 📍 รับพิกัด GPS (Latitude / Longitude)
* 🔌 ควบคุมการเปิด/ปิดไฟเลี้ยงเซนเซอร์ (Power Saving)

---

## 📤 ข้อมูลที่ส่ง (Uplink Payload)

Payload ขนาด **16 bytes**

| Byte  | ข้อมูล                |
| ----- | --------------------- |
| 0-1   | Temperature (°C x100) |
| 2-3   | Humidity (% x100)     |
| 4-5   | Distance (mm)         |
| 6-7   | Battery (V x10)       |
| 8-11  | Latitude (×1e6)       |
| 12-15 | Longitude (×1e6)      |

📌 ตัวอย่างการ encode: 

---

## 📏 การวัดระยะ (VL53L1X)

* ใช้ sensor VL53L1X
* คำนวณค่า:

```text
ระดับน้ำ = 500 - distance
```

* หากอ่านค่าไม่ได้:

```text
distance = -99
```

---

## 📍 GPS

* ใช้ TinyGPS++
* timeout ภายใน **60 วินาที**
* ถ้าไม่ได้พิกัด:

```text
lat = 0
lon = 0
```

---

## 🔌 Pin ที่ใช้

| Function     | Pin |
| ------------ | --- |
| VEXT Control | 21  |
| Battery ADC  | 4   |
| GPS RX       | 9   |
| GPS TX       | 10  |
| I2C SDA      | 29  |
| I2C SCL      | 31  |

---

## ⏱️ การส่งข้อมูล

* ส่งข้อมูลทุก **1 นาที**

```cpp
uint32_t appTxDutyCycle = 1 * 60 * 1000;
```

---

## 🌍 LoRaWAN Settings

* Region: `AS923`
* Class: `CLASS_A`
* Activation: OTAA
* Confirmed message: ✅ เปิดใช้งาน

---

## 🔋 Power Saving

* เปิดไฟเลี้ยงเซนเซอร์ก่อนอ่านค่า
* ปิดหลังส่งข้อมูล

```cpp
digitalWrite(PIN_VEXT_CTRL, HIGH); // ON
digitalWrite(PIN_VEXT_CTRL, LOW);  // OFF
```

---

## ⚠️ หมายเหตุ

* ต้องตั้งค่า DevEUI / AppKey ให้ตรงกับ Network Server
* GPS ต้องมีสัญญาณ (กลางแจ้งดีที่สุด)
* VL53L1X ต้องติดตั้งในตำแหน่งที่วัดระดับได้ถูกต้อง

---

## 🎯 วัตถุประสงค์

* 🌾 ใช้ในระบบ Smart Farming
* 📏 วัดระดับน้ำ / สภาพแวดล้อม
* 📡 ส่งข้อมูลขึ้น Dashboard แบบเรียลไทม์

---

## 👨‍💻 ผู้พัฒนา

LoRaRice Project V3

