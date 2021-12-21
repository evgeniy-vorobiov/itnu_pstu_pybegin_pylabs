# 1) Заменить все Х на У
s_x = 'qwertyx asdfghy xxx yyy'
bez_x = ''
for i in s_x:
    if i == 'x':
        bez_x += 'y'
    else:
        bez_x += i
print(s_x)
print(bez_x)

# 2) Произведение чисел, кратных и 3 и 5
a = [1, 2, 3, 5, 9, 10, 15, 18, 20, 21, 24, 25, 30]
p = 1
for i in a:
    if i//3==i/3 and i//5==i/5:
        p *= i
print(p)

# 3) Заменить все Х на У без допстроки
s_x = 'qwertyx asdfghy xxx yyy'
s_x = s_x.replace('x','y')
print(s_x)
