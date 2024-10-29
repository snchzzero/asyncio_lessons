import asyncio


async def monitor_cpu(status_list):
    task_name = asyncio.current_task().get_name()
    for status in status_list:
        print(f"[{task_name}] Статус проверки: {status}")
        if status == 'Катастрофически':
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")
            break
        await asyncio.sleep(0.1)


async def monitor_memory(status_list):
    task_name = asyncio.current_task().get_name()
    for status in status_list:
        if status == 'Катастрофически':
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")
            break
        print(f"[{task_name}] Статус проверки: {status}")
        await asyncio.sleep(0.1)


async def monitor_disk_space(status_list):
    task_name = asyncio.current_task().get_name()
    for status in status_list:
        if status == 'Катастрофически':
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")
            break
        print(f"[{task_name}] Статус проверки: {status}")
        await asyncio.sleep(0.1)


async def main():
    status_list = [
        "Отлично", "Хорошо", "Удовлетворительно", "Средне",
        "Пониженное", "Ниже среднего", "Плохо", "Очень плохо",
        "Критично", "Катастрофически"
    ]
    task_1 = asyncio.create_task(monitor_cpu(status_list), name='CPU')
    task_2 = asyncio.create_task(monitor_cpu(status_list), name='Память')
    task_3 = asyncio.create_task(monitor_cpu(status_list), name='Дисковое пространство')

    await asyncio.gather(task_1, task_2, task_3)



asyncio.run(main())
