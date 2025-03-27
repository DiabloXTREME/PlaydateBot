import hikari
import tanjun

component = tanjun.Component()


# Create a poll command that accepts a question and four options.
# Options without text will be skipped. Customize as needed.
@component.with_command
@tanjun.as_slash_command("poll", "Creates a GPT powered poll")
@tanjun.with_str_slash_option("option1", "First option")
@tanjun.with_str_slash_option("option2", "Second option")
async def poll(
        ctx: tanjun.abc.Context,
        question: str,
        option1: str,
        option2: str
) -> None:
    # Build a list of options (ignore empty options)
    options = [option1, option2]

    # Create buttons for each option.
    # Buttons need custom_ids that you will use later to update votes.
    buttons = []
    for index, option in enumerate(options):
        buttons.append(
            hikari.impl.MessageActionRowBuilder().add_interactive_button(
                hikari.ButtonStyle.PRIMARY,
                label=option,
                custom_id = f"poll_option_{index}"
            ).build()
        )

    # Build the poll message.
    poll_message = f"**Poll:** {question}\n"
    for index, option in enumerate(options):
        poll_message += f"\n:zero: **{index + 1}.** {option} — 0 votes"

    # Respond using an ephemeral message (or public, depending on your preference).
    # Here, we send the poll and let users vote by clicking the buttons.
    await ctx.respond(poll_message, components=buttons)


@component.with_listener(hikari.InteractionCreateEvent)
async def button_response(event: hikari.InteractionCreateEvent) -> None:
    # This listener catches all interaction events; filter for buttons by custom_id prefix.
    if not isinstance(event.interaction, hikari.ComponentInteraction):
        return

    custom_id = event.interaction.custom_id
    if not custom_id.startswith("poll_option_"):
        return

    # The following is a simple acknowledgement.
    # For a full poll you would store the user's vote and update the poll message.
    option_index = custom_id.split("_")[-1]
    await event.interaction.create_initial_response(
        hikari.ResponseType.MESSAGE_UPDATE,
        "Thanks for voting!",  # You can later edit the original poll message.
    )


@tanjun.as_loader
def load(client: tanjun.Client) -> None:
    client.add_component(component)