# Напишите программу, которая принимает на вход число N и
#  выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ]
#  (1, 1*2, 1*2*3, 1*2*3*4)

def main():
    n_number = int(input('Введите число: '))
    factorial = 1
    factorial_list = []
    for i in range(1, n_number + 1):
        factorial *= i

        factorial_list.append(factorial)

    print("Факториал числа: ", n_number, 'равен', factorial_list)


main()
