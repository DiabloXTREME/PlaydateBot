# Imports
import hikari
import lightbulb
import dotenv
import os
import aiohttp
from files.Steam import Steam

# ## Dependency Init
# registry_default = client.di.registry_for(lightbulb.di.Contexts.DEFAULT)
# # Registers the client session to the dependencies registry
# registry_default.register_value(typ=lightbulb.Client, value=client)
class Playdate:
    def __init__(self, steam: Steam):
        dotenv.load_dotenv()
        self.bot = hikari.GatewayBot(token=os.getenv("BOT_TOKEN"), logs="DEBUG")
        self.client = lightbulb.client_from_app(self.bot)
        self.steam = steam
        self.bot.subscribe(hikari.StartingEvent, self.start)
        self.running = False


    ## Client Init
    async def start(self, event: hikari.StartingEvent):
        await self.client.load_extensions("extensions.emoji_text_chain", "extensions.register_user")
        await self.client.start()

    ## Run
    def run(self):
        if not self.running:
            self.bot.run()
            self.running = True




pd = Playdate(Steam)
pd.run()
