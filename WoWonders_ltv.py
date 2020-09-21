import itertools
import os
import sys
import time
import pickle

def sortByLength(inputStr):
    return len(inputStr)

retr = 'Да'

while retr == 'Да':
    word = str(input('Введите набор букв: ')).lower()
    combinations = []
    while len(word) <= 2:
        print('-'*43 + '\nМинимальная длина набора букв - 3 символа!')
        print('Введите STOP для отмены или повторите ввод.\n' + '-'*43)
        word = str(input('Повторите ввод: ')).lower()
        if word == 'STOP':
            sys.exit()
    for i in range(3, len(word) + 1):
        for items in itertools.permutations(word, i):
                combinations.append(''.join(str(ch) for ch in items))

    combinations = list(set(combinations))

    #### main ############################################

    with open('normalize.txt', 'r', encoding = 'UTF-8-SIG') as f:
        lib = [line.strip().lower() for line in f]
    lib = list(set(lib))
        
    result = list(set(lib) & set(combinations))
    #result.sort(key=sortByLength, reverse=True)
    other = list(set(result) ^ set(combinations))

    i = 1
    print('Результат по словарю: ')
    for ch in sorted(result, key=len, reverse=True):
        print(str(i) + ': ' + ch)
        i += 1

    q = str(input('Вывести все возможные оставшиеся комбинации? (Да / Нет): '))
    if q == 'Да':
        l = int(input('Введите необходимую длину слова: '))
        i = 1  
        print('Оставшиеся комбинации из '+str(l)+' символов: ')
        for ch in sorted(other):
            if len(ch) == l:
                print(str(i) + ': ' + ch)
                i += 1

    retr = str(input('Играть снова? (Да / Нет): '))
#### main ############################################
close = input("Press Enter to close programm.")
if close:
    sys.exit()
