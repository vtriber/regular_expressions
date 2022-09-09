from pprint import pprint
import re

# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

# Помещаем Фамилию, Имя и Отчество человека в поля lastname, firstname и surname
contact_list_dict = {}
for list in contacts_list:
  full_name = list[0] + ' ' + list[1] + ' ' + list[2]
  full_name_list = full_name.split()
  i = 0

  for name in full_name_list:
    list[i] = full_name_list[i]
    i +=1

# Объединяем дублирующиеся записи о человеке в одну.
  key = list[0] + list[1]

  if key in contact_list_dict.keys():
    i = 0
    for meaning in contact_list_dict.get(key):
      if meaning == '':
        list_new = contact_list_dict.get(key)
        list_new[i] = list[i]
        y = {key: list_new}
        contact_list_dict.update(y)
      i +=1
  else:
    y = {key: list}
    contact_list_dict.update(y)

# Приводим тедлефоны в соответствующий формат
pattern = r"(\+7|8)\s?\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})([-\s]?)\(?(доб\.)?[\s]?(\d+)?\)?"
substitution = r"+7(\2)\3-\4-\5\6\7\8"
contacts_list = []
for key, list in contact_list_dict.items():
  text = list[5]
  list[5] = re.sub(pattern, substitution, text)
  contacts_list.append(list)

# Записываем результат в файл phonebook.csv
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)