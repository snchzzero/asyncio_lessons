import asyncio

# Имена пользователей
users = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eva', 'Frank', 'George', 'Helen', 'Ivan', 'Julia']

async def controller(condition, name):
    print(f'Пользователь {name} ожидает доступа к базе данных')
    async with condition:
        await condition.wait()
        print(f'Пользователь {name} подключился к БД')
        await asyncio.sleep(0.1)
        print(f'Пользователь {name} отключается от БД')
        condition.notify()

async def notify__all(condition):
    async with condition:
        condition.notify_all()

async def main():
    condition = asyncio.Condition()
    tasks = [asyncio.create_task(controller(condition, user)) for user in users]
    await asyncio.gather(*tasks, notify__all(condition))

asyncio.run(main())

