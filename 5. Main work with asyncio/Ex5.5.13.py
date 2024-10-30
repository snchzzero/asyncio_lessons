import asyncio
from asyncio import Future, coroutine
from collections.abc import Coroutine


async def some_task(num):
    await asyncio.sleep(1)
    print(f'Task {num} - started')
    await asyncio.sleep(1)
    result = f'Task {num} - finished'
    return result


async def get_coros_and_tasks():
        coros = []
        for i in range(10):
            if i % 2 == 0:
                coros.append(asyncio.create_task(some_task(i)))
            else:
                coros.append(some_task(i))
        print('coros ', coros)
        return coros

async def main():
    awaitables = [aw for aw in await get_coros_and_tasks()]
    results = []
    for await_object in awaitables:
        if isinstance(await_object, Coroutine):
            task = asyncio.create_task(await_object)
            await asyncio.gather(task)
            results.append(task.result())
    print(results)

asyncio.run(main())