"""
Дано трехзначное число. Найдите сумму его цифр.
"""

n = int(input())
a = (n // 100) + ((n // 10) % 10) + (n % 10)
print(a)