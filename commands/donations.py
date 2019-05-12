from discord.ext import commands
from services import donationsDialogue
from asyncio import TimeoutError


help = "This command lists donations given and received sorted by donations"\
    " given. If you want donations sorted by amount of received donations,"\
    " you can use !received."

brief = "!don [guild name]   lists donations over set period"

usage = '[guild name]'


@commands.command(aliases=['don'], help=help, brief=brief, usage=usage)
async def donations(ctx, *args):
    """
    Bot command, which returns donations over given time sorted by given
    donations.
        :param ctx: message context created by commands extension
        :param args: arguments passed after the main command
    """
    try:
        await donationsDialogue(ctx, *args, sortReceived=False)
    except TimeoutError:
        return
