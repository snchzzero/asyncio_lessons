import asyncio
from aiohttp import ClientSession
from bs4 import BeautifulSoup


async def level_5(url_5: str, semaphore, total: list):
    async with semaphore:
        async with ClientSession() as session:
            async with session.get(url_5) as response:
                soup = BeautifulSoup(await response.read())
                number_tag = soup.find('p', {'id': 'number'})
                if number_tag:
                    total.append(int(number_tag.text))


async def level_100(url_100: str, semaphore, total: list):
    tasks_5 = []
    async with semaphore:
        async with ClientSession() as session:
            async with session.get(url_100) as response:
                soup = BeautifulSoup(await response.read())
                tag_links = soup.find_all('a', {'class': 'link'})
                for link in tag_links:
                    depth_2 = link.get('href')
                    link_5 = f'https://asyncio.ru/zadachi/3/depth1/{depth_2}'
                    tasks_5.append(
                        asyncio.create_task(level_5(link_5, semaphore, total))
                    )

    await asyncio.gather(*tasks_5)


async def main(url):
    semaphore = asyncio.Semaphore(30)
    tasks_100 = []
    total = []

    async with ClientSession() as session:
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.read())
            tag_links = soup.find_all('a', {'class': 'link'})
            for link in tag_links:
                depth_1 = link.get('href')
                link_100 = f'https://asyncio.ru/zadachi/3/{depth_1}'
                tasks_100.append(
                    asyncio.create_task(level_100(link_100, semaphore, total))
                )

    await asyncio.gather(*tasks_100)
    print(total)
    print(len(total))
    print(sum(total))


asyncio.run(main(url='https://asyncio.ru/zadachi/3/index.html'))
