import asyncio
from time import time, sleep

async def asfun(x: int=1):
    await asyncio.sleep(x)
    return x

def fun(x: int=1):
    sleep(x)
    return x

def foo(x,y):
    a = fun(1)
    b = asyncio.run(asfun(2))
    return a+b

t0 = time()
r = foo(1,2)
print(time()-t0,r)
