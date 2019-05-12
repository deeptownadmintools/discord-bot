def createCheckAuthor(ctx):
    """
    Function, which creates default check for response user match.
        :param ctx: Context of the original message
        :returns: Check function, which accepts message parameter and returns
            Bool
    """
    def check(m):
        return m.author == ctx.author

    return check
