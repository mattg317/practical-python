import time

def time_this(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            return func(*args,**kwargs)
        finally:
            end = time.time()
            print("%s.%s : %f" % (func.__module__,func.__name__,end-start))
    return wrapper


@time_this
def countdown(n):
    while n > 0:
        n -= 1

countdown(10000000)
