print('Введите число x')
x = int(input())
print('Введите число y')
y = int(input())
print('Введите число x1')
x1 = int(input())
print('Введите число y1')
y1 = int(input())
if x > 0 and y > 0:
    if x1 > 0 and y1 > 0:
        print('YES')
    else:
        print('NO')
else:
    if x < 0 and y < 0:
        if x1 < 0 and y1 < 0:
            print('YES')
        else:
            print('NO')
    else:
        if x > 0 and y < 0:
            if x1 > 0 and y1 < 0:
                print('YES')
            else:
                print('NO')
        else:
            if x < 0 and y > 0:
                if x1 < 0 and y > 0:
                    print('YES')
                else:
                    print('NO')
            else:
                print('NO')