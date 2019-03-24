from conf import FIRST_ENDING, DEFAULT_ENDING, LAST_ENDING, ERROR
from services import sendNextBatch, monospaceWrap


async def choiceDialogue(ctx, data, format, batchSize, text, check,
                         deleteErronAfter=3, raw=False):
    max = len(data)
    index = 0
    errEncountered = False

    while True:
        # if errEncountered:
        #     msg = await ctx.bot.wait_for('message', check=check)
        #     errEncountered = False
        # else:
        if index > max-batchSize:
            msg = await sendNextBatch(ctx, text, LAST_ENDING, data,
                                        index, max, batchSize, format,
                                        check)
        elif index == 0:
            msg = await sendNextBatch(ctx, text, FIRST_ENDING, data,
                                        index, max, batchSize, format,
                                        check)
        else:
            msg = await sendNextBatch(ctx, text, DEFAULT_ENDING, data,
                                        index, max, batchSize, format,
                                        check)

        if msg.content == 'n':
            if index < max-batchSize:
                index += batchSize
        elif msg.content == 'p':
            if index >= batchSize:
                index -= batchSize
        elif msg.content == 'q':
            return -1
        else:
            if raw:
                return msg.content
            try:
                return int(msg.content)
            except ValueError:
                await ctx.send(monospaceWrap(ERROR),
                               delete_after=deleteErronAfter)
                return
                # errEncountered = True

    return -1
