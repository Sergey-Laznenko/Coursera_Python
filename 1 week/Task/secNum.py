"""
Дано натуральное число. Найдите цифру, стоящую в разряде десятков в его десятичной записи
(вторую справа цифру или 0, если число меньше 10).
"""

n = int(input())
print((n // 10) % 10)
