from discord.ext import commands
from services import guildFormat, createCheckAuthor, choiceDialogue, guildFormat, guildTableFormatFluid, guildTableChoiceFormat, sendAll
from conf import DTAT_HOST_URL
from asyncio import TimeoutError
from datetime import datetime
import requests

@commands.command(aliases=['gld'])
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
        guildName = data[id][1]
        result = requests.get(DTAT_HOST_URL + '/guild/id/' +
                              str(guild_id) + '/data')
        json = result.json()
        data = json['players']['data']

        text = 'Choose one ID according to which you want the table to be '\
            'sorted, then choose multiple IDs to be shown as rows in your '\
            'table.\nExample: 2 2 1 5\nThis will show rows 1, 2 and 5 sorted '\
            'by row 2.'
        text += '\n' + guildTableChoiceFormat()

        msg = await choiceDialogue(ctx, json['players']['keys'], guildTableChoiceFormat, 20, text,
                                   createCheckAuthor(ctx), raw=True)
        print(msg)
        msgParsed = msg.split(' ')
        sortCol = int(msgParsed[0])
        cols = []
        show = []

        for i in range(1, len(msgParsed)):
            try:
                c = int(msgParsed[i])
                if c>=0 and c< len(json['players']['keys']):
                    cols.append(c)
            except ValueError:
                pass

        if sortCol == 2:
            data.sort(key=lambda x: datetime.strptime(x[sortCol], '%a, %d %b %Y %H:%M:%S %Z'), reverse=True)
        else:
            data.sort(key=lambda x: x[sortCol], reverse=True)

        for i in range(len(json['players']['keys'])):
            if i in cols:
                show.append(True)
            else:
                show.append(False)

        text = json['name']

        await sendAll(ctx, text, data, guildTableFormatFluid, show, fixed = [True, False, False, False, True, True, True, True, True, True, True, False])

    except TimeoutError:
        return
    except ValueError:
        print('Value error')