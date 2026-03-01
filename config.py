# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "34008151"))
API_HASH = getenv("API_HASH", "ada4f052e9e1f5c6e300d54058165e14")
BOT_TOKEN = getenv("BOT_TOKEN", "8598049703:AAEMIXkXp9RER_ARyoOWVk1KQQ5G8rWviWA")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1913726513").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://WZMLX:WZMLX@cluster0.r9zqw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1001692422279")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1001692422279"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "")
AD_API = getenv("AD_API", "")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
