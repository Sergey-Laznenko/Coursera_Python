"""
Найдите и выведите все двузначные числа, которые равны удвоенному произведению своих цифр.
"""

for i in range(1, 10):
    for j in range(1, 10):
        if i * 10 + j == i * j * 2:
            print(i * j * 2)
