# 题目1：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
""""
for i in range(1, 6):
    for x in range(1, 6):
        for v in range(1, 6):
            if i != x and i != v and v != x:
                print(i, x, v)
"""

"""
题目2
企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，
低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，
超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
"""
"""
totalNum = int(input())
moneys = [1000000, 600000, 400000, 200000, 100000]
commission = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]

for i in range(0, 5):
    if i == 4 and totalNum <= moneys[i]:
        print("是按照", commission[i], "提成")
        print(totalNum * commission[i])
        break
    if totalNum >= moneys[i]:
        a = (totalNum - moneys[i]) * commission[i]
        b = moneys[i] * commission[i + 1]
        result = a + b
        print(a)
        print(b)
        print(result)
        break
"""

# 题目4 输入某年某月某日，判断这一天是这一年的第几天？
# ??

# 输入某年某月某日，判断这一天是这一年的第几天？
"""
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
count = 0
y = int(input())
m = int(input())
d = int(input())
# y = 2020
# m = 1
# d = 29
for i in range(0, m - 1):
    count = count + days[i - 1]
a = count + d
if y % 4 == 0 and ((m > 2 and d > 28) or m > 3):
    print(a + 1)
else:
    print(a)
"""

# 题目5 输入三个整数x,y,z，请把这三个数由大到小输出。
# a = 23111
# b = 3224
# c = 22223

""" 
# 解题1
nums = []
nums.append(int(a))
nums.append(int(b))
nums.append(int(c))

for i in range(len(nums) - 1):
    for j in range(len(nums) - 1):
        if nums[j] < nums[j+1]:
           nums[j], nums[j+1] = nums[j+1], nums[j]
print(nums)
"""

"""
# 解题2
nums = []
nums.append(int(a))
nums.append(int(b))
nums.append(int(c))
nums.sort()
print(nums)
"""

"""
a + b = c
    c + b = d
        d + c = e
            e + d = f
"""
# 题目6 斐波那契数列。 1、1、2、3、5、8、13
"""
nums = []
a = 1
b = 2
nums.append(int(a))
nums.append(int(b))
for i in range(1, 10):
    c = nums[-1]
    d = nums[len(nums)-2]
    nums.append(int(c + d))
print(nums)
"""
# 题目7：将一个列表的数据复制到另一个列表中。
"""
nums = [1, 2, 3, 4]
nums2 = []
nums2 = nums.copy()

print(nums2)
"""

# 题目8：输出 9*9 乘法口诀表。
# for i in range(1, 10):
#     for j in range(i, 10):
#         print(i, "*", j, "=", i*j, "\t")
#     print("\n")

# 题目9 暂停一秒输出。
"""
import time
for i in range(0, 100):
    print(i)
    time.sleep(1)
"""

# 题目10 暂停一秒输出，并格式化当前时间。
"""
import time
for i in range(0, 5):
    time.sleep(1)
    print(time.strftime("%y-%m-%d %H:%M:%S", time.localtime()))
"""
"""
# 解题2
import datetime as dt
import time as t

for i in range(0, 10):
    print(dt.datetime.now())
    # t.sleep(i)
"""
# 题目11 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子
# ，假如兔子都不死，问每个月的兔子总数为多少？
# 斐波那契



# 判断101-200之间有多少个素数，并输出所有素数。
"""
def flagNum(num):
    for i in range(1, num):
        if num - i == 1:
            return True
        if num % (num - i) == 0:
           return False
    return True
count = 0
for i in range(101, 201):
    if flagNum(i):
        print(i)
        count += 1
print("共计%d个"% count)
"""
