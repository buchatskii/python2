# Задача 30
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# num3 = int(input("Введите третье число: "))
# mass = [num1]
# count = 1
# number = 0
# while count < num3:
#     number = mass[-1] + num2
#     count += 1
#     mass.append(number)
# print(mass)

# Задача 32
# mass = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, -2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# num1 = int(input("Введите минимум: "))
# num2 = int(input("Введите максимум: "))
# start = 0
# for i in mass:
#     if num1 < i < num2:
#         if mass.count(i) > 1:
#             print(mass.index(i, start, len(mass)))
#         else:
#             print(mass.index(i))
#     start += 1