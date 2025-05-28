import requests
import dotenv
import os


class Steam:
    values = {}

    def __init__(self, values=None):
        dotenv.load_dotenv()
        values["API_KEY"] = os.getenv("API_KEY")
