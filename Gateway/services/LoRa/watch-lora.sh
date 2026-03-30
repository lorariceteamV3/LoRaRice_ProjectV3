#!/usr/bin/env bash
set -euo pipefail
SERVICE="lora_pkt_fwd.service"

if ! /bin/systemctl is-active --quiet "$SERVICE"; then
  /bin/systemctl reset-failed "$SERVICE" >/dev/null 2>&1 || true
  /bin/systemctl start "$SERVICE"
  /usr/bin/logger -t watch-lora "$SERVICE restarted by cron watchdog"
fi