import asyncio
import aiofiles
import aiofiles.os as aios
import aiocsv
import json

result = {
    'Б/У': 0,
    'Новый': 0
}
path_files = []


async def scan_files(path):
    files_list = await aios.listdir(path)
    for file in files_list:
        if file.endswith('.csv'):
            path_files.append(f'{path}/{file}')
        else:
            new_path = f'{path}/{file}'
            await scan_files(new_path)


async def csv_handler(path, lock, semaphore):
    async with semaphore:
        async with aiofiles.open(path, 'r', encoding='windows-1251') as file:
            async for row in aiocsv.AsyncDictReader(file, delimiter=';'):
                cost = row.get('Стоимость авто')
                status = row.get('Состояние авто')
                async with lock:
                    if status == 'Б/У':
                        result['Б/У'] += int(cost)
                    elif status == 'Новый':
                        result['Новый'] += int(cost)


async def json_write(name, data):
    async with aiofiles.open(f'{name}.json', 'w') as file:
        await file.write(data)


async def main(main_folder):
    global path_files
    global result

    lock = asyncio.Lock()
    semaphore = asyncio.Semaphore(1000)
    await scan_files(main_folder)
    tasks = [
        asyncio.create_task(csv_handler(
            path=file,
            lock=lock,
            semaphore=semaphore
        ))
        for file in path_files
    ]
    await asyncio.gather(*tasks)
    result_json = json.dumps(result, indent=4, ensure_ascii=False)
    await json_write('auto_result', result_json)

asyncio.run(main('auto'))
