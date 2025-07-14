import asyncio
import lightbulb
from files.Discord.Playdate import Playdate
from files.Discord.utils.agreement_form import AgreementForm
from files.Discord.utils.short_text_input import ShortTextInput

loader = lightbulb.Loader()


@loader.command()
class RegisterUser(lightbulb.SlashCommand, name="register-user", description="Use this command to register yourself!"):

     @lightbulb.invoke
     async def invoke(self, ctx: lightbulb.Context, client: lightbulb.Client):
         if ctx.guild_id is None:
             await ctx.respond("Sorry! The registration command currently can only be used on servers themselves :(")
         elif Playdate.User.agreed(ctx.user.id):
             await ctx.respond("Sorry! You already registered!", ephemeral=True)
         else:
             form = AgreementForm()
             message = await ctx.respond("""
              # Welcome to **Playdate**!
              **Playdate** is a Discord bot developed and ran by *Aryaman Maheshwari*. The bot will never ask for any sort of critical or personal details for your various accounts, such as your *Steam Account*. Currently the bot only requires your *SteamID* (**NOT YOUR FRIEND CODE**). Please refer to an online tutorial if you don't know how to get that. 
              ## Your Data
              **Playdate** will never reveal your data to anybody you don't authorize, and your data is safe. By agreeing to the this form you agree to letting **Playdate** know your *SteamID* (and hence you account), which **only** lets the bot use **publicly available** information to build a profile to use for the various features of the bot. This is a one time form. However, if you wish to delete your profile, please use the `delete-account` slash command. 
              p.s: I only operate and make the bot, proper credits and everything will be added later.
             """, components=form, ephemeral=True)
             try:
                 await form.attach(client, timeout= 60)
             except asyncio.TimeoutError:
                 await ctx.edit_response(message, "Sorry, the form timed out!", components=[])
             await ctx.edit_response(message, components=[])
             agreement = form.yn
             if agreement is True:
                 await ctx.edit_response(message,"Thank you!", components=[])
                 Playdate.user.agreed(ctx.user.id)
             else:
                 await  ctx.edit_response(message, "Understood, have a good day!", components=[])
