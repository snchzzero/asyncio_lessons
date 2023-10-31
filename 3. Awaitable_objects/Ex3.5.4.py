import asyncio

# Counter_1 - имя счётчика
# 13 - максимальное значение для счётчика Counter_1

max_counts = {
    "Counter 1": 10,
    "Counter 2": 5,
    "Counter 3": 15
}

delays = {
    "Counter 1": 1,
    "Counter 2": 2,
    "Counter 3": 0.5
}

counters = {
    "Counter 1": 0,
    "Counter 2": 0,
    "Counter 3": 0
}


async def counter(name, timeout):
    while counters[name] < max_counts[name]:
        await asyncio.sleep(timeout)
        counters[name] += 1
        print(f'{name}: {counters[name]}')


async def main():
    tasks = [asyncio.create_task(counter(key, value)) for key, value in delays.items()]
    await asyncio.gather(*tasks)

asyncio.run(main())
