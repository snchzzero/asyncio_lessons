import asyncio
import aiofiles.os as aios
import json
import datetime
import csv

result = []


def sort_key(value):
    return value.split('log_')[1]


async def json_handler(path):
     with open(path, 'r', newline='') as file:
        jsons_data = json.load(file)
        sorted_json_data = sorted(jsons_data, key=lambda x: x['Время и дата'])
        for data in sorted_json_data:
            if data['HTTP-статус'] == 200:
                data_time = data['Время и дата']
                iso_format = datetime.datetime.fromisoformat(data_time)
                new_data = iso_format.strftime('%d.%m.%Y %H:%M:%S')
                result.append(
                    {
                        **data,
                        'Время и дата': new_data
                    }
                )


async def write_csv(name, data):
    with open(
            file=f'{name}.csv',
            mode='w',
            encoding='utf-8-sig',
            newline=''
    ) as file:
        writer = csv.writer(
            file,
            lineterminator='\n',
            quotechar='"',
            delimiter=';',
            quoting=csv.QUOTE_MINIMAL
        )
        writer.writerow(data[0])
        for json_data in data:
            writer.writerow(json_data.values())


async def main(main_folder):
    files = sorted(await aios.listdir(main_folder), key=sort_key)
    tasks = [
        asyncio.create_task(json_handler(f'{main_folder}/{file}'))
        for file in files
    ]
    await asyncio.gather(*tasks)
    await write_csv(
        name='results_log',
        data=result,
    )


asyncio.run(main('logs'))
