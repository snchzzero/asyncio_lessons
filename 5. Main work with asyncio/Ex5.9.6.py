import asyncio
import random

# Не менять!
random.seed(1)

async def collect_gold():
    sleep_time = random.randint(1, 5)
    await asyncio.sleep(sleep_time)
    return random.randint(10, 50)



async def main():
    tasks = [
        asyncio.create_task(
            collect_gold()
        )
        for _ in range(10)
    ]
    total_score = 0
    for task in asyncio.as_completed(tasks):
        result = await task
        total_score += result
        print(f'Собрано {result} единиц золота.')
        print(f'Общее количество золота: {total_score} единиц.')
        print()




asyncio.run(main())
