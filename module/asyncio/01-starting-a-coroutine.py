import asyncio

async def coroutine():
    print('in coroutine')

event_loop = asyncio.get_event_loop()

try:
    print('Entering event loop')
    event_loop.run_until_complete(coroutine())

finally:
    print('closing event loop')
    event_loop.close()
