# 1 Создайте декоратор, который хранит в себе результаты вызовов функции
# и время получения результата за время запуска программы.
import time

global reclist
reclist = []
global call_number
call_number = 0


def eto_moy_decorator(func):
    """Декорирование функций с разным набором входных параметров"""
    def obertochka(*args, **kwargs):
        global call_number
        call_number += 1
        print('Вызов', call_number)
        print('Входные параметры', args, kwargs)
        start_time = time.time()
        end_time = time.time()
        result_of_call = ('Итог = ' + str(func(*args, **kwargs)) + '  '
                          + 'Время вызова = ' + str(end_time - start_time))
        reclist.append(result_of_call)

    return obertochka


@eto_moy_decorator
def square(number=3):
    """Возведение в квадрат с задержкой"""
    result = pow(number, 2)
    return result


for input_number in range(6):
    square(input_number)
    print(reclist[input_number])


# 2 Реализовать функцию get_ranges которая получает на вход непустой список
# неповторяющихся целых чисел, отсортированных по возрастанию,
# которая этот список “сворачивает”
def get_ranges(input_list):
    """Свертка входного листа в выходной с интервалами"""
    index = 0
    output_list = []
    range_start = 0
    range_end = -1
    while index < len(input_list):
        if index == 0 or input_list[index] - input_list[index - 1] > 1:
            range_start = index
        if index == (len(input_list) - 1) or (
                input_list[index + 1] - input_list[index] > 1):
            range_end = index
        if range_start == range_end:
            output_list.append(str(input_list[range_start]))
        if range_start < range_end:
            output_list.append(str(input_list[range_start]) + '-' +
                               str(input_list[range_end]))
        index += 1
    return output_list


print("Итоговый лист:", get_ranges([2, 3, 6, 8, 9, 10, 11, 13, 17, 18]))
print("Итоговый лист:", get_ranges([-3, -1, 0, 1, 6, 8, 9, 10, 11, 13, 14, 18]))