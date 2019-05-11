from services import monospaceWrap


class AlwaysFalse():
    """
    Object, mocking infinite array of False
    """
    def __getitem__(self, x):
        return False


class AlwaysTrue():
    """
    Object, mocking infinite array of True
    """
    def __getitem__(self, x):
        return True


async def sendAll(ctx, text, data, format, visible=AlwaysTrue(),
                  fixed=AlwaysFalse()):
    """
    Sends entire table split into multiple messages to overcome the discord
    message length limit.
        :param ctx: Message context
        :param text: Text you want to appear before the table
        :param format: Formating function, which returns string formated
            line of desired table from provided data. If no parameters are
            provided the formating function will return tables header.
        :param visible: Array signifying, which columns should be shown
        :param fixed: Array signifying, which columns should have fixed size
    """
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
