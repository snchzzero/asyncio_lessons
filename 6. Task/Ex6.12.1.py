import asyncio

codes = [
    "56FF4D", "A3D2F7", "B1C94E", "F56A1D", "D4E6F1",
    "A1B2C3", "D4E5F6", "A7B8C9", "D0E1F2", "A3B4C5",
    "D6E7F8", "A9B0C1", "D2E3F4", "A5B6C7", "D8E9F0"
]


messages = [
    "Привет, мир!", "Как дела?", "Что нового?", "Добрый день!", "Пока!",
    "Спокойной ночи!", "Удачного дня!", "Всего хорошего!", "До встречи!",
    "Счастливого пути!","Успехов в работе!", "Приятного аппетита!",
    "Хорошего настроения!", "Спасибо за помощь!", "Всего наилучшего!"
]


async def message_print(index):
    print(f'Сообщение: {messages[index]}')

    return index


def code_print(task):
    print(f'Код: {codes[task.result()]}')


async def main():
    for index in range(0, len(messages)):
        task = asyncio.create_task(message_print(index))
        task.add_done_callback(code_print)
        await task


asyncio.run(main())
