# Imports
import asyncio
import lightbulb
import uuid

from lightbulb.components import ModalContext

from files.Discord.utils.short_text_input import ShortTextInput


# Init
loader = lightbulb.Loader()
## Creates custom id to prevent "cross contamination" between instances
custom_id = str(uuid.uuid4())

@loader.command()
class EmojiTextChain(lightbulb.MessageCommand, name = "Emoji Text Chain"):
    # Desc for making documentation later on easier
    desc= {"name": "Emoji Text Chain",
           "Description": "Creates a chain of emojis on the selected message (*MessageCommand*) from text supplied by the user"}
    def __str__(self):
        return self.desc.__str__()
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context, client: lightbulb.client.Client):
        # Creates modal object
        text = ShortTextInput()

        # lightbulb.Context.respond_with_modal() is used to send the modal.
        await ctx.respond_with_modal("Text to emoji!", custom_id=custom_id, components = text)
        try:
            # Starts the modal. Timeout is NEEDED otherwise the resources needed to run the bot will get progressively worse
            await text.attach(client, custom_id, timeout=30)

            emoji_string = []
            for i in text.text.lower():
                emoji_string.append(f":regional_indicator_{i}:" if 97 <= ord(i) <= 122 else ":blue_square:")
            # await ctx.respond(emoji_string.__str__())
            for j in emoji_string:
                print(j)
                print(self.target.id)
                await self.target.add_reaction(j)

        except asyncio.TimeoutError:
            # Exception handling
            await ctx.respond("Unfortunately the prompt has timed out :(",  ephemeral = True)

