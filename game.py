field = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]
inputs = ('00', '01', '02', '10', '11', '12', '20', '21', '22',)


def paint_field():
    print("  0 1 2")

    for i, value in enumerate(field):
        print(i, *value)


def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")


def check(count):
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["x", "x", "x"]:
            print("Выиграл X!!!")
            return False
        if symbols == ["o", "o", "o"]:
            print("Выиграл 0!!!")
            return False
        if count == 9:
            print("Ничья")
            return False
    return True


def x_or_o(count):
    if count % 2 == 1:
        print('Ходит o')
        return 'x'
    else:
        print('Ходит x')
        return 'o'


def start_game():
    greet()
    count = 0
    print('Ходит x')
    paint_field()
    while check(count):
        inp = input("Введите координаты x и y (например, 00)")
        if inp in inputs:
            count += 1
            x, y = int(inp) // 10, int(inp) % 10
            if field[x][y] == ' ':
                field[x][y] = x_or_o(count)
            else:
                print('Клетка занята')
                count -= 1
                continue
            paint_field()


start_game()
