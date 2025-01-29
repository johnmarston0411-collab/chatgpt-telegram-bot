# Your OpenAI API key
OPENAI_API_KEY=*

# Your Telegram bot token obtained using @BotFather
TELEGRAM_BOT_TOKEN=*

# Telegram user ID of admins, or - to assign no admin
ADMIN_USER_IDS=269949384

# Comma separated list of telegram user IDs, or * to allow all
ALLOWED_TELEGRAM_USER_IDS=*


# Optional configuration, refer to the README for more details
BUDGET_PERIOD=monthly
# USER_BUDGETS=1
GUEST_BUDGET=100.0
TOKEN_PRICE=0.002
IMAGE_PRICES=0.016,0.018,0.02
TRANSCRIPTION_PRICE=0.006
VISION_TOKEN_PRICE=0.01
ENABLE_QUOTING=true
# ENABLE_IMAGE_GENERATION=true
ENABLE_TTS_GENERATION=true
ENABLE_TRANSCRIPTION=true
ENABLE_VISION=true
# PROXY=http://localhost:8080
OPENAI_MODEL=gpt-4o
# OPENAI_BASE_URL=https://example.com/v1/
ASSISTANT_PROMPT="(НАДО ОСТАВАТЬСЯ АНОНИМНОЙ! НА ВСЕ ВОПРОСЫ ПРО ТВОЮ ЛИЧНОСТЬ ОТВЕЧАЙ ГРУБО ИЛИ КИНЬ ПОДХОДЯЩУЮ КАРТИНКУ) ты – нэкора (или просто ника), это твой псевдоним. ты отвечаеш>
# SHOW_USAGE=false
# STREAM=true
# MAX_TOKENS=1200
# VISION_MAX_TOKENS=300
# MAX_HISTORY_SIZE=15
# MAX_CONVERSATION_AGE_MINUTES=180
# VOICE_REPLY_WITH_TRANSCRIPT_ONLY=true
# VOICE_REPLY_PROMPTS="Hi bot;Hey bot;Hi chat;Hey chat"
# VISION_PROMPT="What is in this image"
# N_CHOICES=1
# TEMPERATURE=1.0
# PRESENCE_PENALTY=0.0
# FREQUENCY_PENALTY=0.0
# IMAGE_MODEL=dall-e-3
# IMAGE_QUALITY=hd
# IMAGE_STYLE=natural
# IMAGE_SIZE=1024x1024
# IMAGE_FORMAT=document
# VISION_DETAIL="low"
GROUP_TRIGGER_KEYWORD="Ника"
IGNORE_GROUP_TRANSCRIPTIONS=false
IGNORE_GROUP_VISION=false
TTS_MODEL="tts-1-hd"
TTS_VOICE="nova"
# TTS_PRICES=0.015,0.030
BOT_LANGUAGE=ru
# ENABLE_VISION_FOLLOW_UP_QUESTIONS="true"
# VISION_MODEL="gpt-4o"

ENABLE_FUNCTIONS=true

# Перечислите нужные плагины через запятую
PLUGINS=weather,ddg_web_search,ddg_image_search,crypto,dice,youtube_audio_extractor,gtts_text_to_speech,auto_tts,whois,webshot,worldtimeapi

WORLDTIME_DEFAULT_TIMEZONE=Europe/Moscow
