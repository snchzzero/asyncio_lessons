import asyncio


async def activate_portal(x):
    print(f"Активация портала в процессе, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x*2


async def perform_teleportation(x):
    print(f"Телепортация в процессе, требуется времени: {x} единиц")
    await asyncio.sleep(x)
    return x+2


async def portal_operator():
    x = 4
    res_1 = await asyncio.ensure_future(activate_portal(x))
    x = 1 if res_1 > 4 else res_1
    res_2 = await asyncio.ensure_future(perform_teleportation(x))
    print(f"Результат активации портала: {res_1} единиц энергии")
    print(f"Результат телепортации: {res_2} единиц энергии")


asyncio.run(portal_operator())