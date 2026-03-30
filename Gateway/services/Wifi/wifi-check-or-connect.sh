# !/bin/bash

DELAY_SEC=600

UPTIME_SEC=$(cut -d. -f1 /proc/uptime)
SSID_NOW=$(iwgetid -r 2>/dev/null || true)

if [ -n "$SSID_NOW" ]; then
  echo "Connected: $SSID_NOW"
  systemctl kill -s SIGUSR1 wifi-led.service 2>/dev/null || true
  exit 0
fi

if [ "$UPTIME_SEC" -lt "$DELAY_SEC" ]; then
  echo "Not connected (idle). Uptime ${UPTIME_SEC}s < ${DELAY_SEC}s"
  systemctl kill -s SIGUSR2 wifi-led.service 2>/dev/null || true
  exit 0
fi

echo "Starting WiFi portal..."
systemctl kill -s SIGALRM wifi-led.service 2>/dev/null || true

/usr/local/bin/wifi-connect --portal-ssid "Gateway-WiFi" || true

sleep 2
SSID_NOW=$(iwgetid -r 2>/dev/null || true)

if [ -n "$SSID_NOW" ]; then
  echo "Connected after portal: $SSID_NOW"
  systemctl kill -s SIGUSR1 wifi-led.service 2>/dev/null || true
else
  echo "Still not connected after portal"
  systemctl kill -s SIGUSR2 wifi-led.service 2>/dev/null || true
  exit 1
fi