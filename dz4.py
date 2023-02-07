import random
num_1 = 3
num_2 = 7
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