"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции
"""

number = input("Введите целое положительное число: ")

biggest = int(number[0])
i = 1
while i < len(number):
    if biggest < int(number[i]):
        biggest = int(number[i])
    i = i + 1

print(f"В числе {number} самая большая цифра {biggest}")
