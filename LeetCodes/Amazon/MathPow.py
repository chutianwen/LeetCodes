
def math_pow(x, y):
    '''
    O(N) 2^(log2_N)
    :param x:
    :param y:
    :return:
    '''
    if y == 0:
        return 1
    else:
        if y % 2 == 0:
            return math_pow(x, y//2) * math_pow(x, y//2)
        else:
            return x * math_pow(x, y//2) * math_pow(x, y//2)
res = math_pow(2, 5)
# print(res)

import math
def math_pow_better(x, y):
    '''
    O(log N)
    :param x:
    :param y:
    :return:
    '''
    if y == 0:
        return 1
    else:
        if y > 0:
            y_new = y // 2
        else:
            y_new = math.ceil(y/2)

        tmp = math_pow_better(x, y_new)
        if y % 2 == 0:
            return tmp * tmp
        else:
            if y > 0:
                return x * tmp * tmp
            else:
                return tmp * tmp / x

res = math_pow_better(2, -5)
print(res)