# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


number = int(input('Введите число больше 0: '))
total = 0
for i in range(number):
    total = total + number % 10
    number = number // 10

print("общая сумма равна", total)