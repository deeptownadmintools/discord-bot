from discord.ext import commands
from services import (guildFormat, createCheckAuthor, choiceDialogue,
                      guildTableFormatFluid, guildTableChoiceFormat, sendAll)
from conf import DTAT_HOST_URL
from asyncio import TimeoutError
from datetime import datetime
import requests


help = "This command lists guild data for a guild of your choice. You can"\
    " invoke it with either !gld or !guild followed by a guild name of your"\
    " choice. You can also use the command without a guild name, in that"\
    " case, it would list all the guilds in our database, but that might"\
    " take a while, so it is advised not to do so.\n\nExample:\n"\
    "!guild deep and dirty\nYou will get to choose a guild from a list.\n"\
    "0\nUser chose a guild marked with 0.\n Server then prints a list of"\
    " columns.\n2 0 1 2 13 5\nHere user chose to order the table by column"\
    " number 2 and list columns 0, 2, 5 and 13."

brief = "!guild [guild name]   lists guild data"

usage = '[guild name]'


@commands.command(aliases=['gld'], help=help, brief=brief, usage=usage)
async def guild(ctx, *args):
    try:
        name = ' '.join(args)
        result = requests.get(DTAT_HOST_URL + '/guild/name/' + name)
        json = result.json()
        data = json['data']
        text = 'Choose a guild:\n' + guildFormat()

        data.sort(key=lambda x: x[2], reverse=True)

        id = await choiceDialogue(ctx, data, guildFormat, 20, text,
                                  createCheckAuthor(ctx))
        if id == -1:
            return
        guild_id = data[id][0]
        result = requests.get(DTAT_HOST_URL + '/guild/id/' +
                              str(guild_id) + '/data')
        json = result.json()
        data = json['players']['data']

        text = 'Choose one ID according to which you want the table to be '\
            'sorted, then choose multiple IDs to be shown as rows in your '\
            'table.\nExample: 2 2 1 5\nThis will show rows 1, 2 and 5 sorted '\
            'by row 2. You can also use -2 2 1 5, which would in turn sort '\
            'the table in descending order.'
        text += '\n' + guildTableChoiceFormat()

        msg = await choiceDialogue(ctx, json['players']['keys'],
                                   guildTableChoiceFormat, 20, text,
                                   createCheckAuthor(ctx), raw=True)
        # print(msg)
        msgParsed = msg.split(' ')
        sortCol = int(msgParsed[0])
        cols = []
        show = []

        for i in range(1, len(msgParsed)):
            try:
                c = int(msgParsed[i])
                if c >= 0 and c < len(json['players']['keys']):
                    cols.append(c)
            except ValueError:
                pass

        reverseSort=False
        if sortCol <0:
           reverseSort = True
           sortCol=sortCol*(-1)

        if sortCol == 2:
            data.sort(key=lambda x: datetime.strptime(
                x[sortCol], '%a, %d %b %Y %H:%M:%S %Z'), reverse=reverseSort)
        elif sortCol == 1:
            data.sort(key=lambda x: x[sortCol].lower(), reverse=reverseSort)
        else:
            data.sort(key=lambda x: x[sortCol], reverse=reverseSort)

        for i in range(len(json['players']['keys'])):
            if i in cols:
                show.append(True)
            else:
                show.append(False)

        text = json['name']

        await sendAll(ctx, text, data, guildTableFormatFluid, show,
                      fixed=[True, False, False, False, True, True,
                             True, True, True, True, True, True,
                             True, True, False])

    except TimeoutError:
        return
    except ValueError:
        print('Value error')
