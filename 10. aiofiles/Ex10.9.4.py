import asyncio
import aiofiles
import aiofiles.os as aios
import aiocsv


def sorted_key(value):
    return int(value.split('_')[1])


async def csv_handler(path, lock):
    async with aiofiles.open(path, 'r') as file:
        async for row in aiocsv.AsyncReader(file):
            async with lock:
                return int(row[0])


async def main(main_folder):
    total = 0
    lock = asyncio.Lock()
    folders = sorted(await aios.listdir(main_folder), key=sorted_key)
    tasks = []
    for folder in folders:
        files = await aios.listdir(f'{main_folder}/{folder}')
        for file in files:
            tasks.append(
                asyncio.create_task(csv_handler(
                    path=f'{main_folder}/{folder}/{file}',
                    lock=lock
                ))
            )
    await asyncio.gather(*tasks)
    for task in tasks:
        total += task.result()
    print('total ', total)


asyncio.run(main('5000folder/5000folder'))
