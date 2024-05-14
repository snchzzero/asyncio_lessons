import aiofiles
from aiohttp import ClientSession
import asyncio
from bs4 import BeautifulSoup


async def get_data_from_url(url, semaphore):
    async with semaphore:
        async with ClientSession() as session:
            async with session.get(url) as response:
                read = await response.read()
                soup = BeautifulSoup(read)
                text = soup.find('p', id='number').text
                return int(text)


async def main(file_name):
    urls = []
    total = 0
    semaphore = asyncio.Semaphore(75)

    async with aiofiles.open(file_name) as f:
        pages = (await f.read()).split('\n')
        for page in pages:
            urls.append(f'https://asyncio.ru/zadachi/2/html/{page}.html')

    tasks = [
        asyncio.create_task(get_data_from_url(url, semaphore))
        for url in urls
    ]

    await asyncio.gather(*tasks)
    for task in tasks:
        total += task.result()
    print('total ', total)

asyncio.run(main('problem_pages.txt'))
