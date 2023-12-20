import asyncio
from itertools import product
import random

shapes = ["circle", "star", "square", "diamond", "heart"]
colors = ["red", "blue", "green", "yellow", "purple"]
actions = ["change_color", "explode", "disappear"]


async def launch_firework(shape, color, action):
    print(f"Запущен {color} {shape} салют, в форме {action}!!!")
    await asyncio.sleep(random.randint(1, 5))
    print(f"Салют {color} {shape} завершил выступление {action}")


async def main():
    combinations = list(product(shapes, colors, actions))
    tasks = [asyncio.create_task(launch_firework(comb[0], comb[1], comb[2])) for comb in combinations]
    await asyncio.gather(*tasks)

asyncio.run(main())








