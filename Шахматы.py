print('Введите координаты поля без пробелов')
print('(Каждая координата - числа от 1 до 8, сначала по горизонтали, потом по вертикали)')
xy2 = int(input())
x2 = xy2 // 10
y2 = xy2 % 10

if (x2 < 1) or (x2 > 8) or (y2 > 8) or (y2 < 1):
    print('Каждая координата должна быть в диапазоне от 1 до 8, сначала по горизонтали, потом по вертикали')
    print('Пожалуйста, перезапустите программу')
    exit()

print('Введите координаты фигуры без пробелов')
print('(Каждая координата - числа от 1 до 8, сначала по горизонтали, потом по вертикали)')
xy1 = int(input())
x1 = xy1 // 10
y1 = xy1 % 10

if (x1 < 1) or (x1 > 8) or (y1 > 8) or (y1 < 1):
    print('Каждая координата должна быть в диапазоне от 1 до 8, сначала по горизонтали, потом по вертикали')
    print('Пожалуйста, перезапустите программу')
    exit()

figurexy = [x1, y1]
fieldxy = [x2, y2]
if fieldxy == figurexy:
    print('Фигура стоит на введенном поле')
    exit()

print('Введите наименование фигуры без пробелов')
figure_name = str(input())
uslov = 0
exist = 0

if figure_name.lower() == 'ферзь':
    for i in range (-9, 8):
        if ((x2 == x1 + i and y2 == y1 + i) or x2 == x1 or y2 == y1):
            uslov = 1
    if uslov == 0:
        print("Фигура не угрожает введенному полю")
    else:
        print("Фигура угрожает введенному полю")
else:
    exist += 1

if figure_name.lower() == 'слон':
    for i in range (-9, 8):
        if x2 == x1 + i and y2 == y1 + i:
            uslov = 1
    if uslov == 0:
        print("Фигура не угрожает введенному полю")
    else:
        print("Фигура угрожает введенному полю")
else:
    exist += 1

if figure_name.lower() == 'ладья':
    if x2 == x1 or y2 == y1:
        uslov = 1
    if uslov == 0:
        print("Фигура не угрожает введенному полю")
    else:
        print("Фигура угрожает введенному полю")
else:
    exist += 1

if figure_name.lower() == 'конь':
    for i1 in range(1,3):
        for i2 in range(1,3):
            if not i1 == i2:
                if ((x2 == x1 + i1) or (x2 == x1 - i1)) and ((y2 == y1 + i2) or (y2 == y1 - i2)):
                    uslov = 1
    if uslov == 0:
        print("Фигура не угрожает введенному полю")
    else:
        print("Фигура угрожает введенному полю")
else:
    exist += 1

if exist == 4:
    print('Такая фигура отсутствует в списке')
