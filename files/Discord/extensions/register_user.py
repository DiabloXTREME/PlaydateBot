import asyncio

import lightbulb

from files.Discord.utils.agreement_form import AgreementForm

loader = lightbulb.Loader()

@loader.command()
class RegisterUser(lightbulb.SlashCommand, name="register_user", description="Use this command to register yourself!"):

     @lightbulb.invoke
     async def invoke(self, ctx: lightbulb.Context, client: lightbulb.Client):
         form = AgreementForm()
         message = await ctx.respond("""
          # Welcome to **Playdate**!
          **Playdate** is a Discord bot developed and ran by *Aryaman Maheshwari*. The bot will never ask for any sort of critical or personal details for your various accounts, such as your *Steam Account*. Currently the bot only requires your *SteamID* (**NOT YOUR FRIEND CODE**). Please refer to an online tutorial if you don't know how to get that. 
          ## Your Data
          **Playdate** will never reveal your data to anybody you don't authorize, and your data is safe. By agreeing to the this form you agree to letting **Playdate** know your *SteamID* (and hence you account), which **only** lets the bot use **publicly available** information to build a profile to use for the various features of the bot. This is a one time form. However, if you wish to delete your profile, please use the `delete-account` slash command. 
         
         """, components=form, ephemeral=True)
         try:
             await form.attach(client, wait = True, timeout= 60)
         except asyncio.TimeoutError:
             await ctx.edit_response(message, "Sorry, the form timed out!", components=[])
         agreement = form.yn
         if agreement is True:
             await self.add_user(ctx, client, message)
         else:
             await  ctx.edit_response(message, "Understood, have a good day!", components=[])
    # This function is just here mostly for clarity
     async def add_user(self,ctx, client, message):
        await ctx.respond(ctx.user.id)