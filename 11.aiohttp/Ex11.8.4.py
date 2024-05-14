import asyncio
from aiohttp import ClientSession
from bs4 import BeautifulSoup


async def level_100(url_100):
    pass

async def main(url):
    semaphore = asyncio.Semaphore()
    tasks_100 = []

    async with ClientSession() as session:
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.read())
            number_tag = soup.find('p', {'id': 'number'})
            links = soup.find_all('a', {'class': 'link'})
            print(number_tag)

            print(links)
            print(len(links))


asyncio.run(main(url='https://asyncio.ru/zadachi/3/index.html'))