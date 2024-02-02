import asyncio
A = 0


async def to_move(lock, robot, index):
    global A
    async with lock:
        A += 1
        print(f'Робот {robot}({index}) передвигается к месту A')
        await asyncio.sleep(0.5)
        print(f'Робот {robot}({index}) достиг места A. Место A посещено {A} раз')


async def main():
    lock = asyncio.Lock()
    robot_names = ['Электра', 'Механикс', 'Оптимус', 'Симулакр', 'Футуриус']
    tasks = [
        asyncio.create_task(to_move(lock, name, index))
        for index, name in enumerate(robot_names)
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())
