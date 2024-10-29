import asyncio



async def analyze_news(keyword, news_list, delay):
    await asyncio.sleep(delay)
    for definition in news_list:
        if keyword in definition:
            print(f"Найдено соответствие для '{keyword}': {definition}")
            await asyncio.sleep(0.1)


async def main():
    news_list = [
        "Новая волна COVID-19 обрушилась на Европу",
        "Рынки акций растут на фоне новостей о вакцине",
        "Комиссия приняла решение о вакцинации от COVID-19",
        "Важные события в мире вакцинации COVID-19",
        "Общее сообщение о вакцинации от COVID-19",
        "Сообщение о вакцинации от COVID-19 в мире",
        "Общее сообщение о вакцинации от COVID-19 в Европе",
        "Общее сообщение о вакцинации от COVID-19 в США",
        "Общее сообщение о вакцинации от COVID-19 в Бразилии"
    ]

    # Создаем асинхронные задачи для каждой корутины с разными ключевыми словами и задержками
    task1 = asyncio.create_task(analyze_news('COVID-19', news_list, 0.5))
    task2 = asyncio.create_task(analyze_news('игр', news_list, 0.5))
    task3 = asyncio.create_task(analyze_news('новый вид', news_list, 0.5))

    # Ожидаем выполнения всех задач
    await asyncio.gather(task1, task2, task3)


asyncio.run(main())
