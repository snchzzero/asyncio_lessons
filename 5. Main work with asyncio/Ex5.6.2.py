import asyncio

equipment_list = [
    '#001 ps5f6537c5-506f-43c2-b095-1890ef579c52: 265 units',
    '#002 ps5ec3020b-022f-466b-845a-a8f11161a6d1: 39 units',
    '#003 psb5c6c090-4f1a-4741-936e-5fe2b3e8d181: 242 units',
    '#004 ps10c90127-a4a5-4f85-b23f-66421ab04b09: 108 units',
    '#005 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units',
    '#006 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units',
    '#007 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units',
    '#008 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units',
    '#009 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units',
    '#010 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units',
    '#011 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units',
    '#012 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units',
    '#013 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units',
    '#014 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units',
    '#015 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units',
    '#016 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units',
    '#017 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units',
    '#018 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units',
    '#019 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units',
    '#020 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units',
    '#021 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units',
    '#022 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units',
    '#023 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units',
    '#024 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units',
    '#025 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units',
    '#026 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units',
    '#027 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units',
    '#028 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units',
    '#029 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units',
    '#030 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units',
    '#031 psa8b77d97-ef82-4832-9601-36abfc399af2: 72 units'
]


# Корутина для отправки запроса.
async def equipment_request(request):
    equipment = request.split(' ')[0]
    await asyncio.sleep(1)
    return f"{equipment} is Ok!"


# Корутина для управления отправкой запросов на заказ оборудования
async def send_requests():
    tasks = [asyncio.create_task(equipment_request(equipment)) for equipment in equipment_list]
    result = await asyncio.gather(*tasks)
    waiting_time = query_time()  # В метод ничего передавать не нужно!
    print(f"На отправку {len(result)} запросов потребовалось {waiting_time} секунд!")

asyncio.run(send_requests())