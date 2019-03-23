from services import monospaceWrap


async def sendNextBatch(ctx, start, end, data, index, max, batch,
                        format, check):
    if index+batch < max:
        max = index+batch

    while index < max:
        start += '\n' + format(index, data[index])
        index += 1

    start += '\n' + end

    await ctx.send(monospaceWrap(start))

    return await ctx.bot.wait_for('message', check=check, timeout=60)
