# Задача 1
# import random
#
# number = int(input("Введите количество арбузов для сравнения массы: "))
# random_list = []
# count = 1
# while count <= number:
#     random_list.append(random.randrange(1, 10))
#     count += 1
# print(random_list)
# i_min = random_list[0]
# i_max = random_list[0]
# for i in random_list:
#     if i < i_min:
#         i_min = i
#     elif i > i_max:
#         i_max = i
#     else:
#         continue
# print(i_min, i_max)

# Задача 2
# import random
#
# number = int(input("Введите количество монеток: "))
# random_list = []
# count = 1
# count_1 = 0
# while count <= number:
#     random_list.append(random.randrange(0, 2))
#     count += 1
# print(random_list)
# random_list.count(1)  # Решка
# random_list.count(0)  # Орел
#
# if random_list.count(1) > random_list.count(0):
#     for i in random_list:
#         if i == 0:
#             count_1 += 1
#     print(count_1)
# elif random_list.count(1) < random_list.count(0):
#     for i in random_list:
#         if i == 1:
#             count_1 += 1
#     print(count_1)
# else:
#     print(random_list.count(1))

# Задача 3
sum = int(input())
mul = int(input())
for i in range(sum):
    for j in range(mul):
        if sum == i + j and mul == i * j:
            print(i, j)



# Задача 4

#number = int(input("Число: "))
#count = 0
#while count < number:
#    dva_k = count ** 2
#    if dva_k < number:
#        print(count)
#    else:
#        break
#    count += 1


