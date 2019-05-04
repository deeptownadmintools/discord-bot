from conf import DTAT_HOST_URL
from services import (guildFormat, createCheckAuthor, choiceDialogue,
                      timeStampFormat, donationsFormatFluid, sendAll)
import requests


async def donationsDialogue(ctx, *args, sortReceived=False):
    name = ' '.join(args)
    result = requests.get(DTAT_HOST_URL + '/data/guild/name/' + name)
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
    result = requests.get(DTAT_HOST_URL + '/data/guild/id/' +
                          str(guild_id) + '/times')
    json = result.json()
    data = json['times']['data']

    data.sort(key=lambda x: x[0], reverse=True)

    # from
    text = ('Choose a time to count from:\n' + timeStampFormat())
    data.insert(0, [-1, 'Dawn of time'])
    id1 = await choiceDialogue(ctx, data, timeStampFormat, 20, text,
                               createCheckAuthor(ctx))
    id1 = int(id1)
    if id1 == -1:
        return

    # to
    text = ('Choose a time to count to:\n' + timeStampFormat())
    data[0][1] = 'Now'
    id2 = await choiceDialogue(ctx, data, timeStampFormat, 20, text,
                               createCheckAuthor(ctx))
    id2 = int(id2)
    if id2 == -1:
        return

    if id1 == 0:
        if id2 == 0:
            result = requests.get(DTAT_HOST_URL +
                                  '/data/donations/current/guild/id/' +
                                  str(guild_id))
        else:
            result = requests.get(DTAT_HOST_URL +
                                  '/data/donations/specified/time/id/' +
                                  str(data[id2][0]))
    else:
        if id2 == 0:
            result = requests.get(DTAT_HOST_URL +
                                  '/data/donations/difference/guild/id/' +
                                  str(guild_id) +
                                  '/time/id/' +
                                  str(data[id1][0]))
        else:
            result = requests.get(DTAT_HOST_URL +
                                  '/data/donations/difference/time/id/' +
                                  str(data[id1][0]) +
                                  '/time/id/' +
                                  str(data[id2][0]))

    json = result.json()
    data = json['data']
    text = guildName + '\nFrom: ' + \
        str(json['from']) + '\nTo:  ' + \
        str(json['to'])

    if sortReceived:
        data.sort(key=lambda x: 2147483647 if x[2] == '/' else x[2], reverse=True)
    else:
        data.sort(key=lambda x: 2147483647 if x[1] == '/' else x[1], reverse=True)

    await sendAll(ctx, text, data, donationsFormatFluid)
