from discord.ext import commands


@commands.command(aliases=['web'])
async def website(ctx, *args):
    """
    Bot command, which returns url for DTAT ebsite.
        :param ctx: message context created by commands extension
        :param args: arguments passed after the main command
    """
    await ctx.send('http://dtat.hampl.space/')
