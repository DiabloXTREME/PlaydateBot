import lightbulb
import asyncio

class ShortTextInput(lightbulb.components.Modal):
    def __init__ (self, label: str, required: bool, value: str, placeholder: str):
        if label is None:
            label= 'Text Input'


        self.text = self.add_short_text_input()