# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1 import room1 as central_house1_room1, room2 as central_house1_room2
from district.central_street.house2 import room1 as central_house2_room1, room2 as central_house2_room2
from district.soviet_street.house1 import room1 as soviet_house1_room1, room2 as soviet_house1_room2
from district.soviet_street.house2 import room1 as soviet_house2_room1, room2 as soviet_house2_room2



print('На районе живут', inhabitant.join(my_list))