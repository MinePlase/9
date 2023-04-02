lang = input('Выберете язык (ru/eng)')
message = input('Введите слово: ')
message = message.lower()
chiper = []
ALPHABET_RU="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ALPHABET_EN="abcdefghijklmnopqrstuvwxyz"
step = int(input('Введите шаг сдвига (число): '))
if lang == 'ru':
    for symbol in message:
        chiper.append(ALPHABET_RU.find(symbol) + step)
    print(chiper)
    for item in range(len(chiper)):
        chiper[item] -= step
    print('Дешифровка: ')
    print(chiper)
    symb = [ALPHABET_RU[num] for num in chiper]
    result = ''.join(symb)
    print(result)
elif lang == 'eng':
    for symbol in message:
        chiper.append(ALPHABET_EN.find(symbol) + step)
    print(chiper)
    for item in range(len(chiper)):
        chiper[item] -= step
    print('Дешифровка: ')
    print(chiper)
    symb = [ALPHABET_EN[num] for num in chiper]
    result = ''.join(symb)
    print(result)
