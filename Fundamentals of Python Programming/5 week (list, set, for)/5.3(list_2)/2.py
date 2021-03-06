"""
Дан список целых чисел, число k и значение C. Необходимо вставить в список на позицию с индексом k элемент, равный C,
сдвинув все элементы, имевшие индекс не менее k, вправо.

Поскольку при этом количество элементов в списке увеличивается, после считывания списка
в его конец нужно будет добавить новый элемент, используя метод append.

Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе и не создавая дополнительного списка.
"""

# Альтернативный вариант решения

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
res = l1[:l2[0]] + [l2[1]] + l1[l2[0]:]
print(*res)
