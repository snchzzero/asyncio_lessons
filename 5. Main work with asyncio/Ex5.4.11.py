import asyncio

async def countdown(name, seconds):
    actions = {
        'Квест на поиск сокровищ': 'Найди скрытые сокровища!',
        'Побег от дракона': 'Беги быстрее, дракон на хвосте!'
    }
    finish_action = {
        'Квест на поиск сокровищ': 'Квест на поиск сокровищ: Задание выполнено! Что дальше?',
        'Побег от дракона': 'Побег от дракона: Задание выполнено! Что дальше?'
    }
    for end_second in range(seconds, 0, -1):
        print(f"{name}: Осталось {end_second} сек. {actions[name]}")
        await asyncio.sleep(1)
    print(f"{finish_action[name]}")

async def main():
    treasure_hunt = asyncio.create_task(countdown('Квест на поиск сокровищ', 10))
    dragon_escape = asyncio.create_task(countdown('Побег от дракона', 5))
    await asyncio.gather(treasure_hunt, dragon_escape)
    print()



asyncio.run(main())
