# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

#错误解法
# originalNum = ["1", "2", "3"]
# resrult = set()
#
# def coumputeNum(originalNum, nums):
#     for num in originalNum:
#         if nums.find(num) == -1:
#             return False
#     return True
#
# for num in range(4322):
#     if len(str(num)) == 3 and coumputeNum(originalNum, str(num)):
#         resrult.add(num)
#
# print(resrult)


#正确解法
for i in range(1, 5):
    for o in range(1, 5):
        for k in range(1, 5):
            if i != o and i != k and k != o:
                print(i,o,k)

# 程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。

# 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？