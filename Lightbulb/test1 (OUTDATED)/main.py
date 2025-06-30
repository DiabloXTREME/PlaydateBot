# Bot
import hikari
import lightbulb

from typing import Optional
from hikari import Intents

# Misc
import os
import dotenv

# Auth
dotenv.load_dotenv()
bot_token = os.getenv("BOT_TOKEN")

# Setup
INTENTS = Intents.GUILD_MEMBERS | Intents.GUILDS

bot = lightbulb.BotApp(
    bot_token,
    intents=INTENTS)

# Test command
@bot.command # Declares that this is a command
@lightbulb.command("hola", description="Hola Como Estas?") # Declares the command name (what it is called by) and the description that appears
@lightbulb.implements(lightbulb.SlashCommand) # Tells that this is a SlashCommand

async def ping (ctx: lightbulb.SlashContext) -> None:
    await ctx.respond(f"HOLA!")
z
#Test command: Pinging game roles

@bot.command
@lightbulb.option("ping", "Role to ping", type = hikari.Role, required=False)
@lightbulb.option("channel", "Channel to send", type = hikari.TextableChannel, required = False)
@lightbulb.option("message", "Message", type=str)
@lightbulb.command("announcement", "Make an announcement!", pass_options = True)
@lightbulb.implements(lightbulb.SlashCommand)
async def announce(
        ctx: lightbulb.SlashContext,
        message: str,
        channel: hikari.GuildTextChannel,
        ping: Optional[hikari.Role] = None
) -> None:
    await ctx.app.rest.create_message(
        channel = channel.id,
        content = ping.mention if ping else hikari.UNDEFINED,
        role_mentions = True
    )
    await ctx.respond(
        f"Announcement posted to {channel.name}, pinging {ping.name}", flags = hikari.MessageFlag.EPHEMERAL
    )



if __name__ == "__main__":
    bot.run()