"""
Головоломка “Ханойские башни” состоит из трех стержней, пронумерованных числами 1, 2, 3. На стержень 1 надета пирамидка
из n дисков различного диаметра в порядке убывания диаметра (снизу находится самый большой диск,
а сверху — самый маленький). Диски можно перекладывать с одного стержня на другой по одному,
при этом диск нельзя класть на диск меньшего диаметра. Необходимо переложить всю пирамидку
со стержня 1 на стержень 3 за минимальное число перекладываний.

Напишите программу, которая решает головоломку; для данного числа дисков n печатает последовательность перекладываний
в формате a b c, где a — номер перекладываемого диска, b — номер стержня с которого снимается данный диск,
c — номер стержня на который надевается данный диск.

Программа должна вывести минимальный (по количеству произведенных операций) способ перекладывания
пирамидки из данного числа дисков.
"""


def move(n, x, y):
    if n == 1:
        print(1, x, y)
    else:
        move(n - 1, x, 6 - x - y)
        print(n, x, y)
        move(n - 1, 6 - x - y, y)


num = int(input())
move(num, 1, 3)
