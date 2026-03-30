

# 📡 LoRa Packet Forwarder Setup

คู่มือนี้ใช้สำหรับตั้งค่า `lora_pkt_fwd.service` ให้รันอัตโนมัติ และมี watchdog คอยตรวจสอบ ถ้าหยุดจะเริ่มใหม่ให้อัตโนมัติ

---

## 📁 ไฟล์ที่ใช้

- `/etc/systemd/system/lora_pkt_fwd.service`
- `/usr/local/bin/watch-lora.sh`
- `/etc/cron.d/watch-lora`

---

## ⚙️ ขั้นตอนติดตั้ง

### 1) สร้าง service

```bash
sudo nano /etc/systemd/system/lora_pkt_fwd.service
````

วาง:

```ini
[Unit]
Description=LoRa Packet Forwarder
Wants=network-online.target
After=network-online.target

[Service]
WorkingDirectory=/home/loraricev3-1/sx1302_hal/packet_forwarder
ExecStart=/home/loraricev3-1/sx1302_hal/packet_forwarder/lora_pkt_fwd -c AS923
Restart=always
RestartSec=10
User=loraricev3-1

[Install]
WantedBy=multi-user.target
```

---

### 2) reload และ enable service

```bash
sudo systemctl daemon-reload
sudo systemctl enable lora_pkt_fwd.service
```

> ถ้ามี service นี้อยู่แล้ว ให้ใช้แค่ `daemon-reload`

---

### 3) start service

```bash
sudo systemctl start lora_pkt_fwd.service
```

### 4) ตรวจสอบสถานะ

```bash
sudo systemctl status lora_pkt_fwd.service
```

---

## 🔁 ตั้ง Watchdog

### 5) สร้างสคริปต์ watchdog

```bash
sudo nano /usr/local/bin/watch-lora.sh
```

วาง:

```bash
#!/usr/bin/env bash
set -euo pipefail
SERVICE="lora_pkt_fwd.service"

if ! /bin/systemctl is-active --quiet "$SERVICE"; then
  /bin/systemctl reset-failed "$SERVICE" >/dev/null 2>&1 || true
  /bin/systemctl start "$SERVICE"
  /usr/bin/logger -t watch-lora "$SERVICE restarted by cron watchdog"
fi
```

จากนั้น:

```bash
sudo chmod +x /usr/local/bin/watch-lora.sh
```

---

### 6) ตั้ง cron ให้ตรวจทุก 1 นาที

```bash
sudo nano /etc/cron.d/watch-lora
```

วาง:

```cron
*/1 * * * * root /usr/local/bin/watch-lora.sh
```

แล้วรัน:

```bash
sudo chmod 644 /etc/cron.d/watch-lora
sudo systemctl reload cron || sudo service cron reload
```

---

## ✅ คำสั่งที่ใช้บ่อย

```bash
sudo systemctl start lora_pkt_fwd.service
sudo systemctl stop lora_pkt_fwd.service
sudo systemctl restart lora_pkt_fwd.service
sudo systemctl status lora_pkt_fwd.service
journalctl -u lora_pkt_fwd.service -f
```

---

## 📌 หมายเหตุ

* ชื่อ service ต้องตรงกันทุกจุด: `lora_pkt_fwd.service`
* ตรวจสอบ path ของ `lora_pkt_fwd` ให้ถูกต้อง
* ตรวจสอบ user `loraricev3-1` ให้มีสิทธิ์ใช้งานไฟล์

---

## 👨‍💻 ผู้พัฒนา

LoRaRice Project V3

