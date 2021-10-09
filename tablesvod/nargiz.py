import pandas as pd
import re

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

# Подключение таблиц
frdo = pd.read_excel("ФРДО.xlsx")
frdo_2 = pd.read_excel("ФРДО.xlsx")
spisok = pd.read_excel("Список.xlsx")

filtr = "(МКОУ)|(МБОУ)|(МОУ)|(ГКОУ)|(ГБОУ)|(ГБУ)|(ГКУ)"

frdo = frdo.replace(filtr,'',regex = True)
spisok = spisok.replace(filtr,'',regex = True)

k=0
for i in frdo.index:
    k+=1
    print(k)
    frdo_name = frdo.iloc[i]['СОШ']
    for j in spisok.index:
        spisok_name = spisok.iloc[j]['СОШ']
        if (frdo_name.lower() in spisok_name.lower()) or (spisok_name.lower() in frdo_name.lower()):
            print('YES')
            frdo_2['Наличие'][i] = 'YES'
        break
frdo_2.to_csv('frdo2.csv', encoding = 'utf-8')
"""
# Объединение таблицы своl и месяц по столбцам Наименование ДОО с правым пересечением
df3 = pd.merge(svod, month, left_on='Наименование ДОО', right_on='Наименование ДОО', how='right')

# Сохранение фрейма в файл
df3.to_csv('тест1.csv', encoding='1251')
"""
