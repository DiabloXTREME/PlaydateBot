import hikari
import asyncio
import json
import pyjokes as pj
import tanjun

# Secrets Loading
with open("../secrets.json", "r") as file:
    secrets = json.load(file)

intents = hikari.Intents.GUILD_MESSAGES | hikari.Intents.MESSAGE_CONTENT
bot = hikari.GatewayBot(token=secrets['BOT_TOKEN'], intents=intents)


@bot.listen()
async def testHello(event: hikari.GuildMessageCreateEvent) -> None:
    if not event.is_human:
        return
    # me = bot.get_me()
    if event.content is None:
        await event.message.respond(event.content)
        return
    if event.content.startswith("$!") and event.author_id in event.message.user_mentions_ids:
        await event.message.respond(f"{event.message.content}")
    elif event.content.startswith("$!") and event.message.content.find("joke 'em") != -1:
        await event.message.respond(pj.get_joke())
    elif event.content.startswith("$!"):
        await event.message.respond(f"Hello There! {event.author.display_name}")



bot.run()
