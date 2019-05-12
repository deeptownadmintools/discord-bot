from conf import FIRST_ENDING, DEFAULT_ENDING, LAST_ENDING, ERROR
from services import sendNextBatch, monospaceWrap


async def choiceDialogue(ctx, data, format, batchSize, text, check,
                         deleteErrorAfter=3, raw=False):
    """
    Dialogue, which allows user to list through pages of a given table, and
    to select one of its rows.
        :param ctx: Message context created by commands extension
        :param data: Array of arrays containing data you want to print
        :param format: Formating function, which returns string formated
            line of desired table from provided data. If no parameters are
            provided the formating function will return tables header.
        :param batchSize: Number of lines you want to print at once
        :param text: Introductory string, which will be printed before the
            table
        :param check: Function returning True if conditions for response are
            satisfied otherwise False. These conditions can be for example
            message provided from ctx and newly received response being sent
            by the same user.
        :param deleteErrorAfter: If zero error messages will not be deleted,
            otherwise error messages will be deleted after set amount of
            seconds.
        :param raw: If True, response will be directly returned without any
            changes to it.
        :returns: Returns -1 if user decided to abort selection. Othervise
            returns users selection.
    """
    max = len(data)
    index = 0

    while True:
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
                               delete_after=deleteErrorAfter)
                return -1

    return -1
