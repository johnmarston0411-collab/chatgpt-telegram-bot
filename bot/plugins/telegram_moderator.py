import os
from dotenv import load_dotenv
from typing import Dict, List
from .plugin import Plugin

from telegram import Bot
from telegram.error import TelegramError

# Load environment variables from .env file.
load_dotenv()

# Configuration values from environment variables.
BOT_TOKEN_MODERATOR = os.getenv("BOT_TOKEN_MODERATOR","")
ALLOWED_TELEGRAM_USER_IDS = list(map(int, os.getenv("ALLOWED_TELEGRAM_USER_IDS", "").split(","))) if os.getenv("ALLOWED_TELEGRAM_USER_IDS") else []
CHANNEL_ID = os.getenv("CHANNEL_ID","")

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
                "new message to the channel. Otherwise, the message is processed via a simulated external bot."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["send"],
                        "description": "The action to perform, 'send' a new message to the channel"
                    },
                    "message_text": {
                        "type": "string",
                        "description": "The full text of the Telegram message."
                    }
                },
                "required": ["action","message_text"]
            }
        }]

    async def execute(self, function_name: str, helper, **kwargs) -> Dict:
        """
        Execute the function specified by function_name.
        
        Expected kwargs:
          - message_text: str
          - chat_id: int
          - message_id: int
          - message_thread_id: int
          - from_user_id: int
        """
        # Basic configuration checks.
        if not BOT_TOKEN_MODERATOR:
            error_msg = "BOT_TOKEN is missing from environment variables."
            return {"error": error_msg}

        if not CHANNEL_ID:
            error_msg = "CHANNEL_ID is missing from environment variables."
            return {"error": error_msg}

        # Unpack required parameters.
        action = kwargs.get("action")
        message_text = kwargs.get("message_text")
        chat_id = kwargs.get("chat_id")
        message_id = kwargs.get("message_id")
        message_thread_id = kwargs.get("message_thread_id")
        from_user_id = kwargs.get("from_user_id")

        # Check if the sender is allowed.
        # if from_user_id not in ALLOWED_TELEGRAM_USER_IDS:
        #     return {"status": "ignored", "reason": "User not allowed"}

        # Initialize the Telegram Bot.
        bot = Bot(token=BOT_TOKEN_MODERATOR)

        try:
            if action=="send":
                # Send a new message to the channel.
                await bot.send_message(chat_id=CHANNEL_ID, text=message_text)
                return {"status": "success", "action": "send", "details": message_text}

            else:
                return {"status": "success", "action": "process", "details": "Invalid action provided"}

        except TelegramError as e:
            error_msg = f"Telegram error: {e}"
            return {"error": error_msg}
        except Exception as ex:
            error_msg = f"Unexpected error: {ex}"
            return {"error": error_msg}
