from services import monospaceWrap


async def sendNextBatch(ctx, start, end, data, index, max, batch,
                        format, check):
    """
    Sends part of the table starting with row indexed by "index" and followe
    by next "batch" lines.
        :param ctx: Message context
        :param start: Text you want to appear before the table
        :param data: Data to be shown in a table (array of arrays)
        :param index: Row to start printing
        :param max: Number of rows in a table
        :param batch: Number of rows printed at once
        :param format: Formating function, which returns string formated
            line of desired table from provided data. If no parameters are
            provided the formating function will return tables header.
        :param check: Function returning True if conditions for response are
            satisfied otherwise False. These conditions can be for example
            message provided from ctx and newly received response being sent
            by the same user.
        :returns: -1 if user decided to abort or any positive number,
            signifying selected row
    """
    if index+batch < max:
        max = index+batch

    while index < max:
        start += '\n' + format(index, data[index])
        index += 1

    start += '\n' + end

    await ctx.send(monospaceWrap(start))

    return await ctx.bot.wait_for('message', check=check, timeout=60)
