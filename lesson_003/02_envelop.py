# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
#
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7
paper_x, paper_y = 6, 8
# проверить для
# paper_x, paper_y = 9, 8 net
# paper_x, paper_y = 6, 8 da
# paper_x, paper_y = 8, 6 da
# paper_x, paper_y = 3, 4 da
# paper_x, paper_y = 11, 9 net
# paper_x, paper_y = 9, 11 net
# (просто раскоментировать нужную строку и проверить свой код)


envelop_x, envelop_y = 9, 11
paper_x, paper_y = 11, 11

if envelop_x >= paper_x: # сравниваем сторону конверта х с стороной листа х
    if envelop_y >= paper_y: #сравниваем сторону конверта у с стороной листа у
        print('Yes!')
    else:
        if envelop_x >= paper_y:# сравниваем сторону конверта y с стороной листа х
            if envelop_y >= paper_x:# сравниваем сторону конверта у с стороной листа x
                print('Yes!')
            else:
                print('Not')
        else:
            print('Not')
else:# сравниваем в обратном порядке
    if envelop_y >= paper_x:
        if envelop_x >= paper_y:
            print('Yes!')
        else:
            print('Not')
    else:
        print('Not')







# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

# hole_x, hole_y = 8, 9
# brick_x, brick_y, brick_z = 11, 10, 2
# brick_x, brick_y, brick_z = 11, 2, 10
# brick_x, brick_y, brick_z = 10, 11, 2
# brick_x, brick_y, brick_z = 10, 2, 11
# brick_x, brick_y, brick_z = 2, 10, 11
# brick_x, brick_y, brick_z = 2, 11, 10
# brick_x, brick_y, brick_z = 3, 5, 6
# brick_x, brick_y, brick_z = 3, 6, 5
# brick_x, brick_y, brick_z = 6, 3, 5
# brick_x, brick_y, brick_z = 6, 5, 3
# brick_x, brick_y, brick_z = 5, 6, 3
# brick_x, brick_y, brick_z = 5, 3, 6
# brick_x, brick_y, brick_z = 11, 3, 6
# brick_x, brick_y, brick_z = 11, 6, 3
# brick_x, brick_y, brick_z = 6, 11, 3
# brick_x, brick_y, brick_z = 6, 3, 11
# brick_x, brick_y, brick_z = 3, 6, 11
# brick_x, brick_y, brick_z = 3, 11, 6
# (просто раскоментировать нужную строку и проверить свой код)

hole_x, hole_y = 8, 9
brick_x, brick_y, brick_z = 5, 6, 3

if (hole_x >= brick_x <= hole_y) and (hole_x >= brick_y <= hole_y):
    print('Yes')
elif (hole_x >= brick_y <= hole_y) and (hole_x >= brick_z <= hole_y):
    print('Yes')
elif (hole_x >= brick_x <= hole_y) and (hole_x >= brick_z <= hole_y):
    print('Yes')
else:
    print('Not')