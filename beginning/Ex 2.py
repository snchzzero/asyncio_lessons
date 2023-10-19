import time
import urllib.request

# Список URL для загрузки
urls = [
    'http://www.python.org',
    'http://www.python.org/about/',
    'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
    'http://www.python.org/doc/',
    'http://www.python.org/download/',
    'http://www.python.org/getit/',
    'http://www.python.org/community/',
    'https://wiki.python.org/moin/',
]

start_time = time.time()

# Загрузка каждого URL
for url in urls:
    print(f'Загрузка {url}')  # Выводим сообщение о загрузке URL
    response = urllib.request.urlopen(url)
    print(f'Загружено {url}')  # Выводим сообщение о завершении загрузки URL

end_time = time.time()
print(f'Загружено {len(urls)} URL за {end_time - start_time} секунд')  # Выводим общее время загрузки