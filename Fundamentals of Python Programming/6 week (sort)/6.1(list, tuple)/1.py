"""
Первая строка входных данных содержит количество элементов в массиве N, N ≤ 10⁵. Далее идет N целых чисел,
не превосходящих по абсолютной величине 10⁹.
"""


n = int(input())
myList = list(map(int, input().split()[:n]))
myList.sort()
print(' '.join(map(str, myList)))
