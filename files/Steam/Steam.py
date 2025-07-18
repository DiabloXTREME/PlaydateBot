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
dotenv.load_dotenv()
token = os.getenv("STEAM_TOKEN")


class Steam:
    # TODO: THIS NEEDS TO BE REPLACED WITH OID LIBRARY BUT I CAN'T FIND ANY THAT IS ACTUALLY EVEN THERE ON PYPI
    @staticmethod
    def get_user(user_id: int) -> json:
        """
        :param user_id:
        :return:
        """
        request =  requests.request(method="GET",
                                url=f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v002/?key={token}&steamids={user_id}").json()
        print(request)
        return request