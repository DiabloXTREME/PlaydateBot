class User:
    def __init__(self, user_discord_id: int):
        self.yn = False
        if user_discord_id is None:
            print("User ID was not passed during registration!")
            return
        self.id = user_discord_id

    def agreed(self):
        self.yn = True
        return True


