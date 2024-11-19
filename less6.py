import random

import math as m


# 1
def binary_search():
    value = int(input('Введите искомое число для поиска в списке: '))
    some_list_two = [1, 2, 3, 4, 5, 6, 11]
    mid = len(some_list_two) // 2
    low = 0
    high = len(some_list_two) - 1
    while some_list_two[mid] != value and low <= high:
        if value > some_list_two[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    if low > high:
        print("No value")
    else:
        print("ID =", mid)


# 2
def binar_system():
    value_two = int(input('Введите целое положительное число для перевода в двоичную систему:'))
    if value_two < 0:
        print ('Error')
    bi_system = ''
    while value_two > 0:
        bi_system = str(value_two % 2) + bi_system
        value_two = value_two // 2
    print(bi_system)


# 3

def is_prime(simple_value):
    i = 2
    while i <= m.sqrt(simple_value):
        if simple_value % i == 0:
            return False
        i += 1
    if simple_value > 1:
        return True


# 4
def nok():
    value_a = int(input('Введите первое число для поиска НОД:'))
    value_b = int(input('Введите второе число для поиска НОД:'))

    while value_a != 0 and value_b != 0:
        if value_a > value_b:
            value_a = value_a % value_b
        else:
            value_b = value_b % value_a
    print(value_a + value_b)


# 5
def deshifr(alfavit_EU='ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    smeshenie = int(input('Шаг шифровки: '))
    message = input("Сообщение для ДЕшифровки: ").upper()
    itog = ''
    lang = input('Выберите язык RU/EU: ')
    if lang == 'RU':
        for i in message:
            mesto = alfavit_RU.find(i)
            new_mesto = mesto - smeshenie
            if i in alfavit_RU:
                itog += alfavit_RU[new_mesto]
            else:
                itog += i
    else:
        for i in message:
            mesto = alfavit_EU.find(i)
            new_mesto = mesto - smeshenie
            if i in alfavit_EU:
                itog += alfavit_EU[new_mesto]
            else:
                itog += i
    print(itog)


def shifr(alfavit_EU='ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    smeshenie = int(input('Введите шаг смещения:'))
    message = input('Введите текст для шифрования:').upper()
    itog = ''
    lang = input('Выберите язык RU/EU: ').upper()
    if lang == 'RU':
        alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        for i in message:
            mesto = alfavit_RU.find(i)
            new_mesto = mesto + smeshenie
            if i in alfavit_RU:
                itog += alfavit_RU[new_mesto]
            else:
                itog += i
    else:
        for i in message:
            mesto = alfavit_EU.find(i)
            new_mesto = mesto + smeshenie
            if i in alfavit_EU:
                itog += alfavit_EU[new_mesto]
            else:
                itog += i
    print(itog)


# 7
def creat_array():
    r = 0
    colom = int(input('Введите количество столбцов'))
    line = int(input('Введите количество строк'))
    array = []
    r = random.randint(1, 50)
    for i in range(colom):
        array.append([])
        for j in range(line):
            array[i].append(random.randint(0, 50))

    print('Matrix:')
    for u in range(colom):
        print(array[u])
    return array


# 8
def max_and_min():
    matrix = creat_array()
    max_valua = matrix[0][0]
    max_i = 0
    max_j = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] >= max_valua:
                max_valua = matrix[i][j]
                max_i = i
                max_j = j

    print('Максимальное число:', max_i, max_j)
    max_valua = matrix[0][0]
    max_i = 0
    max_j = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] <= max_valua:
                max_valua = matrix[i][j]
                max_i = i
                max_j = j
    print('Минимальное число:', max_i, max_j)


# 9
def sum_by():
    matrix = creat_array()
    total_sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            total_sum += matrix[i][j]
    print('Общая сумма:', total_sum)

    for i in range(len(matrix)):
        colom_sum = 0
        for j in range(len(matrix[i])):
            colom_sum += matrix[j][i]
        print('Процернт каждого столбика от общей суммы', colom_sum / total_sum * 100)


# 10
def multiply_columns():
    matrix = creat_array()
    k = int(input('Введите cтолбец для расчета произведения:'))
    if not matrix or k < 0 or k >= len(matrix[0]):
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for j in range(cols):
        column_result = []
        for i in range(rows):
            column_result.append(matrix[i][j] * matrix[i][k])
        result.append(column_result)
    print('Произведение столбца и задонного столбца в матрице:')
    for u in range(cols):
        print(result[u])
    return result


# 11
def sum_matrix_row():
    matrix =creat_array()
    row_number = int(input("Введите номер строки: "))
    row_to_add = matrix[row_number]
    new_matrix = []

    for row in matrix:
        new_row = [x + y for x, y in zip(row, row_to_add)]
        new_matrix.append(new_row)

    return new_matrix



# 12
def find_number():
    matrix = creat_array()
    number = int(input('Введите число для поиска:'))
    columns_with_number = []
    columns_without_number = []
    cols = len(matrix[0])
    for j in range(cols):
        column = [matrix[i][j] for i in range(len(matrix))]
        if number in column:
            columns_with_number.append(j)
        else:
            columns_without_number.append(j)
    print(f'Столбцы с искомым числом - {columns_with_number},столбцы без этого числа - {columns_without_number}')
    return columns_with_number, columns_without_number


# 13
def diagonal_sums():
    matrix = creat_array()
    rows = len(matrix)
    cols = len(matrix[0])
    main_diagonal_sum = sum(matrix[i][i] for i in range(min(rows, cols)))
    side_diagonal_sum = sum(matrix[i][cols - 1 - i] for i in range(min(rows, cols)))

    print(f'Сумма главной диагонали:{main_diagonal_sum},Сумма побочной диагонали:{side_diagonal_sum}')


# 14
def add_even_column():
    matrix = [
        [1, 1, 1],
        [0, 1, 1],
        [1, 1, 0]
    ]
    print(matrix)
    new_matrix = []
    for row in matrix:
        count = sum(row)
        if count % 2 == 0:
            new_row = row + [1]
        else:
            new_row = row + [0]
        new_matrix.append(new_row)
    print(f'Матрица с четным количеством единиц{new_matrix}')


# 1
print('Список чисел для поиска индекса: 1, 2, 3, 4, 5, 6, 11')
binary_search()
print('______________________________________________________')

# 2
binar_system()
print('_______________________________________________________')

# 3


value_three = int(input('Введите целое положительное число, чтобы узнать простое ли оно:'))

if is_prime(value_three):
    print("Простое число")
else:
    print("Число НЕ является простым")

print('_______________________________________________________')

# 4

nok()
print('_______________________________________________________')

# 5
cesar = input('Если хотите зашифровать, напишите 1 / Дешифровать - 2')
if cesar == '1':
    shifr()
elif cesar == '2':
    deshifr()
print('_______________________________________________________')

# 7
creat_array()
print('_______________________________________________________')

# 8
max_and_min()
print('_______________________________________________________')

# 9
sum_by()
print('_______________________________________________________')

# 10

multiply_columns()
print('_______________________________________________________')


# 11
new_matrix = sum_matrix_row()

print("Новая матрица:")
for row in new_matrix:
    print(row)
print('_______________________________________________________')

# 12
find_number()
print('_______________________________________________________')

# 13
diagonal_sums()
print('_______________________________________________________')

# 14
add_even_column()
