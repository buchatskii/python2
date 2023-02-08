# Задача 16
# number = int(input("Введите размер списка: "))
# num = int(input("Сколько раз встречается число: "))
# spam = list(range(1, number + 1))
# print(spam)
# print(spam.count(num))

# Задача 18
# number = int(input("Введите размер списка: "))
# num = int(input("Ближайшие к числу: "))
# spam = list(range(1, number + 1))
# for i in spam:
#     if i == num:
#         print(num - 1, num + 1)




# Задача 20
list_1 = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z'],
    1: ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
    2: ['Д', 'К', 'Л', 'М', 'П', 'У'],
    3: ['Б', 'Г', 'Ё', 'Ь', 'Я'],
    4: ['Й', 'Ы'],
    5: ['Ж', 'З', 'Х', 'Ц', 'Ч'],
    8: ['Ш', 'Э', 'Ю'],
    10: ['Ф', 'Щ', 'Ъ'],
}
point = 0
word = str.upper(input("Введите слово: "))
for i in word:
    for j in list_1:
        if i in list_1[j]:
            point += j
            continue
print(point)

