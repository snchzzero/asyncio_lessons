import asyncio

books_json = [
    {
        "Порядковый номер": 1,
        "Автор": "Rebecca Butler",
        "Название": "Three point south wear score organization.",
        "Год издания": "1985",
        "Наличие на полке": True
    },
    {
        "Порядковый номер": 2,
        "Автор": "Mark Cole",
        "Название": "Drive experience customer somebody pressure.",
        "Год издания": "1985",
        "Наличие на полке": True
    },
    {
        "Порядковый номер": 3,
        "Автор": "Mark Coless",
        "Название": "Drive experience customer somebody unknown.",
        "Год издания": "1988",
        "Наличие на полке": False
    }
]


async def check_book(book):
    if not book.get('Наличие на полке'):
        num = book.get('Порядковый номер')
        author = book.get('Автор')
        name = book.get('Название')
        year = book.get('Год издания')
        print(f'{num}: {author}: {name} ({year})')

async def main():
    tasks = [asyncio.create_task(check_book(book)) for book in books_json]
    await asyncio.gather(*tasks)


asyncio.run(main())