import asyncio


async def sensor_movs(event, index:int, ip: str):
    print(f'Датчик {index} IP-адрес {ip} настроен и ожидает срабатывания')
    await event.wait()
    print(f'Датчик {index} IP-адрес {ip} активирован, "Wee-wee-wee-wee"')


async def set_signal(event):
    await asyncio.sleep(5)
    print('Датчики зафиксировали движение')
    event.set()


async def main():
    event = asyncio.Event()
    ip = ["192.168.0.3", "192.168.0.1", "192.168.0.2", "192.168.0.4", "192.168.0.5"]
    tasks = [
        asyncio.create_task(
            sensor_movs(
                event=event,
                index=index,
                ip=sensor_ip
            )
        ) for index, sensor_ip in enumerate(ip)
    ]
    await asyncio.gather(*tasks, asyncio.create_task(set_signal(event)))

asyncio.run(main())
