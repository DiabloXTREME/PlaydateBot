import asyncio
import uuid
import lightbulb

from files.Discord.User import UserTools
from files.Discord.utils.short_text_input import ShortTextInput

loader = lightbulb.Loader()
id = str(uuid.uuid4())
@loader.command()
class SetSteamId(lightbulb.SlashCommand, name="set-steam-id", description="Set your Steam ID!"):
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context, client: lightbulb.Client):
        steam_id = ShortTextInput()
        await ctx.respond_with_modal(title="SteamID",custom_id=id, components=steam_id)
        try:
            await steam_id.attach(client, custom_id=id, timeout=240)
        except asyncio.TimeoutError:
            await ctx.respond("Sorry, the form timed out!", ephemeral=True)

        UserTools.load_users()
        UserTools.set_steam_id(int(ctx.user.id), int(steam_id.text))
        print(steam_id.text)
        UserTools.save_users()

