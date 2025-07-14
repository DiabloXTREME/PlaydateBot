import hikari
import lightbulb

class AgreementForm(lightbulb.components.Menu):
    def __init__(self):
       self.yes = self.add_interactive_button(
           hikari.ButtonStyle.SUCCESS,
           self.agree,
           label="YES"
       )
       self.no = self.add_interactive_button(
           hikari.ButtonStyle.DANGER,
           self.disagree,
           label="NO"
       )
       self.yn = None

    async def agree(self, ctx: lightbulb.components.MenuContext):
        self.yn = True
        await ctx.respond("Agreement Acknowledged", ephemeral = True)
        ctx.stop_interacting()
    async def disagree(self, ctx: lightbulb.components.MenuContext):
        self.yn = False
        await ctx.respond("Disagreement Acknowledged", ephemeral = True)
        ctx.stop_interacting()