import tanjun

component = tanjun.Component()


@component.with_command
@tanjun.as_slash_command("who-dis", "who is this?")
async def who_dis(ctx: tanjun.abc.Context) -> None:
    await ctx.respond("Playdate!")


@component.with_command
@tanjun.as_slash_command("banner", "banner")
async def deez(ctx: tanjun.abc.Context) -> None:
    await ctx.respond(ctx.author.avatar_url)
    await ctx.respond("That's quite ugly")


@component.with_command()
@tanjun.as_slash_command("test", "test command")
async def test(ctx: tanjun.abc.Context) -> None:
    await ctx.respond(
        f"{ctx.is_human} \n, {ctx.author} \n, {ctx.client} \n, {ctx.member} \n, {ctx.channel_id} /n, {ctx.cache} \n")


@component.with_command()
@tanjun.as_slash_command("help", "List all commands")
async def helper(ctx: tanjun.abc.Context) -> None:
    ctx.client.reload_modules()
    await ctx.respond("who-dis, test, banner, and help")





# @component.with_command()
# @tanjun.as_slash_command("poll", "makes a test poll")
# async def poll(ctx: tanjun.abc.Context) -> None:
#     await  ctx.

@tanjun.as_loader
def load(client: tanjun.Client) -> None:
    client.add_component(component)
