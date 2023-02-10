# Задача 22
import random
num_1 = 6
num_2 = 10
random_list_1 = []
random_list_2 = []
count = 1
count_2 = 1
while count <= num_1:
    random_list_1.append(random.randrange(1, 10))
    count += 1
random_list_1.sort()
print(random_list_1)
while count_2 <= num_2:
    random_list_2.append(random.randrange(1, 10))
    count_2 += 1
random_list_2.sort()
print(random_list_2)
c = set(random_list_1) & set(random_list_2)
print(sorted(c))

# Задача 24
# number = int(input("Введите размер списка: "))
# spam = list(range(1, number + 1))
# print(spam)
# pid = 0
# for i in spam:
#     if i == number:
#         pid += (i - 1) + spam[0] + i
#       print(pid)
