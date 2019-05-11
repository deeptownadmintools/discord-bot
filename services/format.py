def guildFormat(index='ID', data=['', 'GUILD NAME', 'LVL']):
    """
    Formating function, which returns a table row. If no parameters are
    given, the table header will instead be returned.
        :param index: Table row index
        :param data: Data you want to print
        :returns: Table row (String)
    """
    return '{:>4}) {:<32} {:>4}'.format(index, data[1], data[2])


def timeStampFormat(index='ID', data=['', 'TIME STAMP']):
    """
    Formating function, which returns a table row. If no parameters are
    given, the table header will instead be returned.
        :param index: Table row index
        :param data: Data you want to print
        :returns: Table row (String)
    """
    return '{:>4}) {:<}'.format(index, data[1])


def donationsFormat(index='ID', data=['NAME', 'DONATED', 'RECEIVED']):
    """
    Formating function, which returns a table row. If no parameters are
    given, the table header will instead be returned.
        :param index: Table row index
        :param data: Data you want to print
        :returns: Table row (String)
    """
    return '{:> 3}){:<32} {:>12} {:>12}'.format(index, data[0],
                                                data[1], data[2])


def donationsFormatFluid(index='ID', data=['NAME', 'DONATED', 'RECEIVED'],
                         lengths=[32, 12, 12], keys=[]):
    """
    Formating function, which returns a table row. If no parameters are
    given, the table header will instead be returned.
        :param index: Table row index
        :param data: Data you want to print
        :param lengths: Array of lengths for each column
        :param keys: Only for interface purposes
        :returns: Table row (String)
    """
    if lengths[1] < 7:
        lengths[1] = 7
    if lengths[2] < 8:
        lengths[2] = 8
    return ('{:>3})' + '{:<' + str(lengths[0]) +
            '} {:>' + str(lengths[1]) +
            '} {:>' + str(lengths[2]) +
            '}').format(index, data[0], data[1], data[2])


def guildTableFormatFluid(index='ID',
                          data=['ID', 'Name', 'Last Online', 'LVL', 'DPTH',
                                'Mine', 'ChMine', 'Oil', 'Craft', 'Smelt',
                                'Jewel', 'ChemSt', 'GreenH', 'LstEvDon'],
                          keys=[True, True, True, False, False, False,
                                False, False, False, False, False, False,
                                False, False],
                          lengths=[3, 32, 29, 3, 4, 2, 2, 2, 2, 2,
                                   2, 2, 2, 12]):
    """
    Formating function, which returns a table row. If no parameters are
    given, the table header will instead be returned.
        :param index: Table row index
        :param data: Data you want to print
        :param keys: Array, each value signifies, if associated column
            should be displayed. 
        :param lengths: Array of lengths for each column
        :returns: Table row (String)
    """
    text = ''
    if keys[0]:
        text += '{:>3})'.format(index)
    if keys[1]:
        text += (' {:<' + str(lengths[1]) + '}').format(data[1])
    if keys[2]:
        text += (' {:<' + str(lengths[2]) + '}').format(data[2])
    if keys[3]:
        text += (' {:>' + str(lengths[3]) + '}').format(data[3])
    if keys[4]:
        text += (' {:>' + str(4) + '}').format(data[4])
    if keys[5]:
        text += (' {:>' + str(4) + '}').format(data[5])
    if keys[6]:
        text += (' {:>' + str(6) + '}').format(data[6])
    if keys[7]:
        text += (' {:>' + str(3) + '}').format(data[7])
    if keys[8]:
        text += (' {:>' + str(5) + '}').format(data[8])
    if keys[9]:
        text += (' {:>' + str(5) + '}').format(data[9])
    if keys[10]:
        text += (' {:>' + str(5) + '}').format(data[10])
    if keys[11]:
        text += (' {:>' + str(6) + '}').format(data[11])
    if keys[12]:
        text += (' {:>' + str(6) + '}').format(data[12])
    if keys[13]:
        if lengths[13] < 8:
            lengths[13] = 8
        text += (' {:>' + str(lengths[13]) + '}').format(data[13])
    return text


def guildTableChoiceFormat(index='ID', data='KEY'):
    """
    Formating function, which returns a table row. If no parameters are
    given, the table header will instead be returned.
        :param index: Table row index
        :param data: Data you want to print
        :returns: Table row (String)
    """
    return'{:>3}) {:<}'.format(index, data)
