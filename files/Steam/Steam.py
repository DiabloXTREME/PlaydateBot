# Imports
import json
import requests
import dotenv
import os
import logging

# Setup
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger()

"""
The *Steam* class is meant primarily to serve as a way to organize Steam related queries. For example, information on sales.
However, most likely, this class will **not** be carried on further into the main system. There are two scenarios in which this class still exists:
1) It is needed to be kept for things such as Addons which may require the aforementioned information like sales
2) It is needed just for the sake of organization
"""
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

    # TODO: THIS NEEDS TO BE REPLACED WITH OID LIBRARY BUT I CAN'T FIND ANY THAT IS ACTUALLY EVEN THERE ON PYPI
    # def register_new_user(self, user_disc_id: int, user_steam_int) -> bool:


