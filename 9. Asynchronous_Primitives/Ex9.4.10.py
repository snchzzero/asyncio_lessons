import asyncio

stone_resources_dict = {
    'Каменная плитка': 10,
    'Каменная ваза': 40,
    'Каменный столб': 50,
}

metal_resources_dict = {
    'Металлическая цепь': 6,
    'Металлическая рамка': 24,
    'Металлическая ручка': 54,
}

cloth_resources_dict = {
    'Тканевая занавеска': 8,
    'Тканевый чехол': 24,
    'Тканевое покрывало': 48,
}

condition = asyncio.Condition()
storage = {
    'stone': 0,
    'metal': 0,
    'cloth': 0
}


async def gather_stone(event, condition):
    # Добываем камень, 10ед каждую сек.
    global storage
    while True:
        await asyncio.sleep(1)
        async with condition:
            if event.is_set():
                break
            storage['stone'] += 10
            condition.notify_all()
        print(f"Добыто 10 ед. камня. На складе {storage['stone']} ед.")


async def gather_metal(event, condition):
    # Добываем металл, 6ед каждую сек.
    global storage
    while True:
        await asyncio.sleep(1)
        async with condition:
            if event.is_set():
                break
            storage['metal'] += 6
            condition.notify_all()
        print(f"Добыто 6 ед. металла. На складе {storage['metal']} ед.")


async def gather_cloth(event, condition):
    # Добываем ткань, 8ед каждую сек.
    global storage
    while True:
        await asyncio.sleep(1)
        async with condition:
            if event.is_set():
                break
            storage['cloth'] += 8
            condition.notify_all()
        print(f"Добыто 8 ед. ткани. На складе {storage['cloth']} ед.")




async def craft_stone_items(event, condition):
    # Мастерская по крафту из камня
    global storage
    made = []
    while not event.is_set():
        async with condition:
            await condition.wait()
            for item in stone_resources_dict:
                if item not in made and stone_resources_dict[item] <= storage['stone']:
                    print(f"Изготовлен {item} из камня.")
                    storage['stone'] -= stone_resources_dict[item]
                    made.append(item)
            if len(made) == 3:
                event.set()


async def craft_metal_items(event, condition):
    # Мастерская по крафту из мателла
    global storage
    made = []
    while not event.is_set():
        async with condition:
            await condition.wait()
            for item in metal_resources_dict:
                if item not in made and metal_resources_dict[item] <= storage['metal']:
                    print(f"Изготовлен {item} из металла.")
                    storage['metal'] -= metal_resources_dict[item]
                    made.append(item)
            if len(made) == 3:
                event.set()


async def craft_cloth_items(event, condition):
    # Мастерская по крафту из ткани
    global storage
    made = []
    while not event.is_set():
        async with condition:
            await condition.wait()
            for item in cloth_resources_dict:
                if item not in made and cloth_resources_dict[item] <= storage['cloth']:
                    print(f"Изготовлен {item} из ткани.")
                    storage['cloth'] -= cloth_resources_dict[item]
                    made.append(item)
            if len(made) == 3:
                event.set()


async def main():
    # Запускаем производства
    event_stone = asyncio.Event()
    event_metal = asyncio.Event()
    event_cloth = asyncio.Event()
    tasks = [
        asyncio.create_task(gather_stone(event_stone, condition)),
        asyncio.create_task(gather_metal(event_metal, condition)),
        asyncio.create_task(gather_cloth(event_cloth, condition)),
        asyncio.create_task(craft_stone_items(event_stone, condition)),
        asyncio.create_task(craft_metal_items(event_metal, condition)),
        asyncio.create_task(craft_cloth_items(event_cloth, condition))
    ]
    await asyncio.gather(*tasks)


asyncio.run(main())
