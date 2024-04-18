import asyncio
from aiohttp import ClientSession
from asyncio import Semaphore


async def get_data(url: str, semaphore: Semaphore):
    try:
        async with ClientSession() as session:
            async with semaphore:
                async with session.get(url) as response:
                    print(response.status)
                    return response.status
    except Exception as ex:
        print(f'Cant get status for url: {url}: {ex}')


async def main():
    semaphore = asyncio.Semaphore(100)
    tasks = [
        asyncio.create_task(
            get_data(
                url=f'https://asyncio.ru/zadachi/5/{num}.html',
                semaphore=semaphore
            )
        )
        for num in range(1, 1001)
    ]
    await asyncio.gather(*tasks)
    status_codes = [int(task.result()) for task in tasks]
    print('status_codes ', status_codes)
    print('sum status_codes ', sum(status_codes))



asyncio.run(main())
