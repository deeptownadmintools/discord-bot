import mock
import pytest
from services.sendAll import sendAll


def format(index='id',
           data=['id', 'name', 'number'],
           keys=[True, True, True],
           lengths=[1, 1, 1]):
    text = ''
    if keys[0]:
        text += (' {:>' + str(lengths[0]) + '})').format(data[0])
    if keys[1]:
        text += (' {:<' + str(lengths[1]) + '}').format(data[1])
    if keys[2]:
        text += (' {:>' + str(lengths[2]) + '}').format(data[2])
    return text


async def async_magic():
    pass


@pytest.mark.asyncio
async def test_sendAll():
    mock.MagicMock.__await__ = lambda x: async_magic().__await__()
    ctx = mock.MagicMock()
    text = 'text'
    data = [
        [111, 'abc', 1234567890],
        [1, 'abc', 12345678901234567890],
        [1, 'abcde', 1234567890],
        [1, 'abcdefgh', 1234567890],
    ]

    await sendAll(ctx, text, data, format)
    ctx.send.assert_called_with(
        """```
text
  id) name                   number
 111) abc                1234567890
   1) abc      12345678901234567890
   1) abcde              1234567890
   1) abcdefgh           1234567890
```""")

    ctx.reset_mock()
    data = [
        [111, 'abc', 1234567890],
        [1, 'abc', 12345678901234567890123456789012345678901234567890],
        [2, 'abcde', 1234567890],
        [3, 'abcdefgh', 1234567890],
        [4, 'a', 1],
        [5, 'a', 1],
        [6, 'a', 1],
        [7, 'a', 1],
        [8, 'a', 1],
        [9, 'a', 1],
        [10, 'a', 1],
        [11, 'a', 1],
        [12, 'a', 1],
        [13, 'a', 1],
        [14, 'a', 1],
        [15, 'a', 1],
        [16, 'a', 1],
        [17, 'a', 1],
        [18, 'a', 1],
        [19, 'a', 1],
        [20, 'a', 1],
        [21, 'a', 1],
        [22, 'a', 1],
        [23, 'a', 1],
        [24, 'a', 1],
        [25, 'a', 1],
        [26, 'a', 1],
        [27, 'a', 1],
        [28, 'a', 1],
        [29, 'a', 1],
        [30, 'a', 1],
        [31, 'a', 1],
        [32, 'a', 1],
    ]

    await sendAll(ctx, text, data, format)

    ctx.send.assert_any_call(
        """```
text
  id) name                                                 number
 111) abc                                              1234567890
   1) abc      12345678901234567890123456789012345678901234567890
   2) abcde                                            1234567890
   3) abcdefgh                                         1234567890
   4) a                                                         1
   5) a                                                         1
   6) a                                                         1
   7) a                                                         1
   8) a                                                         1
   9) a                                                         1
  10) a                                                         1
  11) a                                                         1
  12) a                                                         1
  13) a                                                         1
  14) a                                                         1
  15) a                                                         1
  16) a                                                         1
  17) a                                                         1
  18) a                                                         1
  19) a                                                         1
  20) a                                                         1
  21) a                                                         1
  22) a                                                         1
  23) a                                                         1
  24) a                                                         1
  25) a                                                         1
  26) a                                                         1
  27) a                                                         1
```""")

    ctx.send.assert_any_call(
        """```

  28) a                                                         1
  29) a                                                         1
  30) a                                                         1
  31) a                                                         1
  32) a                                                         1
```""")
    assert ctx.send.call_count == 2
