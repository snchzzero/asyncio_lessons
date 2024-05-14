import asyncio
from bs4 import BeautifulSoup
from aiohttp import ClientSession

url = 'https://asyncio.ru/zadachi/1/index.html'

code_dict = {
    0: 'F',
    1: 'B',
    2: 'D',
    3: 'J',
    4: 'E',
    5: 'C',
    6: 'H',
    7: 'G',
    8: 'A',
    9: 'I'
}


async def main(url_pars: str):
    encoding = ''
    async with ClientSession() as session:
        async with session.get(url_pars) as response:
            read = await response.content.read()
            soup = BeautifulSoup(read)
            p_text = soup.find('p').text.strip()
            for digit in p_text:
                encoding += code_dict[int(digit)]
    print('encoding ', encoding)


asyncio.run(main(url))
