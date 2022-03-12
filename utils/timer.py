import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)
        end_time = time.time()
        print("{} run time: {};".format(func.__name__, end_time - start_time), "Ans: {}".format(value))
        return value
    return wrapper
