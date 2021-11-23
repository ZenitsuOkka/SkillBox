# -*- coding: utf-8 -*-

# Сделать генератор текста на основе статистики
# Идея проста: подсчитаем какие буквы наиболее часто стоят рядом
# Точнее, подсчитаем как часто за буковой Х идет буква У, на основе некоего текста.
# После этого начнем с произвольной буквы и каждую следующую будем выбирать в зависимости от
# частоты её появления в статистике.
import zipfile
from pprint import pprint

zip_file_name = 'voyna-i-mir.txt.zip'

zfile = zipfile.ZipFile(zip_file_name, 'r')
for filename in zfile.namelist():
    zfile.extract(filename)

file_name = 'voyna-i-mir.txt'

stat = {}
#stat = {'а': {'т': 500, 'х': 5, }, 'т':}

prev_char = ' '
with open(file_name, 'r', encoding='cp1251') as file:
    for line in file:
        #print(line)
        for char in line:
            if prev_char in stat:
                if char in stat[prev_char]:
                    stat[prev_char][char] += 1
                else:
                    stat[prev_char][char] = 1
            else:
                stat[prev_char] = {char: 1}
            prev_char = char

pprint(stat)

totals = {}
for prev_char, char_stat in stat.items():
    totals[prev_char] = 0
    for char, count, in char_stat.items():
        totals[prev_char] += count
