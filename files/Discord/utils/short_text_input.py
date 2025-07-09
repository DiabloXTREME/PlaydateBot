import lightbulb
import asyncio

from lightbulb.components import ModalContext


class ShortTextInput(lightbulb.components.Modal):
    def __init__ (self, label: str = "Text", required: bool = False, value: str = "", placeholder: str = ""):
        super().__init__()
        self.text = self.add_short_text_input(label=label, required=required, value = value, placeholder = placeholder)

    async def on_submit(self, ctx: ModalContext):
        await ctx.respond(f"Used: {ctx.value_for(self.text)}", ephemeral = True)
        self.text = ctx.value_for(self.text)

