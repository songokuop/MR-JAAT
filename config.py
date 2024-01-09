import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "25443947"))
API_HASH = environ.get("API_HASH", "ab4cd800dac7c9a36314ee83800adba8")
BOT_TOKEN = environ.get("BOT_TOKEN", "6764106664:AAE-L9vaJltK2Q-30xonGBauWOHFK_YcCEM")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1001957898674"))
ADMINS = int(environ.get("ADMINS", "6013614984"))
DB_URI = environ.get("DB_URI", "mongodb+srv://haroonhassan2:haroonhassan2@haroonhassan2.z3j6yxu.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "haroonhassan2")
OPENAI_API = environ.get("OPENAI_API", "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")
AI = is_enabled((environ.get("AI","True")), False)
