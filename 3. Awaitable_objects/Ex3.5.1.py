import asyncio


async def cor1():
    print("Coroutine 1 is done")


async def cor2():
    print("Coroutine 2 is done")


async def cor3():
    print("Coroutine 3 is done")


async def main():
    task1 = asyncio.create_task(cor1())
    task2 = asyncio.create_task(cor2())
    task3 = asyncio.create_task(cor3())


asyncio.run(main())