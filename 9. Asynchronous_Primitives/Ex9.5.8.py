import asyncio

users = ["sasha", "petya", "masha", "katya", "dima", "olya", "igor", "sveta", "nikita", "lena",
         "vova", "yana", "kolya", "anya", "roma", "nastya", "artem", "vera", "misha", "liza"]

request_count = 0


async def handler(semaphore, name):
    global request_count
    async with semaphore:
        request_count += 1
        print(f'Пользователь {name} делает запрос')
        await asyncio.sleep(0.1)
    print(f'Запрос от пользователя {name} завершен')
    print(f'Всего запросов: {request_count}')


async def main():
    semaphore = asyncio.Semaphore(3)
    tasks = [
        asyncio.create_task(handler(semaphore, name)) for name in users
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())
