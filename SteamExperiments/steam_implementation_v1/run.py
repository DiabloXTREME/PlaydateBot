from Steam import Steam
import logging
import os
import dotenv
from SteamExperiments.steam_implementation_v1.User import User

# Setup
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger()

# Testing Variables
dotenv.load_dotenv()
steam_id = os.getenv("STEAM_ID")


obj = Steam()

logger.info(
    obj.get_user(int(steam_id))
)
user = User(obj.get_user(int(steam_id)))
logger.info(user)