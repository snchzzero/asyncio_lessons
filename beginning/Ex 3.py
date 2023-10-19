import time

# Функция для вычисления факториала
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

start_time = time.time()

# Вычисление факториала для каждого числа от 1 до 20
for i in range(1, 21):
    print(f'Факториал {i} = {factorial(i)}')  # Выводим факториал числа

end_time = time.time()
print(f'Вычислено 20 факториалов за {end_time - start_time} секунд')  # Выводим общее время вычисления