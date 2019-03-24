from discord.ext import commands
from services import donationsDialogue
from asyncio import TimeoutError


help = "This command lists donations given and received sorted by donations"\
    " received. If you want donations sorted by amount of given donations,"\
    " you can use !donations."

brief = "!rec [guild name]   lists donations over set period"

usage = '[guild name]'


@commands.command(aliases=['rec'], help=help, brief=brief, usage=usage)
async def received(ctx, *args):
    try:
        await donationsDialogue(ctx, *args, sortReceived=True)
    except TimeoutError:
        return
