import asyncio
import random

class Pizzeria:
    def __init__(self, name):
        self.name = name

    async def make_pizza(self, order_id):
        cook_time = random.randint(2, 5)      # случайное время готовки пиццы от 2 до 5 секунд
        print(f'Пиццерия {self.name} начала готовить пиццу для заказа {order_id}.')
        await asyncio.sleep(cook_time)        # ожидание пока пицца готовится
        print(f'Пиццерия {self.name} закончила готовить пиццу для заказа {order_id}.')

async def main():
    pizzeria = Pizzeria("Тесто & Сыр")

    # создание 5 заказов
    tasks = [asyncio.create_task(pizzeria.make_pizza(i)) for i in range(1, 6)]

    # запуск всех задач (заказов) в Event Loop
    await asyncio.gather(*tasks)

# запуск Event Loop
asyncio.run(main())