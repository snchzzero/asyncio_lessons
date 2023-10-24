import asyncio


async def my_task():
    print("Running my task")
    await asyncio.sleep(1)
    print("Task complete")


async def main():
    task = asyncio.create_task(my_task())
    await asyncio.sleep(2)

asyncio.run(main())