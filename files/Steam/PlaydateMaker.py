from files.Discord.User import User
class PlaydateMaker:
    @staticmethod
    def make_playdate(users: list[User]) -> dict:
        games = {}
        for i in users:
            j = i.get_steam()
            j = j.load_games()
            response = j["response"]["games"]
            for k in response:
                if games[k["name"]] is not None:
                    games[k["name"]] += 1
                else:
                    games[k["name"]] = 1
        # Found this from some reddit post or something can't remember
        sorted_games = dict(sorted(games.items()), key= lambda item: item[1], reversed = True)
        sorted_games = {game: count for game, count in sorted_games.items() if count != 1}
        return sorted_games




