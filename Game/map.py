from random import randint


class Tile():
    def __init__(self, x, y, wall = "ˍ ˍ", state = 1, situation = None, was_here = False, digger_was_here = False):
        self.x = x
        self.y = y
        self.state = state
        self.situation = situation
        self.was_here = was_here
        self.digger_was_here = digger_was_here
        self.wall = wall

    def __str__(self):
        return f"{self.wall}"

def matrix_print(matrix):
    for i, j in enumerate(matrix):
        for z, l in enumerate(j):
            print(matrix[i][z], end="")
        print()

def matrix_make_tiles(height, width, a = 0):
    lvlmap = [[a for i in range(width)] for j in range(height)]
    for i, j in enumerate(lvlmap):
        for z, l in enumerate(j):
            lvlmap[i][z] = Tile(i,z)
    return lvlmap


def map_generator3(lvlmap):
    max_x, max_y = len(lvlmap) - 1, len(lvlmap[0]) - 1
    digger = [0, 0]
    path1 = [(0, 0)]
    map_ave = (len(lvlmap) + len(lvlmap[0])) / 2
    b_count = 0
    a_count = 0
    lvlmap[max_x][max_y].situation = "door"
    while digger != [max_x, max_y]:
        for i, j in enumerate(lvlmap):
            for z, l in enumerate(j):
                if [i, z] == digger:
                    lvlmap[i][z].digger_was_here = True
                    if digger[0] == 0 and digger[1] == 0: #диггер в верхнем левом углу
                        a = randint(0, 1)
                        if a == 0: #рандом + если не был справа, идем  and lvlmap[i + 1][z].digger_was_here == False
                            digger[0] += 1 #вправо
                            path1.append((digger[0], digger[1]))
                            b_count = 0
                            break
                        else: #рандом + если не был снизу, идем  lvlmap[i][z + 1].digger_was_here == False
                            digger[1] += 1 #вниз
                            path1.append((digger[0], digger[1]))
                            b_count = 0
                            break
                    elif digger[0] == 0 and digger[1] == max_y: #диггер в нижнем левом углу
                        a = randint(0,1)
                        if a == 0 and lvlmap[i + 1][z].digger_was_here == False:  # рандом + если не был справа, идем
                            digger[0] += 1  # вправо
                            path1.append((digger[0], digger[1]))
                            b_count = 0
                            break
                        elif lvlmap[i][z - 1].digger_was_here == False:  # рандом + если не был вверху, идем
                            digger[1] -= 1  # вверх
                            path1.append((digger[0], digger[1]))
                            b_count = 0
                            break
                        else:
                            b_count += 1
                            a_count += 1
                            digger = list(path1[-b_count])
                            break
                    elif digger[0] == max_x and digger[1] == 0: #диггер в верхнем правом углу
                        a = randint(0, 1)
                        if a == 0 and lvlmap[i - 1][z].digger_was_here == False:  # рандом + если не был слева, идем
                            digger[0] -= 1  # влево
                            path1.append((digger[0], digger[1]))
                            b_count = 0
                            break
                        elif lvlmap[i][z + 1].digger_was_here == False:  # рандом + если не был сверзу, идем
                            digger[1] += 1  # вниз
                            path1.append((digger[0], digger[1]))
                            b_count = 0
                            break
                        else:
                            b_count += 1
                            a_count += 1
                            digger = list(path1[-b_count])
                            b_count = 0
                            break
                    elif digger[0] == 0 and 0 < digger[1] < max_y: #диггер слева
                        a = randint(0, 1)
                        if a == 0 and lvlmap[i + 1][z].digger_was_here == False:
                            digger[0] += 1  # вправо
                            path1.append((digger[0], digger[1]))
                            b_count = 0
                            break
                        else:
                            a = randint(0, 1)
                            if a == 0 and lvlmap[i][z - 1].digger_was_here == False:
                                digger[1] -= 1  # вверх
                                path1.append((digger[0], digger[1]))
                                b_count = 0
                                break
                            elif lvlmap[i][z + 1].digger_was_here == False:  # рандом + если не был снизу, идем
                                digger[1] += 1  # вниз
                                path1.append((digger[0], digger[1]))
                                b_count = 0
                                break
                            else:
                                b_count += 1
                                a_count += 1
                                digger = list(path1[-b_count])
                                break
                    elif 0 < digger[0] < max_x and digger[1] == 0: #диггер сверху
                        a = randint(0, 1)
                        if a == 0 and lvlmap[i + 1][z].digger_was_here == False:
                            digger[0] += 1  # вправо
                            path1.append((digger[0], digger[1]))
                            b_count = 0
                            break
                        else:
                            a = randint(0, 1)
                            if a == 0 and lvlmap[i][z + 1].digger_was_here == False:  # рандом + если не был сверху, идем
                                digger[1] += 1  # вниз
                                path1.append((digger[0], digger[1]))
                                b_count = 0
                                break
                            elif lvlmap[i - 1][z].digger_was_here == False:  # рандом + если не был снизу, идем
                                digger[0] -= 1  # влево
                                path1.append((digger[0], digger[1]))
                                b_count = 0
                                break
                            else:
                                b_count += 1
                                a_count += 1
                                digger = list(path1[-b_count])
                                break
                    elif 0 < digger[0] < max_x and digger[1] == max_y: #диггер снизу
                        a = randint(0, 1)
                        if a == 0 and lvlmap[i + 1][z].digger_was_here == False:
                            digger[0] += 1  # вправо
                            path1.append((digger[0], digger[1]))
                            b_count = 0
                            break
                        else:
                            a = randint(0,1)
                            if a == 0 and lvlmap[i][z - 1].digger_was_here == False:
                                digger[1] -= 1  # вверх
                                path1.append((digger[0], digger[1]))
                                b_count = 0
                                break
                            elif lvlmap[i - 1][z].digger_was_here == False:
                                digger[0] -= 1  # влево
                                path1.append((digger[0], digger[1]))
                                b_count = 0
                                break
                            else:
                                a_count += 1
                                b_count += 1
                                digger = list(path1[-b_count])
                                break
                    elif digger[0] == max_x and 0 < digger[1] < max_y: #диггер справа
                        a = randint(0, 1)
                        if a == 0 and lvlmap[i - 1][z].digger_was_here == False:
                            digger[0] -= 1  # влево
                            path1.append((digger[0], digger[1]))
                            b_count = 0
                            break
                        else:
                            a = randint(0, 1)
                            if a == 0 and lvlmap[i][z - 1].digger_was_here == False:
                                digger[1] -= 1  # вверх
                                path1.append((digger[0], digger[1]))
                                b_count = 0
                                break
                            elif lvlmap[i][z + 1].digger_was_here == False:
                                digger[1] += 1  # вниз
                                path1.append((digger[0], digger[1]))
                                b_count = 0
                                break
                            else:
                                b_count += 1
                                a_count += 1
                                digger = list(path1[-b_count])
                                break
                    elif 0 < digger[0] < max_x and 0 < digger[1] < max_y: #диггер внутри
                        a = randint(0, 1)
                        if a == 0:
                            a = randint(0, 1)
                            if a == 0 and lvlmap[i - 1][z].digger_was_here == False:
                                digger[0] -= 1  # влево
                                path1.append((digger[0], digger[1]))
                                b_count = 0
                                break
                            elif lvlmap[i][z - 1].digger_was_here == False:
                                digger[1] -= 1  # вверх
                                path1.append((digger[0], digger[1]))
                                b_count = 0
                                break
                            else:
                                b_count += 1
                                a_count += 1
                                digger = list(path1[-b_count])
                                break
                        else:
                            a = randint(0, 1)
                            if a == 1 and lvlmap[i][z + 1].digger_was_here == False:  # рандом + если не был снизу, идем
                                digger[1] += 1  # вниз
                                path1.append((digger[0], digger[1]))
                                b_count = 0
                                break
                            elif lvlmap[i + 1][z].digger_was_here == False:
                                digger[0] += 1  # вправо
                                path1.append((digger[0], digger[1]))
                                b_count = 0
                                break
                            else:
                                b_count += 1
                                a_count += 1
                                digger = list(path1[-b_count])
                                break
        if a_count > 100:
            break
    p_prop = map_ave / len(path1)
    if (max_x, max_y) in path1 and 0.1 < p_prop < 0.13:
        print(f"Пропорции {p_prop}")
        lvlmap[max_x][max_y].digger_was_here = True
        return lvlmap, path1
    else:
        for i, j in enumerate(lvlmap):
            for z, l in enumerate(j):
                lvlmap[i][z].digger_was_here = False
        return map_generator3(lvlmap)

def add_chest_to_map(lvlmap, path):
    """Функция добавляет в произвольные тайлы карты сундуки, если на выходе сундука нет, еще раз вызывает себя"""
    def check_for_no_chest(lvlmap):
        """Проверочная функция, пробегает по карте для того, что бы удостовериться, что сундук добавлен"""
        chest_flag = False
        for i, j in enumerate(lvlmap):
            for z, l in enumerate(j):
                if lvlmap[i][z].situation == "chest":
                    chest_flag = True
                    return chest_flag
    chests_x_y = []
    for i, j in enumerate(lvlmap):
        for z, l in enumerate(j):
            if lvlmap[i][z].digger_was_here == True and (i, z) != (0, 0) and (i, z) != (len(lvlmap) - 1, len(lvlmap[0]) - 1):
                a = randint(1, len(path))
                chest_chance = list(range(round(len(path) / 100)))
                if a in chest_chance:
                    lvlmap[i][z].situation = "chest"
                    lvlmap[i][z].wall = "ˍ⮹ˍ"
                    chests_x_y.append((i, z))
    if check_for_no_chest(lvlmap) == True:
        return chests_x_y
    else:
        print("Нет сундука, повторяем")
        return add_chest_to_map(lvlmap, path)
def add_random_to_map(lvlmap, path, chests_x_y):
    """Функция добавляет в произвольные тайлы карты свитки и зелья"""
    random_s_x_y = []
    for i, j in enumerate(lvlmap):
        for z, l in enumerate(j):
            if lvlmap[i][z].digger_was_here == True and (i, z) != (0, 0) and (i, z) not in chests_x_y and (i, z) != (len(lvlmap) - 1, len(lvlmap[0]) - 1):
                a = randint(1, len(path))
                random_stuff_chance = list(range(round(len(path)/ 10))) #добавляет случайные события
                if a in random_stuff_chance:
                    lvlmap[i][z].situation = "random"
                    lvlmap[i][z].wall = "ˍ?ˍ"
                    random_s_x_y.append((i, z))
    return random_s_x_y










