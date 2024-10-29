import asyncio

async def some_task(num):
    await asyncio.sleep(1)
    print(f'Task {num} - started')
    await asyncio.sleep(1)
    result = f'Task {num} - finished'
    return result


async def get_coros_and_tasks():
        return [asyncio.create_task(some_task(i)) for i in range(10)]


async def main():
    awaitables = [aw for aw in await get_coros_and_tasks()]
    tasks = [asyncio.ensure_future(task) for task in awaitables]
    await asyncio.gather(*tasks)
    results = [task.result() for task in tasks]
    print(f'Results ', results)
    return results


asyncio.run(main())