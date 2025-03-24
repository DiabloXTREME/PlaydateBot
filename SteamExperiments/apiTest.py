import requests
from secrets import secrets

secret = secrets.secrets
steam_token = secret["STEAM_TOKEN"]
steam_id = secret["STEAM_ID"]
print(requests.request("GET",
    f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v002/?key={steam_token}").content)
