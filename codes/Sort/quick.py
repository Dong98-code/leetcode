# -*- coding: utf-8 -*-
# @Time : 2021/9/3 14:38
# @Author : XDD
# @File : quick.py
def partition(arr, left, right):
    """
    返回index为基准值所在的位置
    :param arr: 需要排序的子序列
    :param left:
    :param right:
    :return:
    """
    pivot = left
    index = pivot + 1
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:
            arr[i], arr[index] = arr[index], arr[i]  # 交换位置，使得小于基准值的数在index左侧,index此时指向的值为大于pivot
            index += 1
        i += 1
    arr[index - 1], arr[pivot] = arr[pivot], arr[index - 1]
    return index - 1


def quick_sort(arr, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr) - 1 if not isinstance(right, (int, float)) else right
    if left < right:
        partition_index = partition(arr, left, right)
        quick_sort(arr, left, partition_index - 1)
        quick_sort(arr, partition_index + 1, right)
    return arr


if __name__ == "__main__":
    arr = [30, 24, 5, 58, 18, 36, 12, 42, 39]
    res = quick_sort(arr)
    print(res)
