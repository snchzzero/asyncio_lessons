import asyncio
import aiofiles
import os
import glob

total = 0


async def handler(filename, lock):
    async with aiofiles.open(filename, 'r') as file:
        result = await file.read()
        async with lock:
            global total
            if int(result) % 2 == 0:
                print(result)
                total += int(result)


async def main():
    global total
    lock = asyncio.Lock()
    all_files = glob.glob(os.path.join('files_10.9.1', "*.txt"))
    tasks = [asyncio.create_task(handler(filename, lock)) for filename in all_files]
    await asyncio.gather(*tasks)
    print(total)


asyncio.run(main())
