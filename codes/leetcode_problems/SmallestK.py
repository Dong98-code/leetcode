"""
返回最小的K个数
"""


class Solution:
    def smallestK(self, arr, k: int):
        if k == 0:
            return []
        self.sorted(arr, 0, len(arr)-1, k)
        return arr[:k]

    def partition(self, arr, l, r):
        pivot = l
        index = pivot + 1
        i = index
        while i <= r:
            if arr[i] < arr[pivot]:
                arr[index], arr[i] = arr[i], arr[index]
                index += 1
            i += 1

        arr[pivot], arr[index - 1] = arr[index - 1], arr[pivot]  # 交换index及基准值
        return index - 1

    def sorted(self, arr, l, r, k):
        if l < r:
            partition_index = self.partition(arr, l, r)

            if partition_index < k - 1:
                self.sorted(arr, partition_index + 1, r, k)
            elif partition_index > k - 1:
                self.sorted(arr, l, partition_index - 1, k)
        return arr


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 3, 5, 7, 2, 4, 6, 8]
    k = 4
    print(sol.smallestK(arr,k))
