import asyncio
import json

import aiofiles
import aiofiles.os as aios

result_dict = {}


def sorted_key(value):
    return int(value.split('_')[1].split('.')[0])


async def log_handler(path, lock):
    async with aiofiles.open(path, 'r') as file:
        lines = await file.readlines()
        for line in lines:
            person = line.split(' - ')[1].split(':')[0]
            message = line.split(' - ')[1].split(':')[1].lstrip().rstrip()
            async with lock:
                global result_dict
                if person not in result_dict:
                    result_dict[person] = len(message) * 0.03
                    continue
                result_dict[person] += len(message) * 0.03


async def main(directory):
    lock = asyncio.Lock()
    files = sorted(await aios.listdir(directory), key=sorted_key)
    tasks = [
        asyncio.create_task(
            log_handler(path=f'{directory}/{file_name}', lock=lock)
        ) for file_name in files
    ]
    await asyncio.gather(*tasks)

    sorted_dict = dict(sorted(result_dict.items(), key=lambda item: item[1], reverse=True))
    round_result = {
        key: f'{round(float(value), 2)}р'
        for key, value in sorted_dict.items()
    }
    result_json = json.dumps(round_result, indent=4, ensure_ascii=False)
    print('result_json ', result_json)

asyncio.run(main(directory='chat_log'))
