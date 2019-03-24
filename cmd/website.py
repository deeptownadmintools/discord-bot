from discord.ext import commands
from services import monospaceWrap


@commands.command(aliases=['web'])
async def website(ctx, *args):
    await ctx.send('http://dtat.hampl.space/')