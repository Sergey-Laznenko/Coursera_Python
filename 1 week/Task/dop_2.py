"""
Дано целое число N. Выведите следующее за ним четное число.
"""


n = int(input())
print(n + 1 + (n + 1) % 2)
