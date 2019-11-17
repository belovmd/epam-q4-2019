# 1 Создайте декоратор, который хранит в себе результаты вызовов функции
# и время получения результата за время запуска программы.
import time

global reclist
reclist = []


def eto_moy_decorator(func):
    def obertochka(number):
        print('Входной параметр = ', number + 1)
        starttime = time.time()
        func(number)
        endtime = time.time()
        result_of_call = 'Итог = ' + str(func(number)) + '  ' + \
                         'Время вызова = ' + str(endtime - starttime)
        reclist.append(result_of_call)

    return obertochka


@eto_moy_decorator
def square(number=3):
    """Возведение в квадрат с задержкой"""
    time.sleep(1)
    result = pow(number + 1, 2)
    return result


for input_number in range(6):
    square(input_number)
    print(reclist[input_number])


# 2 Реализовать функцию get_ranges которая получает на вход непустой список
# неповторяющихся целых чисел, отсортированных по возрастанию,
# которая этот список “сворачивает”
def get_ranges(input_list):
    cnt = 0
    output_list = []
    range_start = 0
    range_end = -1
    final_string = ''
    while cnt < len(input_list):
        if cnt == 0 or input_list[cnt] - input_list[cnt - 1] > 1:
            range_start = cnt
        if cnt == len(input_list) - 1 or input_list[cnt + 1] - \
                input_list[cnt] > 1:
            range_end = cnt
        if range_start == range_end:
            output_list.append(str(input_list[range_start]))
        if range_start < range_end:
            output_list.append(str(input_list[range_start]) + '-' +
                               str(input_list[range_end]))
        cnt += 1
    return output_list


print("Итоговый лист:", get_ranges([2, 3, 6, 8, 9, 10, 11, 13, 17, 18]))
print("Итоговый лист:", get_ranges([2, 4, 6, 8, 9, 10, 11, 13, 14, 18]))
