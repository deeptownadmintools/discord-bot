from discord.ext import commands
from services import donationsDialogue
from asyncio import TimeoutError


@commands.command(aliases=['don'])
async def donations(ctx, *args):
    try:
        await donationsDialogue(ctx, *args, sortReceived=False)
    except TimeoutError:
        return