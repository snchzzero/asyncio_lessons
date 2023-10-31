import asyncio


async def print_with_delay(number):
    await asyncio.sleep(1)
    print(f'Coroutine {number} is done')


async def main():
    tasks = [await asyncio.create_task(print_with_delay(i)) for i in range(10)]

asyncio.run(main())
