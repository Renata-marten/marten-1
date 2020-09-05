s = input('Введите два числа через запятую')
l = len(s)
list = []
i = 0
while i < l:
    s_int = ''
    a = s[i]
    while '0' <= a <= '9':
        s_int += a
        i += 1
        if i < l:
            a = s[i]
        else:
            break
    i += 1
    if s_int != '':
        list.append(int(s_int))

print(list)
