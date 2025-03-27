import hikari
import tanjun
import json
from hikari import *


def build_bot() -> GatewayBot:
    with open("../../secrets.json", "r") as file:
        secrets = json.load(file)
    bot = hikari.GatewayBot(secrets['BOT_TOKEN'])
    make_client(bot)

    return bot


def make_client(bot: hikari.GatewayBot) -> tanjun.Client:
    # client = tanjun.Client.from_gateway_bot(bot).set_type_dependency(
    #     str, "!")
    client = (tanjun.Client.from_gateway_bot(bot).load_modules("plugins.utils").declare_global_commands())
    return client
