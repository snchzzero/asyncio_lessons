import asyncio
from aiohttp import ClientSession
from bs4 import BeautifulSoup
import aiofiles
import os


def get_folder_size(folder_path):
    total_size = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
    return total_size


async def download_file(url: str, semaphore, index):
    async with semaphore:
        async with ClientSession() as session:
            async with session.get(url) as response:
                byte = await response.read()
                async with aiofiles.open(f'images/img_{index}.jpg', 'wb') as file:
                    await file.write(byte)


async def main(url):
    semaphore = asyncio.Semaphore(10)
    tasks_1000 = []

    async with ClientSession() as session:
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.read(), 'html.parser')
            main_tag = soup.find('main')
            img_tags = main_tag.find_all('img')
            for index, tag in enumerate(img_tags):
                tasks_1000.append(
                    asyncio.create_task(
                        download_file(
                            url=f'https://asyncio.ru/zadachi/4/{tag.get("src")}',
                            semaphore=semaphore,
                            index=index
                        )
                    )
                )

    await asyncio.gather(*tasks_1000)


asyncio.run(main('https://asyncio.ru/zadachi/4/index.html'))

folder_path = "images"
print(get_folder_size(folder_path))
