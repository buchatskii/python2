# Задача 16
# number = int(input("Введите размер списка: "))
# num = int(input("Сколько раз встречается число: "))
# spam = list(range(1, number + 1))
# print(spam)
# print(spam.count(num))

# Задача 18
number = int(input("Введите размер списка: "))
num = int(input("Ближайшие к числу: "))
spam = list(range(1, number + 1))
for i in spam:
    if i == num:
        print(num - 1, num + 1)




# Задача 20
# list_1 = {
#     1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
#     2: ['D', 'G'],
#     3: ['B', 'C', 'M', 'P'],
#     4: "F, H, V, W, Y",
#     5: "K"],
#     8: "J, X"],
#     10: "Q, Z"]
# }
# point = 0
# word = str.upper(input("Введите слово: "))
# for i in word:
#     for j in list_1:
#         if i in list_1[j]:
#             point += 1
# print(point)

