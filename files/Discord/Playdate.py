# Imports
import hikari
import lightbulb
import dotenv
import os

from files.Discord.User import UserTools
from files.Steam import Steam, SteamUser


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
        await self.client.load_extensions("extensions.register_user", "extensions.set_steam_id", "extensions.playdate_maker")
        print("Init")
        # DO NOT EVER UNCOMMENT UNTIL THE ENTIRE SYSTEM IS FIXED. IN WHICH CASE DELETE THIS ANYWAYS AHHHHHHHH
        UserTools.load_users()
        await self.client.start()

    ## Run
    def run(self):
        if not self.running:
            self.bot.run()
            self.running = True


pd = Playdate(Steam)
pd.run()
