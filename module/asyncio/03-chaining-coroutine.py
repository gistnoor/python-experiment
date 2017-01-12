#One coroutine can start another coroutine and wait for the results. This makes it easier to decompose a task into reusable parts
import asyncio

async def outer():
    print('in outer')
    print('waiting for result1')
    result1 = await phase1()
    print('waiting for result2')
    result2 = await phase2(result1)
    return (result1, result2)

async def phase1():
    print('in Phase1')
    return 'result1'

async def phase2(arg):
    print('in phase 2')
    return 'result2 derived from {}'.format(arg)

loop = asyncio.get_event_loop()
try:
    return_value = loop.run_until_complete(outer())
    print('return value: {!r}'.format(return_value))

finally:
    loop.close()
