def check_three(a):
    global result

    if (a[0][0] == a[1][0] == a[2][0] == 'X') \
            or (a[0][1] == a[1][1] == a[2][1] == 'X') \
            or (a[0][2] == a[1][2] == a[2][2] == 'X') \
            or (a[0][0] == a[0][1] == a[0][2] == 'X') \
            or (a[1][0] == a[1][1] == a[1][2] == 'X') \
            or (a[2][0] == a[2][1] == a[2][2] == 'X') \
            or (a[0][0] == a[1][1] == a[2][2] == 'X') \
            or (a[0][2] == a[1][1] == a[2][0] == 'X'):
        result = "X wins"
        return True

    if (a[0][0] == a[1][0] == a[2][0] == 'O') \
            or (a[0][1] == a[1][1] == a[2][1] == 'O') \
            or (a[0][2] == a[1][2] == a[2][2] == 'O') \
            or (a[0][0] == a[0][1] == a[0][2] == 'O') \
            or (a[1][0] == a[1][1] == a[1][2] == 'O') \
            or (a[2][0] == a[2][1] == a[2][2] == 'O') \
            or (a[0][0] == a[1][1] == a[2][2] == 'O') \
            or (a[0][2] == a[1][1] == a[2][0] == 'O'):
        result = "O wins"
        return True


a = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
game = True
counter = 0
result = "Draw"

print('---------')
print(f'|       |')
print(f'|       |')
print(f'|       |')
print('---------')

while counter < 9:
    c = input('Enter the coordinates: ').split()
    if len(c) == 2 and c[0].isdecimal() and c[1].isdecimal():
        c_0 = int(c[0]) - 1
        c_1 = int(c[1]) - 1
        if (0 <= c_0 <= 2) and (0 <= c_1 <= 2):
            if a[c_0][c_1] == 'X' or a[c_0][c_1] == 'O':
                print('This cell is occupied! Choose another one!')
            else:
                a[c_0][c_1] = 'X' if counter % 2 == 0 else 'O'
                print('---------')
                print(f'| {a[0][2]} {a[1][2]} {a[2][2]} |')
                print(f'| {a[0][1]} {a[1][1]} {a[2][1]} |')
                print(f'| {a[0][0]} {a[1][0]} {a[2][0]} |')
                print('---------')
                counter += 1
                if check_three(a):
                    break
        else:
            print('Coordinates should be from 1 to 3!')
    else:
        print('You should enter numbers!')

print(result)
