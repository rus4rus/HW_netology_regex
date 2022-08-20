# Ваша задача: починить адресную книгу, используя регулярные выражения.
# Структура данных будет всегда:
# lastname,firstname,surname,organization,position,phone,email
# Предполагается, что телефон и e-mail у человека может быть только один.
# Необходимо:
#
#     поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;
#     привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;
#     объединить все дублирующиеся записи о человеке в одну.
# читаем адресную книгу в формате CSV в список contacts_list

import csv
from regex_functions import modify_name_to_standart, modify_phone_number, delete_duplicates

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ

new_contact_list = modify_name_to_standart(contacts_list)
new_contact_list = delete_duplicates(new_contact_list)
for i in range(1, len(new_contact_list)):
    new_contact_list[i][5] = modify_phone_number(new_contact_list[i][5])

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(new_contact_list)




