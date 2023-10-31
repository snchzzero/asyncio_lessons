import asyncio

# Counter_1 - имя счётчика
# 13 - максимальное значение для счётчика Counter_1

max_counts = {
    "Counter 1": 13,
    "Counter 2": 7
}

counters = {
    "Counter 1": 0,
    "Counter 2": 0
}


async def counter(name, timeout):
    while counters[name] < max_counts[name]:
        await asyncio.sleep(timeout)
        counters[name] += 1
        print(f'{name}: {counters[name]}')


async def main():
    tasks = [asyncio.create_task(counter(name, 1)) for name in ['Counter 1', 'Counter 2']]
    await asyncio.gather(*tasks)

asyncio.run(main())
