import asyncio
import aiofiles
import aiocsv
import json
import csv


class Dialect(csv.Dialect):
    delimiter = ';'
    quotechar = '"'
    lineterminator = '\n'
    quoting = csv.QUOTE_MINIMAL


async def main(file_name):
    result = []
    lock = asyncio.Lock()
    async with aiofiles.open(file_name, 'r', encoding='utf-8-sig') as file:
        async for row in aiocsv.AsyncDictReader(file, dialect=Dialect):
            print(row)
            async with lock:
                result.append(row)
    result_json = json.dumps(result, indent=4, ensure_ascii=False)
    async with aiofiles.open('result_json', 'w', encoding='utf-8') as file:
        await file.write(result_json)

asyncio.run(main('adress_1000000.csv'))
