from services import monospaceWrap


class AlwaysFalse():
    def __getitem__(self, x):
        return False


class AlwaysTrue():
    def __getitem__(self, x):
        return True


async def sendAll(ctx, text, data, format, visible=AlwaysTrue(),
                  fixed=AlwaysFalse()):
    max = []
    for i in range(len(data[0])):
        max.append(len(str(data[0][i])))

    for j in range(len(data[0])):
        if visible[j] and not fixed[j]:
            for i in range(len(data)):
                if len(str(data[i][j])) > max[j]:
                    max[j] = len(str(data[i][j]))

    text += '\n' + format(lengths=max, keys=visible)
    for i in range(len(data)):
        if len(text) > 1900:
            await ctx.send(monospaceWrap(text))
            text = ''
        text += '\n' + format(i, data[i], keys=visible, lengths=max)
    if len(text) > 0:
        await ctx.send(monospaceWrap(text))
