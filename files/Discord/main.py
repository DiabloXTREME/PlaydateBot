# Imports
import hikari
import lightbulb
import dotenv
import os
import  aiohttp

## Extensions
import extensions.emoji_text_chain as misc

# Init
dotenv.load_dotenv()

bot = hikari.GatewayBot(os.getenv("BOT_TOKEN"), logs="DEBUG")
client = lightbulb.client_from_app(bot)

## Client Init
@bot.listen(hikari.StartingEvent)
async def start(event: hikari.StartingEvent):
    await client.load_extensions("extensions.emoji_text_chain")
    await client.start()

# ## Dependency Init
# registry_default = client.di.registry_for(lightbulb.di.Contexts.DEFAULT)
# # Registers the client session to the dependencies registry
# registry_default.register_value(typ=lightbulb.Client, value=client)

# Run
bot.run()