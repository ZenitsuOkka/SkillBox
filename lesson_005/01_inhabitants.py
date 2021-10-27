# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

import room_1 as f1
inhabitant1 = ', '.join(f1.folks)
import room_2 as f2
inhabitant2 = ', '.join(f2.folks)
print('В комнате 1 живут:', inhabitant1)
print('В комнате 2 живут:', inhabitant2)