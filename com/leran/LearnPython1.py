# 使用lambda 计算 1 - 10 的阶乘
"""
nums = lambda l: l * l
for i in range(1, 11):
    print(nums(i))
"""

# lambda练习
"""
def myfun(n):
    return lambda n1: n * n1

for i in range(1, 10):
    num = myfun(i)
    print(num(i))
"""

# def is_odd(n):
#     return n % 2 == 1
# L = list(filter(is_odd, range(1, 20)))
# print(L)

# L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
# a = range(0, 10)
# print(type(a))
#
