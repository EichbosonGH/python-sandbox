import asyncio
from time import time, sleep

async def asfun(x: int=1):
    await asyncio.sleep(x)
    return x

def fun(x: int=1):
    sleep(x)
    return x

def foo(x,y):
    """Abstrahiere coroutine für synchrone Funktion foo."""
    a = fun(x)
    b = asyncio.run(asfun(y))
    return a+b


async def _gather(x,y):
    return await asyncio.gather(asfun(x),asfun(y))


def goo(x,y,z):
    """Synchrone Funktion mit asynchronem Aufruf."""
    a = fun(x)
    b, c = asyncio.run(_gather(y,z))
    return a+b+c

t0 = time()
r = foo(1,2)
print("foo(1,2): ",time()-t0,r)

t0 = time()
r = goo(1,2,3)
print("goo(1,2,3): ",time()-t0,r)
