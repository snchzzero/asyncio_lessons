import asyncio

# Словарь файлов и их размеров
files = {
    "file1.mp4": 32,
    "image2.png": 24,
    "audio3.mp3": 16,
    "document4.pdf": 8,
    "archive5.zip": 40,
    "video6.mkv": 48,
    "presentation7.pptx": 12,
    "ebook8.pdf": 20,
    "music9.mp3": 5,
    "photo10.jpg": 7,
    "script11.py": 3,
    "database12.db": 36,
    "archive13.rar": 15,
    "document14.docx": 10,
    "spreadsheet15.xls": 25,
    "image16.gif": 2,
    "audioBook17.mp3": 60,
    "tutorial18.mp4": 45,
    "code19.zip": 22,
    "profile20.jpg": 9
}

async def download_file(file_name, size, speed):
    time_download = size/speed
    print(f'Начинается загрузка файла: {file_name},'
          f' его размер {size} мб, '
          f'время загрузки составит {time_download} сек')
    await asyncio.sleep(time_download)
    print(f'Загрузка завершена: {file_name}')



async def monitor_tasks(tasks):
    for task in tasks:
        status = 'в процессе' if not task.done() else 'завершена'
        print(f'Задача {task.get_name()}: {status}, Статус задачи {task.done()}')
    await asyncio.sleep(1)


async def main():
    tasks = [
        asyncio.create_task(
            name=file_name,
            coro=download_file(
                file_name=file_name,
                size=size,
                speed=8
            )
        ) for file_name, size in files.items()
    ]
    all_tasks = tasks
    while tasks:
        await monitor_tasks(all_tasks)
        done, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    await monitor_tasks(all_tasks)
    print('Все файлы успешно загружены')



asyncio.run(main())
