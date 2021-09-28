# 归并排序
def merge(list_left, list_right):
    """
    将两个有序数组合并成一个大的的有序数组
    :param list_left:左数组
    :param list_right: 右数组
    :return:
    """
    l = 0
    r = 0
    new_list = []
    while l < len(list_left) and r < len(list_right):
        if list_left[l] < list_right[r]:
            new_list.append(list_left[l])
            l += 1
        else:
            new_list.append(list_right[r])
            r += 1
    new_list += list_left[l:]
    new_list += list_right[r:]
    return new_list


def merge_sort(mylist):
    """

    :param mylist: 需要排序的数组
    :return: 拍好序的数组
    """
    if len(mylist) <= 1:
        return mylist

    mid = len(mylist) // 2
    list_left = merge_sort(mylist[:mid])
    list_right = merge_sort(mylist[mid:])
    return merge(list_left, list_right)


if __name__ == "__main__":
    my_list = [1, 1, 5, 10, 9]
    res = merge_sort(my_list)
    print('归并排序结果：',res)
