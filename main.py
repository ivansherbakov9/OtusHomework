SYMBOLS = \
    'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def splitting(str):
    result = ""
    rev_str = str[::-1]
    for i in range(len(rev_str)):
        if i % 3 == 0 and i != 0:
            result += " "
        result += rev_str[i]
    return result[::-1]


def snake_to_camel(str):
    result = ""
    list = str.split("_")
    print(len(list))
    for i in range(len(list)):
        if i == 0:
            result += list[i].capitalize()
        else:
            result += list[i][0].upper() + list[i][1:]
    return result


def camel_to_snake(str):
    result = ''
    for char in str:
        if char.isupper():
            result += '_' + char.lower()
        else:
            result += char
    if result[0] == "_":
        result = result[1:]
    return result


def сaesar_сipher(message, key, mode="e"):
    if mode == 'd':
        key = -key

    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1:#если символа нет(пробел)
            translated += symbol
        else:
            symbolIndex += key

            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)

            translated += SYMBOLS[symbolIndex]

    return translated


inp = str(input("Введите число(Формат: 123456) "))
print(splitting(inp))

inp2 = str(input("Введите snake_case "))
print(snake_to_camel(inp2))

inp3 = str(input("Введите CamelCase "))
print(camel_to_snake(inp3))

mode = str(input("Зашифровать/Расшифровать? (e / d) "))
msg = str(input("Введите сообщение "))
key = int(input("Введите ключ "))

print(сaesar_сipher(msg, key, mode=mode))
