def find_with_attribute(lf_str):
    with open('phonebook.txt', "r", encoding = "UTF-8") as save_info:
        for line in save_info:
            if str(lf_str).lower() in str(line).lower():
                print(line)

def ask_for_attribute():
    print("Введите атрибут для поиска данных или проигнорируйте для вывода всех данных")
    lf_str = str(input("Поиск: "))
    return lf_str

find_with_attribute(ask_for_attribute())
def import_new_data():
    print("Введите новые данные в заданном формате: Имя Фамилия; Телефон")
    with open('phonebook.txt', "a", encoding="UTF-8") as save_info:
        save_info.writelines(input())
        save_info.write(" \n ")
    print("Данные внесены")

# def delete_line(find_with_attribute):
#     with open('phonebook.txt', "r", encoding="UTF-8") as save_info:
#         data_save = save_info.readline()
#     del data_save[find_with_attribute]
#     with open('phonebook.txt', "w", encoding = "UTF-8") as save_info:
#         save_info.writelines(data_save)
#     print("Данные удалены")


import_new_data()
