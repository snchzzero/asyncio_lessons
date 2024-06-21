import asyncio


async def set_future_result(value, delay):
    print(f"Задача начата. Установка результата '{value}' через {delay} секунд.")
    await asyncio.sleep(delay)
    print("Результат установлен.")
    return value


async def create_and_use_future():
    task = asyncio.ensure_future(
        set_future_result('Успех', 2)
    )
    if task.done():
        print("Состояние Future до выполнения: Завершено")
    else:
        print("Состояние Future до выполнения: Ожидание")

    print("Задача запущена, ожидаем завершения...")
    await task

    if task.done():
        print("Состояние Future после выполнения: Завершено")
        result = task.result()
        return result
    else:
        print("Состояние Future после выполнения: Ожидание")


async def main():
    result = await create_and_use_future()
    print("Результат из Future:", result)


asyncio.run(main())
