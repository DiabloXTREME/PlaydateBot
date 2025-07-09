import lightbulb

loader = lightbulb.Loader()




@loader.command()
class EmojiTextChain(lightbulb.MessageCommand, name = "Emoji Text Chain"):
    desc= {"name": "Emoji Text Chain",
           "Description": "Creates a chain of emojis on the selected message (*MessageCommand*) from text supplied by the user"}
    def __str__(self):
        return self.desc.__str__()
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context):
        await ctx.respond("TEMPORARY")