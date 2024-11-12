import asyncio

spells = {
    "Огненный шар": 3,
    "Ледяная стрела": 2,
    "Щит молний": 4,
    "Телепортация": 7
}

# Максимальное время для каста заклинания
max_cast_time = 5  # Секунды

# Ученики мага
students = ["Алара", "Бренн", "Сирил", "Дариа", "Элвин"]

async def cast_spell(student, spell, cast_time):
    try:
        await asyncio.sleep(cast_time)
        print (f"{student} успешно кастует {spell} за {cast_time} сек.")
    except asyncio.exceptions.CancelledError:
        await asyncio.sleep(cast_time)
        print (f"Ученик {student} не справился с заклинанием {spell}, и учитель применил щит. "
         f"{student} успешно завершает заклинание с помощью shield.")




async def main():
    all_tasks = []

    for student in students:
        all_tasks.extend(
            [
                asyncio.create_task(
                    asyncio.wait_for(
                        asyncio.shield(
                            cast_spell(student, spell_name, spell_time)
                        ),
                        max_cast_time
                    )
                )
                for spell_name, spell_time in spells.items()
            ]
        )

    try:
        await asyncio.gather(*all_tasks)
    except asyncio.exceptions.TimeoutError:
        pass



asyncio.run(main())