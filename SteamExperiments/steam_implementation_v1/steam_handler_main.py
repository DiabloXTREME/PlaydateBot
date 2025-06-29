# Imports
import json
import requests
import dotenv
import os
import logging

# Setup
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger()


class Steam:

    def __init__(self):
        self.values = {}
        dotenv.load_dotenv()
        self.values["STEAM_TOKEN"] = os.getenv("STEAM_TOKEN")
        self.values["STEAM_ID"] = os.getenv("STEAM_ID")
        logger.info(f"Initializing. Values = [\n{self.values.values()}\n]\n")

    def get_user(self, user_id: int) -> json:
        """
        :param user_id:
        :return:
        """
        return requests.request(method="GET",
                                url=f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v002/?key={self.values["STEAM_TOKEN"]}&steamids={user_id}").json()


# Temp Run Command
obj = Steam()
logger.info(
    obj.get_user(int(os.getenv("STEAM_ID")))
)
