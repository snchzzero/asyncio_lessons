import asyncio
import random


async def waiter(future):
    await future
    print(f"future выполнен, результат {future.result()}. Корутина waiter() может продолжить работу")


async def setter(future):
    second = random.randint(1, 3)
    await asyncio.sleep(second)
    future.set_result(True)


async def main():
    future = asyncio.Future()
    task_1 = asyncio.create_task(waiter(future))
    task_2 = asyncio.create_task(setter(future))
    await asyncio.gather(task_1, task_2)

asyncio.run(main())
