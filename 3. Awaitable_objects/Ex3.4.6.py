# моментальное выполнение корутины

import asyncio


async def my_task(i):
    print(f"Running task {i}")
    await asyncio.sleep(1)
    print(f"Task {i} complete")


async def main():
    tasks = [asyncio.create_task(my_task(i)) for i in range(5)]


asyncio.run(main())