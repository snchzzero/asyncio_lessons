import asyncio
import random


async def scan_port(address, port):
    await asyncio.sleep(0.1)
    status_port = random.choice([True, False])
    if status_port:
        print(f'Порт {port} на адресе {address} открыт')
        return port


async def scan_range(address, start_port, end_port):
    print(f'Сканирование портов с {start_port} по {end_port} на адресе {address}')
    tasks = [asyncio.create_task(scan_port(address, port)) for port in range(int(start_port), int(end_port))]
    await asyncio.gather(*tasks)
    open_ports = []
    for task in tasks:
        if task.result():
            open_ports.append(task.result())

    if open_ports:
        print(f'Открытые порты на адресе {address}: {open_ports}')
    if not open_ports:
        print(f'Открытых портов на адресе {address} не найдено')


asyncio.run(scan_range('192.168.0.1', 80, 85))


E