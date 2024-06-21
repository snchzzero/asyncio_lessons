import asyncio


async def async_operation():
    try:
        print("Начало асинхронной операции.")
        await asyncio.sleep(2)
        print("Асинхронная операция успешно завершилась.")
    except asyncio.CancelledError:
        print("Асинхронная операция была отменена в процессе выполнения.")
        raise


async def main():
    print("Главная корутина запущена.")
    future = asyncio.ensure_future(
        async_operation()
    )

    await asyncio.sleep(0.1)
    print("Попытка отмены Future.")

    future.cancel()
    await asyncio.sleep(0.1)
    print("Обработка исключения: Future был отменен.")

    # Проверяем, отменился ли Future
    if future.cancelled():
        print("Проверка: Future был отменен.")
    else:
        print("Проверка: Future не был отменен.")

    print("Главная корутина завершена.")

asyncio.run(main())