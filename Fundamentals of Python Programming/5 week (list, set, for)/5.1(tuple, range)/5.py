"""
Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n флагов.
Изображение одного флага имеет размер 4×4 символов, между двумя соседними флагами также имеется пустой (из пробелов)
столбец. Разрешается вывести пустой столбец после последнего флага. Внутри каждого флага должен быть записан
его номер — число от 1 до n.
"""


num = int(input())

str1 = '+___ '
str2 = ''
str3 = '|__\ '
str4 = '|    '
for i in range(num):
    str2 = str2 + '|' + str(i + 1) + ' / '

res = str1 * num, str2, str3 * num, str4 * num
print(*res, sep='\n')
