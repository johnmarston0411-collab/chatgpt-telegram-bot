import os
from dotenv import load_dotenv
from typing import Dict, List
from .plugin import Plugin

from telegram import Bot, Update
from telegram.error import TelegramError

# Load environment variables from .env file.
load_dotenv()

# Configuration values from environment variables.
BOT_TOKEN_MODERATOR = os.getenv("BOT_TOKEN_MODERATOR", "")
CHANNEL_ID = os.getenv("CHANNEL_ID", "")
GROUP_ID = os.getenv("GROUP_ID", "")  

class TelegramModerator(Plugin):
    """
    A Telegram plugin that handles messages by either forwarding them or sending new messages
    to a specific channel based on keywords.
    """

    def get_source_name(self) -> str:
        return "TelegramModerator"

    def get_spec(self) -> List[Dict]:
        # Return the JSON schema for the handle_message function.
        return [{
            "name": "telegram_moderator",
            "description": (
                "Handles a Telegram message. If the message starts with 'forward it :', the message is "
                "forwarded to a designated channel. If it starts with 'send it :', the text is sent as a "
                "new message to the channel. If it starts with 'get recent', the bot retrieves recent messages."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["send", "get_recent"],
                        "description": "The action to perform, 'send' a new message to the channel or 'get_recent' to retrieve recent messages"
                    },
                    "message_text": {
                        "type": "string",
                        "description": "The full text of the Telegram message."
                    }
                },
                "required": ["action"]
            }
        }]

    async def execute(self, function_name: str, helper, **kwargs) -> Dict:
        """
        Execute the function specified by function_name.
        
        Expected kwargs:
          - message_text: str
          - chat_id: int
          - message_id: int
          - message_thread_id: int (optional; may be provided in the update)
          - from_user_id: int
        """
        # Basic configuration checks.
        if not BOT_TOKEN_MODERATOR:
            return {"error": "BOT_TOKEN is missing from environment variables."}

        if not CHANNEL_ID:
            return {"error": "CHANNEL_ID is missing from environment variables."}

        if not GROUP_ID:
            return {"error": "GROUP_ID is missing from environment variables."}

        # Unpack required parameters.
        action = kwargs.get("action")
        message_text = kwargs.get("message_text")

        # Initialize the Telegram Bot.
        bot = Bot(token=BOT_TOKEN_MODERATOR)

        try:
            if action == "send":
                # Send a new message to the channel.
                await bot.send_message(chat_id=CHANNEL_ID, text=message_text)
                return {"status": "success", "action": "send", "details": message_text}

            elif action == "get_recent":
                # Retrieve pending updates from the bot.
                updates = await bot.get_updates(offset=0, timeout=10)
                messages = []
                for idx, update in enumerate(updates, start=1):
                    if update.message :
                        text = update.message.text or "No text"
                        thread_id = getattr(update.message, "message_thread_id", None)
                        chat_id = update.message.chat.id
                        messages.append(f"Text: {text}, Thread ID: {thread_id}, Chat ID: {chat_id}")
                # Return the details of the last 10 messages.
                result = "\n".join(messages[-10:])
                return {"status": "success", "action": "get_recent", "details": result}

            else:
                return {"status": "success", "action": "process", "details": "Invalid action provided"}

        except TelegramError as e:
            return {"error": f"Telegram error: {e}"}
        except Exception as ex:
            return {"error": f"Unexpected error: {ex}"}