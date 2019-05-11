def monospaceWrap(txt):
    """
    Function, which wraps provided text with '```', thus making it monospace
    formated, once displayed on Discord.
        :param txt: Text you want formated
        :returns: Text wrapped in '```'
    """
    return '```\n' + txt + '\n```'
