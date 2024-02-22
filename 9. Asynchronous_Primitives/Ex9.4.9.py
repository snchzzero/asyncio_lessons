import asyncio

storage = 0

wood_resources_dict = {
    'Деревянный меч': 6,
    'Деревянный щит': 12,
    'Деревянный стул': 24,
}


async def gather_wood(condition, event):
    # Код по добыче 2ед древесины в секунду
    global storage
    while True:
        async with condition:
            if event.is_set():
                break
            await asyncio.sleep(1)
            storage += 2
            condition.notify()
        print(f"Добыто 2 ед. дерева. На складе {storage} ед.")


async def craft_item(condition, event):
    # Код изготовлению деревянных предметов
    global storage
    made = []
    while not event.is_set():
        async with condition:
            await condition.wait()
            for item in wood_resources_dict:
                if item not in made and wood_resources_dict[item] <= storage:
                    print(f"Изготовлен {item}.")
                    storage -= wood_resources_dict[item]
                    made.append(item)
            if len(made) == 3:
                event.set()


async def main():
    condition = asyncio.Condition()
    event = asyncio.Event()
    tasks = [
        asyncio.create_task(gather_wood(condition, event)),
        asyncio.create_task(craft_item(condition, event))
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())
