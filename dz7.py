# Задание 34
# line = "пара-р-рам рам-пам-папам"
# print(line.split())
# vowel = "ауоыэяюёие"
# itog = list()
# for i in line:
#     k = 0
#     for x in i:
#         if x in vowel:
#             k += 1
#         itog.append(k)
# if len(set(itog)) == 0:
#     print('Парам пам-пам')
# else:
#     print('Пам парам')

# Задание 36
def printOperationTable(operation, numRows=9, numColumns=9):
    for row in range(1, numRows + 1):
        for column in range(1, numColumns + 1):
            print(operation(row, column), end='\t')
        print()
print(printOperationTable(lambda x,y: x * y, 2, 3))
