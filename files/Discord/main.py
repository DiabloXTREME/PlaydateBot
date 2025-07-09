# Imports
import hikari
import lightbulb
import dotenv
import os

# Init
dotenv.load_dotenv()

bot = hikari.GatewayBot(os.getenv("BOT_TOKEN"))
client = lightbulb.client_from_app(bot)


