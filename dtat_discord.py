from conf import TOKEN, PREFIX
from cmd import donations, received, guild, website
from discord.ext.commands import Bot


# create bot and set prefix for commands
bot = Bot(command_prefix=PREFIX)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# register commands
bot.add_command(donations)
bot.add_command(received)
bot.add_command(guild)
bot.add_command(website)


bot.run(TOKEN, bot=True, reconnect=True)
