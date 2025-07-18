import asyncio
import hikari

from files.Discord.User import UserTools
from files.Steam.PlaydateMaker import PlaydateMaker as PM
import lightbulb

loader = lightbulb.Loader()


class Button(lightbulb.components.Menu):
    def __init__(self):
        self.btn = self.add_interactive_button(hikari.ButtonStyle.PRIMARY, self.press, label="JOIN")
        self.reacts = []
    async def press(self, ctx: lightbulb.components.MenuContext):
        self.reacts.append(int(ctx.user.id))
        await ctx.respond("Joined!", ephemeral=True)
    def reactors(self):
        return self.reacts
@loader.command()
class PlaydateMaker(lightbulb.SlashCommand, name="playdate-maker", description="Make a Playdate!"):
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context, client: lightbulb.Client):
        button = Button()
        await ctx.respond("React to join the Playdate!", components=button)
        try:
            await button.attach(client, timeout=30)
        except asyncio.TimeoutError:
            await ctx.respond("Timed out!")
        await asyncio.sleep(20)
        people = button.reactors()
        people = list(people)
        people_users = []
        for i in people:
            people_users = UserTools.get_user(i)

        await ctx.respond(PM.make_playdate(users = people_users))




