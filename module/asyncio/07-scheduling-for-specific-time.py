import asyncio
import time

def callback(n, loop):
    print('callback {} invoked at {}'.format(n, loop.time()))

def stopper(loop):
    print('Stopperd invoked at {}'.format(loop.time()))

event_loop = asyncio.get_event_loop()
try:
    now = event_loop.time()
    print('Clock time: {}'.format(time.time()))
    print('loop time: {}'.format(now))

    print('registering callbacks')

    event_loop.call_at(now + 4, callback, 1, event_loop)
    event_loop.call_at(now + 2, callback, 2, event_loop)
    event_loop.call_at(now + 6, stopper, event_loop)
    event_loop.call_soon(callback, 3, event_loop)

    print('entering event loop')
    event_loop.run_forever()
finally:
    print('closing event loop')
    event_loop.close()
