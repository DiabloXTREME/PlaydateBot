import asyncio

import hikari
import tanjun
import json

with open("../secrets.json", "r") as file:
    secrets = json.load(file)

bot = hikari.GatewayBot(token=secrets["BOT_TOKEN"])
# client = tanjun.Client.from_gateway_bot(bot, declare_global_commands=True)
client = tanjun.Client.from_gateway_bot(bot, set_global_commands=secrets["TEST_SERVER_ID"])


# component = tanjun.Component()
#
#
# @component.with_command
# @tanjun.as_slash_command("who-dis", "who is this?")
# async def who_dis(ctx: tanjun.abc.Context):
#     await ctx.respond("Playdate!")
#
#
# @component.with_command
# @tanjun.as_slash_command("deez-nuts", "deezzzzz")
# async def deez(ctx: tanjun.abc.Context):
#     await ctx.respond("What's Imagine Dragons you ask? \n \n IMAGINE DRAGGING DEEZ NUTS YOU IDIOT")
#
#
# client.add_component(component.copy())
# # client.add_component(component)
#


client.load_modules("plugins.utils")
# client.load_modules("plugins.gpt_poll")
bot.run()
client.reload_modules()
client.reload_modules()
client.reload_modules()
client.reload_modules()

