import mock
import pytest
from services.sendNextBatch import sendNextBatch


def format(index='id', data=['id', 'name', 'number']):
    return '{:>4}) {:<32} {:>4}'.format(data[0], data[1], data[2])


async def async_magic():
    pass


@pytest.mark.asyncio
async def test_sendNextBatch():
    mock.MagicMock.__await__ = lambda x: async_magic().__await__()
    ctx = mock.MagicMock()
    start = 'text1'
    end = 'text2'
    data = [
        [1, 'abcde', 1234567890],
        [2, 'a', 1234567890],
        [3, 'a', 1234567890],
        [4, 'a', 1234567890],
        [5, 'a', 1234567890],
        [6, 'a', 1234567890],
    ]
    max = len(data)

    await sendNextBatch(ctx, start, end, data, 0, max, 2, format,
                        lambda a: True)
    ctx.send.assert_called_with(
        """```
text1
   1) abcde                            1234567890
   2) a                                1234567890
text2
```""")

    ctx.reset_mock()

    await sendNextBatch(ctx, start, end, data, 2, max, 4, format,
                        lambda a: True)
    ctx.send.assert_called_with(
        """```
text1
   3) a                                1234567890
   4) a                                1234567890
   5) a                                1234567890
   6) a                                1234567890
text2
```""")
