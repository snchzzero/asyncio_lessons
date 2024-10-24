import asyncio


async def read_book(student, time):
    print(f"{student} начал читать книгу.")
    await asyncio.sleep(time)
    print(f"{student} закончил читать книгу за {time} секунд.")


async def main():
    # Создаем задачи для асинхронного выполнения
    task_1 = asyncio.create_task(
        read_book('Алекс', 5)
    )
    task_2 = asyncio.create_task(
        read_book('Мария', 3)
    )
    task_3 = asyncio.create_task(
        read_book('Иван', 4)
    )
    await task_1
    await task_2
    await task_3


asyncio.run(main())