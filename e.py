print('Введите число')
k = int(input())
hours = k//3600
last_in_hours = k - hours*3600
print('It is', hours, 'hours,', last_in_hours//60, 'minutes.')