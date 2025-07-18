import json
import os
import dotenv
from files.Steam import Steam, SteamUser


class User:
    def __init__(self, user_discord_id: int):
        self.steam_user = None
        self.yn = False
        if user_discord_id is None:
            print("User ID was not passed during registration!")
            return
        self.discord_id = user_discord_id

    def has_agreed(self):
        return self.yn

    def agreed(self):
        self.yn = True

    def steam(self, steam_user: SteamUser):
        self.steam_user = steam_user

    def get_steam(self) -> SteamUser:
        return self.steam_user

class UserTools:
    @staticmethod
    def add_user(user: User):
        users[user.discord_id] = {"agreed": user.has_agreed(), "steam": None}
    @staticmethod
    def get_user(discord_id: int) -> User:
        user = User(discord_id)
        if users[discord_id]["agreed"]:
            user.agreed()
        if users[discord_id]["steam"] != "null":
            user.steam(SteamUser.SteamUser(Steam.Steam.get_user(users[discord_id]["steam"])))
        # except:
        #     # TODO: THIS CAUSES A RECURSIVE LOOP AND NEEDS TO BE FIXED
        #     UserTools.load_users()
        #     user = UserTools.get_user(discord_id)
        return user
    @staticmethod
    def set_steam_id(discord_id: int, steam_id: int):
        users[discord_id]["steam"] = steam_id
    @staticmethod
    def save_users():
        # TODO: Replace this with databasing using MySQL
        try:
            with open("users.json", "w") as file:
                file.write(json.dumps(users))
        except IOError as e:
            raise (e, "users.json failed to write")
    @staticmethod
    def load_users():
        global users
        try:
            with open("users.json", "r") as file:
                users_temp = json.load(file)
                for i in users_temp.keys():
                    users[int(i)] = users_temp[i]

        except IOError as e:
            raise(e, "users.json failed to load")



users = {}

# # Testing
# # TODO: Move this to a testing file
# dotenv.load_dotenv()
# user_test = User(123)
# user_test.agreed()
# UserTools.add_user(user_test)
# UserTools.set_steam_id(user_test, int(os.getenv("STEAM_ID")))
# UserTools.save_users()
# users.clear()
# UserTools.load_users()
# print(users)
# print(UserTools.get_user(123).steam_user)