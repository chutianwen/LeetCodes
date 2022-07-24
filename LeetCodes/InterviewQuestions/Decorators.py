'''
GoodRx
Decorator to limit running function multiple times in one second
'''
import time


class OneSecondLoop(object):
    def __init__(self, time_span):
        self.time_span = time_span

    def __call__(self, original_func):
        decorator_self = self

        def wrapper(*args, **kwargs):
            start = time.time()
            cnt = 0
            while time.time() - start < decorator_self.time_span:
                original_func(*args, **kwargs)
                cnt += 1
            print("Totally run function {} times".format(cnt))

        return wrapper


def crazy(time_span):
    def OneSecondLoopFunction(original_func):
        def wrapper(*args, **kwargs):
            start = time.time()
            cnt = 0
            while time.time() - start < time_span:
                original_func(*args, **kwargs)
                cnt += 1
            print("Totally run function {} times".format(cnt))
        return wrapper
    return OneSecondLoopFunction


# @OneSecondLoop(time_span=0.01)
@crazy(time_span=0.0001)
def fun(*args, **kwargs):
    pass
    # print("I am god")

fun(1, 2, 3, a='s')
