from discord.ext import commands
from services import donationsDialogue
from asyncio import TimeoutError


@commands.command(aliases=['rec'])
async def received(ctx, *args):
    try:
        await donationsDialogue(ctx, *args, sortReceived=True)
    except TimeoutError:
        return