import asyncio
import aiocsv
import aiofiles
import aiofiles.os as aios

total = 0


def sorted_key(value):
    return int(value.split('.')[0])


async def csv_handler(path, lock):
    global total

    async with aiofiles.open(path, 'r') as file:
        async for row in aiocsv.AsyncReader(file):
            async with lock:
                total += int(row[0])


async def main(directory):
    global total

    lock = asyncio.Lock()
    files = sorted(await aios.listdir(directory), key=sorted_key)
    tasks = [
        asyncio.create_task(
            csv_handler(path=f'{directory}/{filename}', lock=lock)
        )
        for filename in files
    ]
    await asyncio.gather(*tasks)

    print(total)


asyncio.run(main('5000csv/5000csv'))
