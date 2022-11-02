def sortItemByUnitValue(d):
    # список предметов с размерами и очками выживания
    return {k: v for k, v in sorted(d.items(), key=lambda item: item[1][1] / item[1][0], reverse=True)}

items = {'в': (3, 25),
         "п": (2, 15),
         "б": (2, 15),
         "а": (2, 20),
         # "и": (1, 5),
         "н": (1, 15),
         "т": (3, 20),
         "о": (1, 25),
         "ф": (1, 15),
         # "д": (1, 10),
         "к": (2, 20),
         "р": (2, 20)
         }
items = sortItemByUnitValue(items)
items_am = len(items)
# total - переменная для подсчёта очков предметов, не взятых с собой
# + 15 очков, которые мы уже имеем со старта по своему варианту (8)
total = 15
# bp_cap - ограничение по суммарному колличеству ячеек
bp_cap = 8
# lefted - переменная для подсчёта очков предметов, не взятых с собой
lefted = 0
# bg - рюкзак
bg = []
# перебираем все предметы
for k in items:
    v = items[k][0]
    if bp_cap - v >= 0:
        bp_cap -= v
        total += items[k][1]
        bg.append([k])
        if v == 2:
            bg.append([k])
        if v == 3:
            bg.append([k])
            bg.append([k])
    else:
        lefted += items[k][1]
bg.append(["и"])
bg.append([""])
bg_0 = []
# создаём массивы (длина каждого - 3)
bg_1 = [i for i in bg[:3]]
bg_2 = [i for i in bg[3:6]]
bg_3 = [i for i in bg[6:]]
# добавляем предыдущие массивы в один целый массив
bg_0.append(bg_1)
bg_0.append(bg_2)
bg_0.append(bg_3)
# создание двумерного массива 3x3
for i in bg_0:
    for i2 in i:
        print(i2, end=' ')
    print()
# Итоговые очки выживания: сумма очков со всех предметов из рюкзака + очки за ингалятор - сумма очков со всех предметов не из рюкзака - очки за антидот
print("Итоговые очки выживания:",total + 5 - lefted - 10)
