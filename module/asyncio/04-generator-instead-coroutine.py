#Python 3.5 introduced new language features to define such coroutines natively using async def and to yield control using await, and the examples for asyncio take advantage of the new feature. Earlier versions of Python 3 can use generator functions wrapped with the asyncio.coroutine() decorator and yield from to achieve the same effect.
import asyncio

@asyncio.coroutine
def outer():
    print('in outer')
    print('waiting for result1')
    result1 = yield from phase1()
    print('waiting for result2')
    result2 = yield from phase2(result1)
    return (result1, result2)

@asyncio.coroutine
def phase1():
    print('in phase1')
    return 'result1'

@asyncio.coroutine
def phase2(arg):
    print('in phase2')
    return 'result2 derived from {}'.format(arg)

loop = asyncio.get_event_loop()
try:
    return_value = loop.run_until_complete(outer())
    print('return values: {}'.format(return_value))
finally:
    loop.close()
