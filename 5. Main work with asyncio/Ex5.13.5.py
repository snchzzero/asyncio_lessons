import asyncio

articles = [
    {'title': 'Методы картирования генома', 'length': 3.2},
    {'title': 'Гормоны растений и их рост', 'length': 4.5},
    {'title': 'Применение CRISPR', 'length': 2.1},
    {'title': 'Микробное разнообразие', 'length': 1.5},
    {'title': 'Механика деления клеток', 'length': 4.1},
    {'title': 'Эпигенетическая регуляция', 'length': 3.8},
    {'title': 'Динамика сворачивания белков', 'length': 4.0},
    {'title': 'Экологические взаимодействия', 'length': 0.7},
    {'title': 'Модели нейронных сетей', 'length': 4.3},
    {'title': 'Пути биолюминесценции', 'length': 2.9}
]

async def upload_article(article):
    length = article['length']
    await asyncio.sleep(length)
    current_event_loop = asyncio.get_running_loop()
    article['loop'] = current_event_loop

async def main():
    tasks = [
        asyncio.create_task(
            upload_article(article)
        ) for article in articles
    ]
    await asyncio.gather(*tasks)
    print('Все статьи успешно загружены в библиотеку ')


asyncio.run(main())