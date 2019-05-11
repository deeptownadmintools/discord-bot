from discord.ext import commands


@commands.command(aliases=['web'])
async def website(ctx, *args):
    await ctx.send('http://dtat.hampl.space/')
