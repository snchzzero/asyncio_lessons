import asyncio

# Определение корутины
async def my_coroutine():
    print("Запуск корутины")
    await asyncio.sleep(1)  # Приостановка корутины на 1 секунду
    print("Завершение корутины")

# Создание задачи из корутины
async def main():
    task = asyncio.create_task(my_coroutine())
    await task

# Запуск event loop
asyncio.run(main())
