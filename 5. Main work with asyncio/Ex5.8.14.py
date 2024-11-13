import asyncio

dishes = {'Куриный суп': 118, 'Бефстроганов': 13, 'Рататуй': 49, 'Лазанья': 108, 'Паэлья': 51, 'Утка по-пекински': 41,
          'Суши': 116, 'Цезарь с курицей': 106, 'Маргарита пицца': 23, 'Шпинатный пирог': 29, 'Карри с курицей': 88,
          'Тирамису': 10, 'Греческий салат': 18, 'Фалафель': 102, 'Буррито': 90, 'Карбонара': 111,
          'Ризотто с грибами': 79, 'Фокачча': 38, 'Шашлык': 121, 'Газпачо': 95, 'Блинчики': 118, 'Сэндвич с авокадо': 67,
          'Кимчи': 80, 'Табуле': 68, 'Паста алла норма': 32, 'Жареный рис': 47, 'Том Ям': 19, 'Веганский бургер': 43,
          'Киш с луком': 61, 'Салат Нисуаз': 97}

async def cook_dish(name, duration):
    print(f"Приготовление {name} начато.")
    all_time = duration/10
    await asyncio.sleep(all_time)
    print(f"Приготовление {name} завершено. за {all_time}")

async def main():
    teasks = [
        asyncio.create_task(
            coro=cook_dish(name, duration),
            name=name
        )
        for name, duration in dishes.items()
    ]
    done, pending = await asyncio.wait(teasks, timeout=10, return_when=asyncio.ALL_COMPLETED)
    for task in pending:
        print(f"{task.get_name()} не успел(а,о) приготовиться и будет отменено.")
        task.cancel()

    print(f"\nПриготовлено блюд: {len(done)}. Не успели приготовиться: {len(pending)}.")




asyncio.run(main())
