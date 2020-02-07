#!/usr/bin/env python3
# -*- coding: utf8 -*-
# -------------------------------------
# Program by
# Nikolaev
#
# Version
# 0.0
#
# Date
# 30.01.2020
# Dead_line = Date + 5
#
# Info
# Home work Sberbank
# -------------------------------------

# ---------------------------------------------------------------------------------------------------------------------#

########################################################################################################################

# ================================
#   Задание 1
# ================================
# Составить алгоритм и написать код программы, вычисляющей длину линии вертикального
# разреза фигуры y_razrez, значения площадей фигуры слева и справа от линии разреза s_left,
# s_right по значениям аргумента x, введенным с консоли:
##########
'''
    график симетричный относительно оси Х на промежутке от x=0 x=2 1я и 4я четв. с.к.
    график в 1й черверти ситемы координат состоит из:
        сектора единичной окружности описанной относительно точки x=1, y=0 на промежутке x=0, x=1
        инвертированного сектора  окружности описанной относительно точки x=2, y=1 на промежутке x=1, x=2
        + отраженный график в 4й черверти ситемы координат
    Для выходных данных достаточно рассмотреть только одну чать симетричного графика в одной из четвертей (1й)

    для нахождения длинны линии разделения графика на промежутке x=0, x=2 можно определить:
                    1 через теор Пифагора т.к. треугольник тХ. тПересеч. т.ЦОкруж прямоугольный:
                        на промежутке x=0, x=1 можно определить
                        катет L1(0-1)=  тХ.т.ЦОкруж = (1-x)
                        катет L2(0-1)=  тХ.тПересеч. = (G - (L1)**1/2)**1/2  гипотенуза по условиям G = 1

                        на промежутке x=1, x=2 можно определить инвертировав результат:
                        L1(1-2) =  тХ.т.ЦОкруж = (2-x)
                        L2'(1-2) = (G - (L1)**1/2)**1/2
                        L2(1-2) = 1- L2'(1-2)
                        Итого Длинна L = 2 * L2 при заданном X

                    2 через триганометрические зависимости:
                        на промежутке x=0, x=1 можно определить
                        L2(0-1)= sin(arcos(1/(1-x)))

                        на промежутке x=1, x=2 можно определить инвертировав результат:
                        L2(0-1)= 1 - sin(arcos(1/(2-x)))
                           необходима обработка на ошибку ZeroDivision
                        Итого Длинна L = 2 * L2 при заданном X

    для нахождения площади описываемой графиком на промежутке x=0, x=2 можно определить:
        промежуток x=0, x=1
        до пересечения
        - площадь сектора вычесть площадь вписанного треугольника = S(0-x)
        после пересечения
        - вычислить площадь четверти окружности S(x-1) = Sокр1/4 - S(0-x)

        промежуток x=1, x=2
        до пересечения
        - площадь фигуры S(1-x) = Прямоугольник c Sпр=1*(1-x) - сектор вычесть площадь вписанного треугольника S'(x-2)
        после пересечения
        - площадь фигуры S(x-2) = Прямоугольник c Sпр=1*(x-2) - (Sокр1/4 - S(x-2))

        Итого сложить необходимые площади и *2
'''
############# 111 start  ################

print('Задача 1\n')
print('Составить алгоритм и написать код программы, вычисляющей длину линии вертикального \n'
      'разреза фигуры y_razrez, значения площадей фигуры слева и справа от линии разреза s_left, \n'
      's_right по значениям аргумента x, введенным с консоли\n')
print('# default \nx = 0.5\nнажать enter для задания дефолтных значений')
# default
x_task_1 = 0.5
import math


def is_number(str):
    ''' проверяем является ли число вещественным'''
    try:
        float(str)
        return True
    except ValueError:
        return False


while True:
    ''' получаем значения от пользователя проводим валидацию'''
    inp_x_task_1 = input('введите x от 0 до 2           пример "0.5"    : ')
    if inp_x_task_1 == '':
        # default
        break
        pass
    elif not is_number(inp_x_task_1) or not float(inp_x_task_1) >= 0 or not float(inp_x_task_1) <= 2:
        print('error variable not 0-2')
        continue
    else:
        x_task_1 = float(inp_x_task_1)
        break


class SectorOneRadiusCircle:
    '''
    класс описывает фигуру сектор
    атрибуты:
     height - высота прямоугольного треугольника вписанного в сектор
     array_triangle - площадь прямоугольного треугольника
     array_sector - площадь сектора
     array_sector_del_array_triangle пльщадь части сектора между треугольником и окружностью
    '''

    def __init__(self, center_to_x):
        self._x = center_to_x
        self.height = math.sin(math.acos(self._x))
        self.array_triangle = self._x * self.height * 0.5
        self.array_sector = math.pi * math.acos(self._x) / (2 * math.pi)
        self.array_sector_del_array_triangle = self.array_sector - self.array_triangle


'''найдем полную площадь фигуры'''
# на промежутке [0:1]
radius = 1
s_0_1 = 2 * math.pi * (radius ** 2) / 4  # четверть круга умноженная на 2
# на промежутке (1:2]
rect_area = 1 * 1
s_1_2 = 2 * rect_area - s_0_1  # из прямоугольной области вычетаем четверть круга умножаем на 2

s_total = s_0_1 + s_1_2

if x_task_1 <= 1:
    sector_obj = SectorOneRadiusCircle(1 - x_task_1)
    long = 2 * sector_obj.height
    s_area_left = 2 * sector_obj.array_sector_del_array_triangle
    s_area_right = s_total - s_area_left
else:
    sector_obj = SectorOneRadiusCircle(2 - x_task_1)
    long = 2 - 2 * sector_obj.height
    '''   '''
    rect_by_right = 2 * ((2 - x_task_1) * 1)
    s_area_right = rect_by_right - (2 * math.pi * (radius ** 2) / 4 - 2 * sector_obj.array_sector_del_array_triangle)
    s_area_left = s_total - s_area_right
print()
print()
print('длинна           линии = ', round(long, 4))
print()
print('полная площадь   фигуры = ', round(s_total, 4))
print()
print('площадь слева  от линии =', round(s_area_left, 4))
print('площадь справа от линии =', round(s_area_right, 4))

print()
input('press enter to go ---------------------------------------------------> ')
############# 111 finish ################

########################################################################################################################

# ================================
#   Задание 2
# ================================
# Вычислить значения суммы ряда S при заданных с консоли начальном и конечном значениях
# аргумента x (x_nach, x_kon), шаге его изменения delta_x и точности вычислений eps.
# Вычисленные значения ряда сравнить со значениями заданной функции f(x). Результаты
# вычислений вывести в виде таблицы с заголовком.

# s = pi/2 + sum( ((-1)^(n+1))/((2*n + 1)*(x^2*n+1)) )
#  pi/2 +(-1/x + 1/3x^3 - 1/5x^5 + 1/7x^7 - 1/9x^9 + 1/11x^11 - 1/13x^13 .......)
# x > 1
##########
'''
    задача на отрезке 1: +infinity оределить значение              //  S(x) ~ arctang(x)
    - x_start       вводится с клавиатуры  начальная точка расчета //  x_start > 1
    - x_finish      вводится с клавиатуры  конечная точка расчета  //  x_finish => x_start > 1
    - delta_x       вводится с клавиатуры шаг измерений            //  x_finish - x_start => delta_x > 0
    - accuracy_calc вводится с клавиатуры  точности вычислений     //  +infinity > eps >= 0
    * получаем значение с клавиатуры проверяем валидность
    * задаем клас Builder - можно использовать в других задачах, можно было без него
    * генератор значений X + delta_x через yeld экономит память [x1, x1+dx, x1+2dx, x1+3dx, ..., x1+Ndx, x2]
    * разбиваем формулу на части часть1 + часть2 + .... + часитьN , (можно разбить на знаменатель числитель)
    * получаем список значений для каждого X выполняется суммирование элементов последовательности указанное коллчество
    * получаем эталонный список через arctang(x)
    * выводим в таблице (так же можно сохранять в csv файл, выводить через графический интерфейс tkinter)
'''

############# 222 start ################
print('\n' * 11)
print('Задача 2\n')
print('Вычислить значения суммы ряда S при заданных с консоли начальном и конечном значениях\n'
      'аргумента x (x_nach, x_kon), шаге его изменения delta_x и точности вычислений eps.\n'
      'Вычисленные значения ряда сравнить со значениями заданной функции f(x). Результаты\n'
      'вычислений вывести в виде таблицы с заголовком.\n')
print('# default \nx1 = 2\nx2 = 20 \ndelta_x = 1 \naccuracy_n = 45 \nнажать enter для задания дефолтных значений')
# default
x1 = 2
x2 = 20
delta_x = 1
accuracy_n = 45

import math


def is_number(str):
    ''' проверяем является ли число вещественным'''
    try:
        float(str)
        return True
    except ValueError:
        return False


while True:
    ''' получаем значения от пользователя проводим валидацию'''
    inp_value = input('введите через пробел X1, X2, delta_X, accuracy(точность) пример "2 44 0.5 78":  ')
    if inp_value == '':
        # default
        break
        pass
    list_inp = inp_value.split()
    if len(list_inp) != 4:
        print('error count variable')
        continue
    elif not is_number(list_inp[0]) and not is_number(list_inp[1]) and not is_number(list_inp[2]) and \
            not list_inp[3].isdigit():
        print('error variable not number')
        continue
    elif float(list_inp[0]) > float(list_inp[1]):
        print('error X1 > X2')
        continue
    elif float(list_inp[0]) <= 1:
        print('error X1 <= 1')
        continue
    elif float(list_inp[2]) <= 0:
        print('error delta_X <= 0')
        continue
    else:
        x1 = float(list_inp[0])
        x2 = float(list_inp[1])
        delta_x = float(list_inp[2])
        accuracy_n = int(list_inp[3])
        break

print(f'Ok  x1={x1}  x2={x2}  delta_x={delta_x} accuracy_n={accuracy_n}')


class Formula:
    ''' разбиваем формулу на части каждая часть как атрибут '''

    def __init__(self, kwargs: dict = None):
        for i, j in kwargs.items():
            setattr(self, i, j)


def get_x_plus_delta(x1, x2, delta_x):
    '''  аналог range допускает шаг [1, 100, 0.5-float] значения не сохраняет в памяти '''
    yield x1
    while x1 < x2:
        x1 = round(x1 + delta_x if x1 + delta_x < x2 else x2, 8)
        yield x1
    pass


part1 = round(math.pi / 2, 8)
part2 = lambda f_x, f_n: ((-1) ** (f_n + 1)) / ((2 * f_n + 1) * (f_x ** (2 * f_n + 1)))
part_in_dict = {'part1': part1, 'part2': part2}
formul = Formula(part_in_dict)

''' решение в одну строчку'''
######
# list_sol = ((x, formul.part1 + sum(map(formul.part2, (x for i in range(0, accuracy_n)), (range(0, accuracy_n)))))
#                                                                         for x in get_x_plus_delta(x1, x2, delta_x))
######

list_solution = []
list_arctang = []
for x in get_x_plus_delta(x1, x2, delta_x):
    value = formul.part1
    for j in range(0, accuracy_n):
        value += formul.part2(x, j)
    list_solution.append((x, value))
    list_arctang.append((x, math.atan(x)))

header = '{0:^20}|{1:^20}|{2:^20}|'.format('value X', 'formula', 'arctang')
division_line = '{0:-^20}|{0:-^20}|{0:-^20}|'.format('', '', '')
output_table = division_line + '\n' + header + '\n' + division_line + '\n'

for i in range(len(list_solution)):
    output_table += '{:^20}|{:^20}|{:^20}|'.format(list_solution[i][0], list_solution[i][1], list_arctang[i][1])
    output_table += '\n' + division_line + '\n'
print()
print(output_table)

print()
input('press enter to go ---------------------------------------------------> ')
############# 222 finish ################


########################################################################################################################

# ================================
#   Задание 3
# ================================
# Для заданного с консоли значения n определить сумму числового ряда:
# s =sum(1/ (n*(n+1)*(n+2) {where +infinity > n >= 1} // 1/(1*2*3) + 1/(2*3*4) + 1/(3*4*5) + ... + 1/(n*(n+1)*(n+2))
# Результаты вычислений вывести в виде таблицы с заголовком. Вычисленные значения
# ряда сравнить со значением функции
# f = 1/ 4  - функция прямая линия

##########
'''
    задача на отрезке [1:+infinity) находятся значения n,  задана формула получить, значение S(n) при вводе n 
    - n  вводится с клавиатуры  начальная точка расчета n=1/ конечная точка n=input('n')/ количество членов input('n') 
    * получаем значение с клавиатуры проверяем валидность
    * подставляем в формулу вычисляем
    * выводим в таблице (так же можно сохранять в csv файл, выводить через графический интерфейс tkinter)
'''

# ############## 333 start ###############
print('\n' * 11)
print('Задача 3\n')
print('Для заданного с консоли значения n определить сумму числового ряда:\n'
      's =sum(1/ (n*(n+1)*(n+2) {where +infinity > n >= 1} //1/(1*2*3)+1/(2*3*4)+1/(3*4*5)+..+1/(n*(n+1)*(n+2))\n'
      'Результаты вычислений вывести в виде таблицы с заголовком. Вычисленные значения\n'
      'ряда сравнить со значением функции\n'
      'f = 1/ 4  - функция прямая линия\n')
print('# default \ninp_n = 45\nнажать enter для задания дефолтных значений')
# default
inp_n = 45
while True:
    ''' получаем значения от пользователя проводим валидацию'''
    inp_value = input('введите целое положительное число n пример "78":  ')
    if inp_value == '':
        # default
        break
        pass
    list_inp = inp_value.split()
    if len(list_inp) != 1:
        print('error count variable')
        continue
    elif not list_inp[0].isdigit():
        print('error variable not number')
        continue
    elif int(list_inp[0]) < 1:
        print('error n < 1')
        continue
    else:
        inp_n = int(list_inp[0])
        break

print(f'Ok  inp_n={inp_n}')

solution_task2 = []
for i in range(1, inp_n + 1):
    value = 1 / (i * (i + 1) * (i + 2))
    solution_task2.append((i, value))

count_task2 = sum(x[1] for x in solution_task2)

header = '{0:^20}|{1:^20}|{2:^20}|'.format('number N', 'formula', 'f = 1/4')
division_line = '{0:-^20}|{0:-^20}|{0:-^20}|'.format('', '', '')
output_table = division_line + '\n' + header + '\n' + division_line + '\n'
output_table += f'{inp_n:^20}|{count_task2:^20}|{1 / 4:^20}|' + '\n' + division_line + '\n'
print()
print()
print(output_table)

print()
input('press enter to go ---------------------------------------------------> ')
############# 333 finish ################


########################################################################################################################

# ================================
#   Задание 4
# ================================
# Числовая последовательность задана рекуррентной формулой
# Задать с консоли два первых члена последовательности 1 a и 2 a . Найти первые n членов
# последовательности и их сумму.
# Результаты вычислений вывести в виде таблицы с заголовком.

# a.k+2 = ( a.k+1 + (a.k)^1/2 )^1/2
# Задать a.1, a.2
#############
'''
    задача получить от пользователя a1, a2, n  вычислить элементы рекурентной послед. вывести сумму 
    - a1 вводится с клавиатуры  a1>=0
    - a2 вводится с клавиатуры  a2>=0
    - n  вводится с клавиатуры  целое число от 0 до +inf()

    * получаем значение a1, a2, n с клавиатуры проверяем валидность
    * подставляем в формулу вычисляем elements  
    * выводим в таблице (так же можно сохранять в csv файл, выводить через графический интерфейс tkinter)
'''

# ############# 444 start ################
print('\n' * 11)
print('Задача 4\n')
print('Числовая последовательность задана рекуррентной формулой\n'
      'Задать с консоли два первых члена последовательности 1 a и 2 a . Найти первые n членов\n'
      'последовательности и их сумму.\n'
      'Результаты вычислений вывести в виде таблицы с заголовком.\n'
      'a.k+2 = ( a.k+1 + (a.k)^1/2 )^1/2\n'
      'Задать a.1, a.2\n')
print('# default \na_1 = 45\na_2 = 78\ncount_n_items = 10\nнажать enter для задания дефолтных значений')

# default
a_1 = 45
a_2 = 78
count_n_items = 10


def is_number(str):
    ''' проверяем является ли число вещественным'''
    try:
        float(str)
        return True
    except ValueError:
        return False


while True:
    ''' получаем значения от пользователя проводим валидацию'''
    inp_value = input('введите a1>0 , a2>0, n  целое положительное число n пример "1 3 98":  ')
    if inp_value == '':
        # default
        break
        pass
    list_inp = inp_value.split()
    if len(list_inp) != 3:
        print('error count variable')
        continue
    elif not is_number(list_inp[0]) and not is_number(list_inp[1]) and not list_inp[0].isdigit():
        print('error variable not number')
        continue
    elif float(list_inp[0]) < 0 and float(list_inp[1]) < 0:
        print('error X1 < 0 or X2 < 0')
        continue
    else:
        a_1 = float(list_inp[0])
        a_2 = float(list_inp[1])
        count_n_items = int(list_inp[2])
        break

print(f'Ok  a_1={a_1}  a_2={a_2} count_n_items={count_n_items}')
list_elements = [a_1, a_2]


def recurrent_recursia():
    ''' max recursia 1000 параметр можно увеличить'''
    if len(list_elements) - 2 < count_n_items:
        list_elements.append((list_elements[-1] + (list_elements[-2]) ** (1 / 2)) ** (1 / 2))
        recurrent_recursia()
    pass


recurrent_recursia()
print(list_elements)
sum_elements = sum(list_elements)

header = '{0:^20}|{1:^20}|{2:^20}|{3:^20}|'.format('number N', 'a_1', 'a_2', 'sum')
division_line = '{0:-^20}|{0:-^20}|{0:-^20}|{0:-^20}|'.format('', '', '', '')
body_table = f'{count_n_items + 2:^20}|{a_1:^20}|{a_2:^20}|{sum_elements:^20}|'
footer_table = None

output_table = division_line + '\n' + header + '\n' + division_line + '\n'
output_table += body_table + '\n' + division_line + '\n'

print()
print(output_table)

# footer_table = None

print()
input('press enter to go ---------------------------------------------------> ')
# ############# 444 finish  ################


########################################################################################################################

# ================================
#   Задание 5
# ================================
# Ввести две строки, состоящие только из нулей и единиц. Считая их изображениями двоичных
# чисел, сложить их и вывести сумму на экран в двоичной и десятичной системах счисления.
# Исходные слагаемые в десятичную систему счисления не преобразовывать.
#
# Входные данные:
# 100101
# 0111
# Выходные данные:
# 101100
# 44

'''
    задача получить от пользователя v1, v2 произвести суммирование
    - v1 вводится с клавиатуры  v1 принадлежит [0,1]
    - v2 вводится с клавиатуры  v2 принадлежит [0,1]

    * получаем значение v1, v2, n с клавиатуры проверяем валидность состоит из 0 и 1
    * привести к одинаковой разрядности
    * привести сложение в двоичном формате
    * перевести в десятичную систему 
          #* выводим в таблице (так же можно сохранять в csv файл, выводить через графический интерфейс tkinter)
'''

############# 555 start  ################
print('\n' * 11)
print('Задача 5\n')
print('Ввести две строки, состоящие только из нулей и единиц. Считая их изображениями двоичных\n'
      'чисел, сложить их и вывести сумму на экран в двоичной и десятичной системах счисления.\n'
      'Исходные слагаемые в десятичную систему счисления не преобразовывать.\n'
      'Входные данные:\n'
      '100101\n'
      '0111\n'
      'Выходные данные:\n'
      '101100\n'
      '44\n')
print('# default \nvariable_str_1 = "11110011"\nvariable_str_2 = "1100001"\n'
      '\nнажать enter для задания дефолтных значений')
# default
variable_str_1 = '11110011'
variable_str_2 = '1100001'

while True:
    ''' получаем значения от пользователя проводим валидацию'''
    inp_value = input('введите v1, v2 число состоит из 0 и 1 пример "100101":  ')
    if inp_value == '':
        # default
        break
        pass
    list_inp = inp_value.split()
    if len(list_inp) != 2:
        print('error count variable')
        continue
    elif not all(map(lambda x: x in ['0', '1'], list_inp[0] + list_inp[1])):
        print('error v1 or v2 not is [0, 1]')
        continue
    else:
        variable_str_1, variable_str_2 = list_inp
        break

print(f'Ok  v1={variable_str_1}  v2={variable_str_2}')


def convert_list_int(str: str):
    return list(map(lambda x: int(x), str))
    pass


variable_1, variable_2 = convert_list_int(variable_str_1), convert_list_int(variable_str_2)
var_support = [0] * (len(variable_1) + 1) if len(variable_1) >= len(variable_2) else [0] * (len(variable_2) + 1)


def equ_len_1_and_2(list: list):
    return ([0] * (len(var_support) - len(list)) + list)
    pass


variable_2 = equ_len_1_and_2(variable_2)
variable_1 = equ_len_1_and_2(variable_1)

summer_list = list(list(j) for j in zip(variable_1, variable_2, var_support))
finally_list = []
'''обрабатываем полученный список'''
for j, i in enumerate(summer_list[::-1]):
    # print(all([i[0], i[2]]), i[0], i[2])
    '''это работает но стоит переделать'''
    if all(i):
        summer_list[len(summer_list) - 2 - j][2] = 1
        finally_list.append(1)
        pass
    elif all(i[:2]) or all(i[1:]) or all([i[0], i[2]]):
        summer_list[len(summer_list) - 2 - j][2] = 1
        finally_list.append(0)
        pass
    elif any(i):
        finally_list.append(1)
        pass
    elif not any(i):
        finally_list.append(0)
        pass
    else:
        print('same error')

finally_list.reverse()
finaly_int_to_str = ''.join(str(i) for i in finally_list)
output_b_num = finaly_int_to_str[finaly_int_to_str.find('1'):]

print()
print(f'binary format v1={variable_str_1} v2={variable_str_2} = {output_b_num}')
print()
### part2
decimal_numb = sum(2 ** x for x, j in enumerate(output_b_num[::-1]) if j == '1')
print(f'decimal format v1={variable_str_1} v2={variable_str_2} = {decimal_numb}')

print()
input('press enter to go ---------------------------------------------------> ')
############# 555 finish ################


########################################################################################################################

# ================================
#   Задание 6
# ================================
# Строка представляет собой последовательность слов, разделенных пробелом. Удалить из нее
# все повторения слов. Рабочие строки не использовать.
# Входные данные:
# abcde fghik abcde lmnop fghi
# Выходные данные:
# abcde fghik lmnop fghi

'''
    задача строки удалить посторяющиеся слова

    --------------- УТОЧНИТЕ ---------------
    ЧТО ОЗНАЧАЕТ Рабочие строки не использовать ???
'''

############# 666 start  ################
print('\n' * 11)
print('Задача 6\n')
print('Строка представляет собой последовательность слов, разделенных пробелом. Удалить из нее\n'
      'все повторения слов. Рабочие строки не использовать.\n'
      'Входные данные:\n'
      'abcde fghik abcde lmnop fghi\n'
      'Выходные данные:\n'
      'abcde fghik lmnop fghi\n'
      'УДАЛЕНИЕ ДУБЛЕЙ СНАЧАЛА СТРОКИ (МОЖНО ИСПРАВИТЬ, УДАЛЕНИЕ С КОНЦА)')
print('# default \nstr_input = "abcde fghik abcde lmnop fghi"\n'
      'нажать enter для задания дефолтных значений')

# default
str_input = 'abcde fghik abcde lmnop fghi'
while True:
    ''' получаем значения от пользователя проводим валидацию'''
    user_input = input('введите строку пример "abcde fghik abcde lmnop fghi":  ')
    if user_input == '':
        # default
        break
    else:
        str_input = user_input
        break

# первый вариант решения который попросили исправить
# ''' может измениться последовательность слов'''
# print(f'Ok input string = "{str_input}"')
# print()
# print(f'Ok output string = {" ".join(set(str_input.split()))}')

### исправленный вариант
# ---> 06.02.2020
# приводим полученную строку к списку
list_input_task6 = str_input.split()

# приводим список к множеству удаляем повторы
set_input_task6 = set(list_input_task6)

# получаем список дублей из списка удаляем множество
list_double_task6 = list_input_task6[:]
[list_double_task6.remove(i) for i in set_input_task6]

# из списка удаляем элементы списка дублей
total_list_task6 = list_input_task6[:]
[total_list_task6.remove(i) for i in list_double_task6]
total_list_task6 = ' '.join(total_list_task6)
# <--- 06.02.2020

print()
print()
print('Входная  строка:   ', str_input)
print('Выходная строка:   ', total_list_task6)

print()
input('press enter to go ---------------------------------------------------> ')
############# 666 finish ################

########################################################################################################################

# ================================
#   Задание 7
# ================================
# В целочисленном векторе vectorn найти первый по порядку отрицательный и последний
# положительный элементы и поменять их местами. Предусмотреть случай, когда все
# элементы вектора одного знака.
# Входные данные:
# n=10
# v_min=-5
# v_max=10
# Исходный вектор:
# 7 3 1 -5 -2 5 2 0 10 -1
# Выходные данные:
# first_otr=-5 n_first_otr=4
# last_pol=10 n_last_pol=9
# Выходной вектор:
# 7 3 1 10 -2 5 2 0 -5 -1

'''
    задача найти в последовательности 1-е вхождение отрицательного числа последнее вхождение положительного их индекс

    ---------------  ---------------

    Каким типом даных задается вектор (str, tuple, list)???
'''
############# 777 start  ################
print('\n' * 11)
print('Задача 7\n')
print('В целочисленном векторе vectorn найти первый по порядку отрицательный и последний\n'
      'положительный элементы и поменять их местами. Предусмотреть случай, когда все\n'
      'элементы вектора одного знака.\n'
      'Входные данные:\n'
      'n=10\n'
      'v_min=-5\n'
      'v_max=10\n'
      'Исходный вектор:\n'
      '7 3 1 -5 -2 5 2 0 10 -1\n'
      'Выходные данные:\n'
      'first_otr=-5 n_first_otr=4\n'
      'last_pol=10 n_last_pol=9\n'
      'Выходной вектор:\n'
      '7 3 1 10 -2 5 2 0 -5 -1\n')
print('# default \nvector_input = "7 3 1 -5 -2 5 2 0 10 -1"\n'
      'нажать enter для задания дефолтных значений\n')

# default
vector_input = '7 3 1 -5 -2 5 2 0 10 -1'

import re

while True:
    ''' получаем значения от пользователя проводим валидацию'''
    """ валидацию не провожу на  7-5--4++1 - 4 -+ и т.п ЕСЛИ НАДО допишу код! """
    user_input = input('введите vector строку пример "7 3 1 -5 -2 5 2 0 10 -1":  ')
    if user_input == '':
        # default
        break
    elif not all(map(lambda x: x in '-+ ' or x.isdigit(), user_input)):
        print('error char')
        continue
        pass
    else:
        vector_input = user_input
        break

'''ищем первое  отрицательного число в последовательности'''
negative_number = re.search(r'-[1-9]+\d*', vector_input)
'''приводим строку к списку'''
vector_list = vector_input.split()
'''находим индекс числа в списке + 1 в человеческой форме если число не None'''
if negative_number:
    index_negative_number = vector_list.index(negative_number.group()) + 1
else:
    index_negative_number = None

'''разворачиваем список находим первое положительное число'''
vector_list.reverse()
positive_number = re.search(r'(?<![-])\b[1-9]+[\d]*', ' '.join(vector_list))
'''находим индекс в списке в человеческой форме ищем в развернутом списке инвертируем число если число не None'''
if positive_number:
    index_positive_number = len(vector_list) - vector_list.index(positive_number.group())
else:
    index_positive_number = None

'''разворачиваем список'''
vector_list.reverse()

'''меняем местами негатив чесло начала с полож конца'''
print('vector_list = ', vector_list)
if index_positive_number and negative_number:
    vector_list[index_negative_number - 1], vector_list[index_positive_number - 1] = positive_number.group(), \
                                                                                     negative_number.group()
    '''выводим на экран'''
    print()
    print('человеческая форма index_negative_number =', index_negative_number)
    print('человеческая форма index_positive_number =', index_positive_number)
    print()
    print('vector_sting = ', ' '.join(vector_list))
else:
    print('все положительные или отрицательные или нули')

print()
input('press enter to go ---------------------------------------------------> ')
############# 777 finish ################


########################################################################################################################

# ================================
#   Задание 8
# ================================
# В заданном k-м слое элементов целочисленного прямоугольного массива matrixnm сдвинуть
# все элементы на p шагов по часовой стрелке. Номер слоя k и количество шагов p задать с
# консоли.
# Входные данные для n=4, m=5, k=2, p=2:
# v_min=-20
# v_max=10
# Исходный массив:
#    7    -2   -11     3    -5
#    5     2     0    10     1
#  -15     9   -12     8   -18
#    0   -10     9   -13     4
# Выходной массив:
#    7    -2   -11     3    -5
#    5   -12     9     2     1
#  -15     8    10     0   -18
#    0   -10     9   -13     4

'''
    задача дан прямоугольный массив, задается k номер слоя и p количество шагов, сдвигается слой по часовой стрелке
    - задается прямоугольный массив вида [[a1, a2, .., an], [b1, b2, .., bn], ... ,[m1, m2, .., mn]]
    - k вводится с клавиатуры  k принадлежит [1, размерность матрицы]
    - p вводится с клавиатуры  p принадлежит [0,+inf()]

    a1 a2 a3 a4 a5 a6 
    b1 b2 b3 b4 b5 b6 
    c1 c2 c3 c4 c5 c6 
    d1 d2 d3 d4 d5 d6 
    e1 e2 e3 e4 e5 e6 

    2 слой КАК Я ПОНЯЛ

    a1 a2 a3 a4 a5 a6 

    b1 *->*->*->*  b6 
       ^        |
    c1 |  c3 c4 |  c6 
       |        v 
    d1 *<-*<-*<-*  d6 

    e1 e2 e3 e4 e5 e6 


            * получаем значение v1, v2, n с клавиатуры проверяем валидность состоит из 0 и 1
            * привести к одинаковой разрядности
            * привести сложение в двоичном формате
            * перевести в десятичную систему 
            #* выводим в таблице (так же можно сохранять в csv файл, выводить через графический интерфейс tkinter)


'''

############# 888 start  ################
print('\n' * 11)
print('Задача 8\n')
print('В заданном k-м слое элементов целочисленного прямоугольного массива matrixnm сдвинуть\n'
      'все элементы на p шагов по часовой стрелке. Номер слоя k и количество шагов p задать с\n'
      'консоли.\n'
      'Входные данные для n=4, m=5, k=2, p=2:\n'
      'v_min=-20\n'
      'v_max=10\n'
      'Исходный массив:\n'
      '   7    -2   -11     3    -5\n'
      '   5     2     0    10     1\n'
      ' -15     9   -12     8   -18\n'
      '   0   -10     9   -13     4\n'
      'Выходной массив:\n'
      '   7    -2   -11     3    -5\n'
      '   5   -12     9     2     1\n'
      ' -15     8    10     0   -18\n'
      '   0   -10     9   -13     4\n')
print('# default \nmatrix_input = "7, -2, -11, 3, -5/ 5, 2, 0, 10, 1/ -15, 9, -12, 8, -18/ 0, -10, 9, -13, 4"\n'
      'k = 2\np = 2\nнажать enter для задания дефолтных значений\n')
print('номер слоя вводится в человеческой форме 1-n 0-нет слоя')
print()
# print(
#    'копировать от сюда чтобы не ошибиться при вводе 10x10\n 1a, 2a, 3a, 4a, 5a, 6a, 7a, 8a, 9a, 0a/
#    1b, 2b, 3b, 4b, 5b, 6b, 7b, 8b, 9b, 0b/1c, 2c, 3c, 4c, 5c, 6c, 7c, 8c, 9c, 0c/
#    1d, 2d, 3d, 4d, 5d, 6d, 7d, 8d, 9d, 0d/1e, 2e, 3e, 4e, 5e, 6e, 7e, 8e, 9e, 0e/
#    1f, 2f, 3f, 4f, 5f, 6f, 7f, 8f, 9f, 0f/1g, 2g, 3g, 4g, 5g, 6g, 7g, 8g, 9g, 0g/
#    1h, 2h, 3h, 4h, 5h, 6h, 7h, 8h, 9h, 0h/1i, 2i, 3i, 4i, 5i, 6i, 7i, 8i, 9i, 0i/
#    1j, 2j, 3j, 4j, 5j, 6j, 7j, 8j, 9j, 0j')
print()
print()
import copy


class MovePartMatrix:
    def __init__(self, string: str = None):
        self.string = string
        self.list = [i.split(',') for i in self.string.split('/')]

    def __call__(self, layer: int = 0, step: int = 2) -> object:
        '''
         получаем верхний уровень, нижний уровень, средний уровень
              преобразовываем
          *cut*_1a 2a 3a 4a 5a  top
                1b          5b     center
                1c          5c     string
                1m 2m 3m 4m 5m         bottom

                в список   (top) 1a 2a 3a 4a 5a + (right)5b 5c  + (revers_bottom)5m 4m 3m 2m 1m + (revers_left)1c 1b
                перемещаем элементы по часовой стрелке на N шагов
                разбираем список в обратном  порядке возврящаем измененные элементы в исходный список
        '''

        '''верхняя, нижняя, левая, правая граница'''
        list_copy = copy.deepcopy(self.list)
        strip_start = layer - 1
        strip_finish = -layer

        # выбран средний нечетный столбец или строка (одна строка в матрице)
        # ---> 06.02.2020
        # '''ДОРАБОТКА кода введена одна строка'''
        if layer > len(list_copy) / 2 or layer > len(list_copy[0]) / 2:
            # проверить одна строка в матрице
            if len(list_copy) == 1:
                # шаг нечетный чтобы не вращать по кругу длинна / 2 больше слоя не трогать 1 централ элем
                if step % 2 == 1 and layer < (len(list_copy[0]) + 1) / 2 and layer != 0:
                    list_copy[0][layer - 1], list_copy[0][-layer] = list_copy[0][-layer], list_copy[0][layer - 1]
                    matrix_move_finally = list_copy
                    matrix_move_finally_str = '/'.join([','.join(i) for i in matrix_move_finally])
                    return MovePartMatrix(matrix_move_finally_str)
                print('Не перемещается т.к. шаг четное число перемещение по кругу')
                print('Или слой указан больше чем длинна деленая попалам (один центральный эл. или отсутствие слоя)')
                matrix_move_finally = list_copy
                matrix_move_finally_str = '/'.join([','.join(i) for i in matrix_move_finally])
                return MovePartMatrix(matrix_move_finally_str)
                pass
            # проверить центральная строка в матрице
            elif layer > len(list_copy) / 2:
                # шаг нечетный чтобы не вращать по кругу длинна / 2 больше слоя не трогать 1 централ элем
                if step % 2 == 1 and layer != 0 and layer == (len(list_copy) + 1) / 2:
                    list_copy[layer - 1][layer - 1], list_copy[layer - 1][-layer] = list_copy[layer - 1][-layer], \
                                                                                    list_copy[layer - 1][layer - 1]
                    matrix_move_finally = list_copy
                    matrix_move_finally_str = '/'.join([','.join(i) for i in matrix_move_finally])
                    return MovePartMatrix(matrix_move_finally_str)
                print('Не перемещается т.к. шаг четное число перемещение по кругу')
                print('Или слой указан больше чем длинна деленая попалам (один центральный эл. или отсутствие слоя)')
                matrix_move_finally = list_copy
                matrix_move_finally_str = '/'.join([','.join(i) for i in matrix_move_finally])
                return MovePartMatrix(matrix_move_finally_str)
                pass
            # проверить центральный столбец в матрице
            elif layer > len(list_copy[0]) / 2:
                # шаг нечетный чтобы не вращать по кругу длинна / 2 больше слоя не трогать 1 централ элем
                if step % 2 == 1 and layer != 0 and layer == (len(list_copy[0]) + 1) / 2:
                    list_copy[layer - 1][layer - 1], list_copy[-layer][layer - 1] = list_copy[-layer][layer - 1], \
                                                                                    list_copy[layer - 1][layer - 1]
                    matrix_move_finally = list_copy
                    matrix_move_finally_str = '/'.join([','.join(i) for i in matrix_move_finally])
                    return MovePartMatrix(matrix_move_finally_str)
                print('Не перемещается т.к. шаг четное число перемещение по кругу')
                print('Или слой указан больше чем длинна деленая попалам (один центральный эл. или отсутствие слоя)')
                matrix_move_finally = list_copy
                matrix_move_finally_str = '/'.join([','.join(i) for i in matrix_move_finally])
                return MovePartMatrix(matrix_move_finally_str)
                pass
            else:
                print('что то пошло не так')
                return MovePartMatrix(self.string)
                pass
            # <--- 06.02.2020
        else:
            '''верхняя строка'''
            list_layer_top = list_copy[strip_start][strip_start: len(list_copy[0]) + strip_finish + 1]
            '''нижняя строка развернутая'''
            list_layer_bottom = list_copy[strip_finish][strip_start: len(list_copy[0]) + strip_finish + 1]
            list_layer_bottom.reverse()
            len_list_top_bottom = len(list_layer_top)

            '''среднии сроки их левый(развернут) и правый элемент'''
            list_layer_body = [[j[strip_start], j[strip_finish]] for j in list_copy[strip_start + 1: strip_finish]]
            if list_layer_body:
                border_left, border_right = zip(*list_layer_body)
                border_right = list(border_right)
                border_left = list(border_left)
                border_left.reverse()
                len_list_left_right = len(border_right)
            else:
                border_right = []
                border_left = []
                len_list_left_right = 0

            '''список сдвигаемых элементов'''
            list_delta = list_layer_top + border_right + list_layer_bottom + border_left
            '''сдвигаем элементы'''
            step = step % len(list_delta)  # больше одного оборота
            list_move_element = list_delta[-step:] + list_delta[:-step]

            '''разбираем список в обратном  порядке возврящаем измененные элементы в исходный список'''
            list_layer_top_finally = list_move_element[:len_list_top_bottom]
            list_move_element[:len_list_top_bottom] = []
            list_layer_right_finally = list_move_element[:len_list_left_right]
            list_move_element[:len_list_left_right] = []
            list_layer_bottom_finally = list_move_element[:len_list_top_bottom]
            list_move_element[:len_list_top_bottom] = []
            list_layer_left_finally = list_move_element[:len_list_left_right]
            ''' разворачиваем элементы left bottom чтобы корректно внести'''
            list_layer_bottom_finally.reverse()
            list_layer_left_finally.reverse()
            ''' вносим элементы в итоговую таблицу'''
            matrix_move_finally = list_copy[:]
            matrix_move_finally[strip_start][strip_start: len(list_copy[0]) + strip_finish + 1] = \
                list_layer_top_finally

            matrix_move_finally[strip_finish][strip_start: len(list_copy[0]) + strip_finish + 1] = \
                list_layer_bottom_finally
            ''' центр '''
            body_left_right = list(zip(list_layer_left_finally, list_layer_right_finally))
            for j, i in zip(matrix_move_finally[strip_start + 1: strip_finish], body_left_right):
                j[strip_start] = i[0]
                j[strip_finish] = i[1]

            matrix_move_finally_str = '/'.join([','.join(i) for i in matrix_move_finally])
            return MovePartMatrix(matrix_move_finally_str)
            pass

    def __str__(self) -> str:
        list_mat_to_format = ''.join(['{' + str(j).strip() + ':>8}|' for j in range(len(self.list[0]))]) + '\n'
        return ''.join(list_mat_to_format.format(*i) for i in self.list)
        pass


# default
# 6x3  1, 2, 3, 3/4, 5, 6, 3/7, 8, 9, 3/01, 02, 03, 3/04, 05, 06, 3/07, 08, 09, 3/
# 6x3  1, 2, 3/4, 5, 6/7, 8, 9/01, 02, 03/04, 05, 06/07, 08, 09/
# 5x6  1, 2, 3, 4, 5, 6/1, 2, 3, 4, 5, 6/1, 2, 3, 4, 5, 6/1, 2, 3, 4, 5, 6/1, 2, 3, 4, 5, 6/
# 3x6  1, 2, 3, 4, 5, 6/1, 2, 3, 4, 5, 6/1, 2, 3, 4, 5, 6/
# 3x5  1, 2, 3, 4, 5/1, 2, 3, 4, 5/1, 2, 3, 4, 5/
# 1x5  1, 2, 3, 4, 5/
# 1x6  1, 2, 3, 4, 5, 6/
# 1x9  1, 2, 3, 4, 5, 6, 7, 8, 9/
matrix_input = '7, -2, -11, 3, -5/ 5, 2, 0, 10, 1/ -15, 9, -12, 8, -18/ 0, -10, 9, -13, 4'
k_input = 2
p_input = 2
k_input_print = k_input
p_input_print = p_input
while True:
    ''' получаем значения от пользователя либо все, либо ни одного валидацию НЕ ПРОВОЖУ (при необх. могу доработать)'''
    print('Вводятся все значения или ни одного(дефолт) иначе цикл вернет в начало \n '
          'можно скопировать от сюда \n 7, -2, -11, 3, -5/ 5, 2, 0, 10, 1/ -15, 9, -12, 8, -18/ 0, -10, 9, -13, 4')
    user_matrix_input = input('введите матрицу в формате: a1, a2, .., an/ b1, b2, .., bn/ ... / m1, m2, .., mn:  ')
    user_k_input = input('введите положительное часло >=1, но меньше ш/2 или в/2  k слой матрицы пример 3 (Вм6, Шм8): ')
    user_p_input = input('введите положительное часло >=0 p количество шагов пример 4: ')
    if all((user_matrix_input == '', user_k_input == '', user_p_input == '')):
        # default
        break
    elif any((user_matrix_input == '', user_k_input == '', user_p_input == '')):
        # default
        print('error value')
        continue
    elif not user_k_input.isdigit() or not user_p_input.isdigit():
        print('error value k or p')
        continue
    else:
        '''ДОРАБОТКА кода от ошибки copy-paste'''
        # ---> 06.02.2020
        user_matrix_input = user_matrix_input.strip()
        if user_matrix_input[-1] == '/':
            user_matrix_input = user_matrix_input[:-1]
        # <--- 06.02.2020

        matrix_inlist = [i.split(',') for i in user_matrix_input.split('/')]
        matrix_input = user_matrix_input

        k_input = int(user_k_input)
        p_input = int(user_p_input)
        break

matrix = MovePartMatrix(matrix_input)
print()
print()
print('Какой   слой  двигаем    : ', k_input)
print('На какое количество шагов: ', p_input)
print()
print(matrix)
print('-------------------------------------------------------')
print()
output_matrix = matrix(k_input, p_input)
print(output_matrix)

print()
input('press enter  to end -----------------------------------------------------> ')
############# 888 finish ################

# ---------------------------------------------------------------------------------------------------------------------#
# if __name__ == '__main__':
#     # root = Main()
#     # root.mainloop()
#     # main()
#     pass


# # '''делаем глубокую копию т.к список изменяемая посоедовательность (x, y = y, x может не сработать)'''
###### d posetive '(?<![-.])\b[0-9]+\b(?!\.[0-9])'
######(?=…) положительный просмотр вперед
######(?!…) отрицательный просотр вперед

######(?<=…) - положительный просмотр назад
######(?<!…) - отрицательный просотр назад
