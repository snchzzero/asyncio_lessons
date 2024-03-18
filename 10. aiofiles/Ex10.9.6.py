import asyncio
import aiofiles
import aiofiles.os as aios
import aiocsv
import json

result = []


async def csv_handler(path, semaphore, lock):
    global result

    async with semaphore:
        async with aiofiles.open(path, 'r', encoding='utf-8-sig') as file:
            async for row in aiocsv.AsyncDictReader(file):
                if row.get('Балл ЕГЭ') == '100':
                    async with lock:
                        result.append(row)


async def csv_write(result_json):
    async with aiofiles.open('region_student_result.json', 'w', encoding='utf-8') as file:
        await file.write(result_json)


async def main(main_folder):
    global result

    semaphore = asyncio.Semaphore(1000)
    lock = asyncio.Lock()
    folders = sorted(await aios.listdir(main_folder))
    tasks = []
    for folder in folders:
        files = await aios.listdir(f'{main_folder}/{folder}')
        for file in files:
            tasks.append(
                asyncio.create_task(
                    csv_handler(
                        path=f'{main_folder}/{folder}/{file}',
                        semaphore=semaphore,
                        lock=lock
                    )
                )
            )
    await asyncio.gather(*tasks)

    result_sort = sorted(result, key=lambda x: x['Телефон для связи'])
    result_json = json.dumps(result_sort, indent=4, ensure_ascii=False)
    await csv_write(result_json)


asyncio.run(main('region_student/Задача Студенты'))
