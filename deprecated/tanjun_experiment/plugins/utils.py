import tanjun

nl = "\n"

component = tanjun.Component()


#
# @component.with_command
# @tanjun.as_slash_command("who", "Who are you bro")  # Fixed command name
# async def who_dis(ctx: tanjun.abc.Context) -> None:
#     print("activated")
#
#     if ctx.member:
#         user_mention = ctx.member.mention
#         user_id = ctx.member.id
#     else:
#         user_mention = "Unknown User"
#         user_id = "Unknown ID"
#
#     await ctx.respond(f"Ur {user_mention}!{nl}Ur ID is: ```{user_id}```")
#
#
# # Loader function to add the component
# @tanjun.as_loader
# def load(client: tanjun.Client) -> None:
#     client.add_component(component)

@component.with_command
@tanjun.as_slash_command("who-dis", "Whos this?")
async def who_dis(ctx: tanjun.abc.SlashContext) -> None:
    print("activated")

    if ctx.member:
        user_mention = ctx.member.mention
        user_id = ctx.member.id
    else:
        user_mention = "Unknown User"
        user_id = "Unknown ID"

    await ctx.respond(f"Ur {user_mention}!{nl}Ur ID is: ```{user_id}```")


# slash_cmd = tanjun.SlashCommand(
#     who_dis,
#     "who-dis",
#     "Who is dis?"
# )

# component.make_loader()
@tanjun.as_loader
def load(client: tanjun.Client) -> None:
    client.add_component(component)
