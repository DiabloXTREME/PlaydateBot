import logging
import os
import json

import requests

from . import Steam

# Setup
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger()

"""
The **User** class is core to the entire project. It will be the accessor and modifier of all user related data (which is planned to eventually be stored encrypted on MySQL).
This class includes things such as the generation of game lists and other user stats, which may either be incorporated in or incorporate other more specialized classes (such as a potential **PlaydateGenerator** class)
"""
class SteamUser:
    def __init__(self, user_data: json):
        print(user_data)
        self.user_data = user_data["response"]["players"]
        print(self.user_data)
        # print(type(self.user_data))
        self.id = self.user_data["steamid"]
        self.name = self.user_data["personaname"]
        self.profile = self.user_data["profileurl"]
        self.avatar_small = self.user_data["avatar"]
        self.avatar_big = self.user_data["avatarfull"]
        self.games = requests.request(method="GET", url=f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={os.getenv("STEAM_TOKEN")}&steamid={self.id}&include_appinfo=true&include_played_free_games=true").json()
    def __str__(self):
        return f"User: {self.name} ({self.id}, games: \n {self.games} \n"
    def load_games(self):
        return self.games
