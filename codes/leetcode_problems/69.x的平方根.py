# """
# 题目描述：
# 实现int sqrt(int x)函数。
#
# 计算并返x的平方根，其中x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
#
# """
#
#
# def my_sqrt(x):
#     """
#
#     :param x: int
#     :return:
#     牛顿迭代法求平方根
#     """
#     if x <= 1:
#         return x
#     else:
#         r = x
#         while r > x/r:
#         # 迭代停止的条件，可以设定一个误差范围,本题只要求返回整数部分
#             r = (x/r + r)//2
#
#         return int(r) # 返回值必须为整数
