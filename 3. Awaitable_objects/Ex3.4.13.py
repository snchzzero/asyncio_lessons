import asyncio


async def first_function(x):
    print(f"Выполняется первая функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x + 1
    print(f"Первая функция завершилась с результатом {result}")
    return result


async def second_function(x):
    print(f"Выполняется вторая функция с аргументом {x}")
    result = x * 2
    print(f"Вторая функция завершилась с результатом {result}")
    return result


async def third_function(x):
    print(f"Выполняется третья функция с аргументом {x}")
    result = x + 3
    print(f"Третья функция завершилась с результатом {result}")
    return result


async def fourth_function(x):
    print(f"Выполняется четвертая функция с аргументом {x}")
    result = x ** 2
    print(f"Четвертая функция завершилась с результатом {result}")
    return result


async def main():
    print("Начало цепочки асинхронных вызовов")
    future_1 = asyncio.ensure_future(first_function(1))
    await future_1
    future_2 = asyncio.ensure_future(second_function(future_1.result()))
    await future_2
    future_3 = asyncio.ensure_future(third_function(future_2.result()))
    await future_3
    future_4 = asyncio.ensure_future(fourth_function(future_3.result()))
    await future_4
    final_result = future_4.result()
    print(f"Конечный результат цепочки вызовов: {final_result}")

asyncio.run(main())
