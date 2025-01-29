version: '3'
services:
  chatgpt-telegram-bot:
    build: .
    volumes:
      - .:/app
    restart: unless-stopped
    #бота
    command: ["python", "bot/main.py"]

  webhook-listener:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - .:/app
    environment:
      - SECRET_KEY=your_secret_key_here
    restart: unless-stopped
    #вебхука
    command: ["python", "webhook_listener.py"]