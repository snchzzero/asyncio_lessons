import asyncio


async def activate_portal(x):
    print(f"Активация портала в процессе, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return f"Результат активации портала: {x*2} единиц энергии"


async def perform_teleportation(x):
    print(f"Телепортация в процессе, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return f"Результат телепортации: {x+2} единиц времени"


async def recharge_portal(x):
    print(f"Подзарядка портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return f"Результат подзарядки портала: {x*3} единиц энергии"


async def check_portal_stability(x):
    print(f"Проверка стабильности портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return f"Результат проверки стабильности: {x+4} единиц времени"


async def restore_portal(x):
    print(f"Восстановление портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return f"Результат восстановления портала: {x*5} единиц энергии"


async def close_portal(x):
    print(f"Закрытие портала, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return f"Результат закрытия портала: {x-1} единиц времени"


async def portal_operator():
    task_1 = asyncio.ensure_future(activate_portal(2))
    task_2 = asyncio.ensure_future(perform_teleportation(3))
    task_3 = asyncio.ensure_future(recharge_portal(4))
    task_4 = asyncio.ensure_future(check_portal_stability(5))
    task_5 = asyncio.ensure_future(restore_portal(6))
    task_6 = asyncio.ensure_future(close_portal(7))
    result = await asyncio.gather(*[task_1, task_2, task_3, task_4, task_5, task_6])
    for res in result:
        print(res)


asyncio.run(portal_operator())


