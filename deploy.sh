#!/bin/bash

# --- Конфиг ---
TELEGRAM_BOT_TOKEN="6224650589:AAHwixFfbPVuAtpgFhze0j3Cc093Mccvggc"
TELEGRAM_CHAT_ID="1979629369"
# --------------

send_telegram() {
  local STATUS=$1
  local MESSAGE="🔄 Деплой: $STATUS\nДата: $(date +'%d.%m.%Y %H:%M:%S')"
  
  curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
    -d "chat_id=${TELEGRAM_CHAT_ID}" \
    -d "text=${MESSAGE}" \
    -d "parse_mode=Markdown"
}

# Запускаем деплой
cd /app

if git pull origin main && \
   docker compose down && \
   docker compose up --build -d
then
  send_telegram "✅ *Успешно*"
else
  send_telegram "❌ *Провал*"
  exit 1
fi