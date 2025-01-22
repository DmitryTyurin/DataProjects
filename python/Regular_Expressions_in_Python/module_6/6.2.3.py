# Нужно исправить код, чтобы он смог заменить O на X, o на x.

import re


def get_x(m):
    return {"o": "x", "O": "X"}[m[0]]


print(re.subn("O", get_x, input(), flags=re.I)[0])
