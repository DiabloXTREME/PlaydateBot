import requests
import dotenv
import os


class Steam:
  
    def __init__(self, values=None):
        self.values = {}
        dotenv.load_dotenv()
        self.values["BOT_TOKEN"] = os.getenv("BOT_TOKEN")

        print("vals", self.values)
