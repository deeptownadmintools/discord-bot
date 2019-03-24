def guildFormat(index='ID', data=['', 'GUILD NAME', 'LVL']):
    return '{:>4}) {:<32} {:>4}'.format(index, data[1], data[2])


def timeStampFormat(index='ID', data=['', 'TIME STAMP']):
    return '{:>4}) {:<}'.format(index, data[1])


def donationsFormat(index='ID', data=['NAME', 'DONATED', 'RECEIVED']):
    return '{:> 3}){:<32} {:>12} {:>12}'.format(index, data[0],
                                                data[1], data[2])


def donationsFormatFluid(index='ID', data=['NAME', 'DONATED', 'RECEIVED'],
                         lengths=[32, 12, 12], keys=[]):
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
        text += (' {:>' + str(5) + '}').format(data[9])
    if keys[11]:
        text += (' {:>' + str(6) + '}').format(data[9])
    if keys[12]:
        text += (' {:>' + str(6) + '}').format(data[9])
    if keys[10]:
        if lengths[10] < 8:
            lengths[10] = 8
        text += (' {:>' + str(lengths[10]) + '}').format(data[10])
    return text


def guildTableChoiceFormat(index='ID', data='KEY'):
    return'{:>3}) {:<}'.format(index, data)
