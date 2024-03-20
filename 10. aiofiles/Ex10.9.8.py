import asyncio
import aiofiles
import aiofiles.os as aios
import aiocsv
import json

result = []

def sort_key(value):
    return value.split('log_')[1]

async def json_handler(path, lock):
    # res = json.loads(path)
    # print(res)
     with open(path, 'r', newline='') as file:
        a = json.load(file)
        # rows = await file.read()
        # a = rows.split('{')
        print(a)



        #print(rows)

        # print('--------------------------')
        # json_n = json.dumps(rows, indent=4, ensure_ascii=False)
        # print(json_n)


async def main(main_folder):
    lock = asyncio.Lock()
    files = sorted(await aios.listdir(main_folder), key=sort_key)
    # tasks = [
    #     asyncio.create_task(json_handler(f'{main_folder}/{file}', lock))
    #     for file in files
    # ]
    # await asyncio.gather(*tasks)
    await json_handler(f'{main_folder}/{files[0]}', lock)


asyncio.run(main('logs'))