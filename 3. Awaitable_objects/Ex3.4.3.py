import asyncio


async def generate(num):
    print(f"Корутина generate с аргументом {num}")


async def main():
    tasks = [asyncio.create_task(generate(i)) for i in range(10)]
    await asyncio.gather(*tasks)

asyncio.run(main())
