import hikari
import lightbulb
import dotenv
import os

dotenv.load_dotenv()

# Creates the base Hikari bot. logs="DEBUG" gives FAR more information
bot = hikari.GatewayBot(os.getenv("BOT_TOKEN"), logs="DEBUG")

# Creates the Lightbulb client, which as far as I understand, basically acts as an extra wrapper for Hikari
client = lightbulb.client_from_app(bot)

# This makes sure that the bot actually starts when Hikari starts. Basically, when the Hikari bot gets a "StartingEvent" this also starts the Lightbulb wrapper
# NOTE: Find more about .bot.subscribe
bot.subscribe(hikari.StartingEvent, client.start)

# Registers that this is a command/something that needs to be looked out for. Maybe use a similar system for addons instead of jsons?
@client.register()
# The below code sets the type (there are three UserCommand, MessageCommand, and SlashCommand), the name of the command, and under what description it is put
class Hello(lightbulb.SlashCommand, name = "hello", description="Wishes you a good day!"):
    # This defines the "invocation" method of the command, which as far as I can tell, is the "init" of the command. It MUST take in the context as the second parameter (has context about the message
    @lightbulb.invoke
    # Takes in the context and defines an asynchronous function (basically waits for things to happen before starting or finishing)
    async def invoke(self,ctx: lightbulb.Context)-> None:
        # Responds using ctx.respond() which is needed for, well, responding.
        await ctx.respond(f"How is it going {ctx.user}!")


bot.run()