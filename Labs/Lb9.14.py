"""Lab9 var14  python3.11"""

file_path = 'Lb9.14-example.txt'  # путь до файла, или ваш путь
separate = ' '  # разделитель при, котором происходит поиск и разделение чисел из строки


def float_validation(symbols: str):
    try:
        return float(symbols)
    except ValueError:
        return False


with open(file_path, 'r') as file:
    digits = set()  # множество, что бы избежать повторения цифр
    all_file_lines = file.readlines()
    for line in all_file_lines:
        list_after_split = line.rstrip().split(separate)  # rstrip - удаляет символ конца строки "\n"
        line_digits = set(
            float(symbols) for symbols in list_after_split
            if float_validation(symbols)
        )
        digits.add(
            min(line_digits)
        )
    result = min(digits)
    print('result ', result)
