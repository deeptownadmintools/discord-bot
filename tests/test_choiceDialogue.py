import mock
import pytest
from services.choice_dialogue import choiceDialogue


def format(index='id', data=['id', 'name', 'number']):
    return '{:>4}) {:<32} {:>4}'.format(data[0], data[1], data[2])


class Msg():
    def __init__(self, c):
        self.content = c


class AsyncMagicMaster():
    data = ['n', 'n', 'p', 'p', '1', '1']
    i = -1

    async def async_magic2(self):
        self.i += 1
        print(self.i)
        return Msg(self.data[self.i])


@pytest.mark.asyncio
@mock.patch('services.choice_dialogue.sendNextBatch')
async def test_choiceDialogue(mNextBatch):
    async_magic_arg = 'q'

    async def async_magic():
        return Msg(async_magic_arg)

    mock.MagicMock.__await__ = lambda x: async_magic().__await__()
    ctx = mock.MagicMock()
    data = [
        [1, 'a', 1],
        [2, 'a', 1],
        [3, 'a', 1],
        [4, 'a', 1],
        [5, 'a', 1],
        [6, 'a', 1],
    ]
    text = 'text'

    assert await choiceDialogue(ctx, data, format, 2, text,
                                lambda a: True) == -1

    async_magic_arg = '1'
    assert await choiceDialogue(ctx, data, format, 2, text,
                                lambda a: True) == 1

    AMM = AsyncMagicMaster()
    mock.MagicMock.__await__ = lambda x: AMM.async_magic2().__await__()
    assert await choiceDialogue(ctx, data, format, 2, text,
                                lambda a: True, raw=True) == '1'
