import asyncio

async def coroutine_1(delay=0.1):
    await asyncio.sleep(0.11)  # Первая задержка --
    print("Второе сообщение от корутины 1")
    await asyncio.sleep(0.01)  # Первая задержка --
    print("Первое сообщение от корутины 1")
    await asyncio.sleep(0.05)  # Вторая задержка
    print("Четвертое сообщение от корутины 1")
    await asyncio.sleep(0.2)  # Третья задержка
    print("Третье сообщение от корутины 1")

async def coroutine_2(delay=0.1):
    await asyncio.sleep(0.1)  # Первая задержка
    print("Третье сообщение от корутины 2")
    await asyncio.sleep(0.09)  # Первая задержка
    print("Четвертое сообщение от корутины 2")
    await asyncio.sleep(0.03)  # Вторая задержка --
    print("Первое сообщение от корутины 2")
    await asyncio.sleep(0.09)  # Третья задержка --
    print("Второе сообщение от корутины 2")


async def coroutine_3(delay=0.1):
    await asyncio.sleep(0.1)  # Первая задержка
    print("Третье сообщение от корутины 3")
    await asyncio.sleep(delay)  # Первая задержка
    print("Четвертое сообщение от корутины 3")
    await asyncio.sleep(0.05)  # Вторая задержка  --
    print("Первое сообщение от корутины 3")
    await asyncio.sleep(0.07)  # Третья задержка  --
    print("Второе сообщение от корутины 3")

async def main():
    await asyncio.gather(
        coroutine_1(),
        coroutine_2(),
        coroutine_3(),
    )

asyncio.run(main())