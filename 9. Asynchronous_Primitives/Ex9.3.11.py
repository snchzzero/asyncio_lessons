import asyncio
import random

error = None
count = 0
sek = 0

async def monitor_rocket_launches(interrupt_flag):
    global count
    global error
    global sek
    try:
        # Допишите сюда цикл
        error = random.choice([True, False, False, False])
        if error:
            interrupt_flag.set()
        while not interrupt_flag.is_set():
            print(f"Мониторинг ракетных запусков... (Запуск номер {count} прошёл успешно)")
            count += 1
            sek += 1
            await asyncio.sleep(1)
            error = random.choice([True, False, False, False])
            if error:
                interrupt_flag.set()

    finally:
        # Поместите сообщение о завершении мониторинга
        print("Завершение мониторинга ракетных запусков")


async def main():
    global error
    global count
    global sek
    interrupt_flag = asyncio.Event()
    # Создайте Task задачу
    task = asyncio.create_task(monitor_rocket_launches(interrupt_flag))

    # Допишите сюда цикл
    while not interrupt_flag.is_set():
        await asyncio.sleep(5)
        if count < 50 or not error:
            interrupt_flag.clear()
        if error:
            print(f"Ошибка при запуске произошла на {sek} секунде =(")
            print("Отмена мониторинга ракетных запусков...")
            interrupt_flag.set()
        if not error:
            print(f"Время ожидания составило {sek} секунд. За это время ошибки не произошло")
    await task
    # Запустите созданную корутину в пункте 2 через await

if __name__ == "__main__":
    asyncio.run(main())