"""
По российский правилам числа округляются до ближайшего целого числа,а если дробная часть числа равна 0.5, то число округляется вверх.
Дано неотрицательное число x, округлите его по этим правилам. Обратите внимание, что функция round не годится для этой задачи!
"""

num = float(input())
if num > 0:
    num += 0.5
else:
    num -= 0.5
print(int(num))