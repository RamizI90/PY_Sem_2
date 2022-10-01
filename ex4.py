#Реализуйте алгоритм перемешивания списка.

import random
def main():
    my_list = [9, 1, 0, 2, 8, 6, 7, 4, 5, 3]
    print('Первоначальный порядок: ', my_list)

    my_list.sort()
    print('Отсортированный порядок: ', my_list)

    random.shuffle(my_list)
    print('Перемешанный список', my_list)

    my_list.reverse()
    print('Инвертированный порядок: ', my_list)

main()
