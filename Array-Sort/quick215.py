# class Solution:
#     def partition(self, nums: [int], low: int, high: int) -> int:        
#         # 以第 1 位元素为基准数
#         i = low + (high-low) // 2
#         nums[i], nums[low] = nums[low], nums[i]
#         pivot = nums[low]
        
#         i, j = low, high
#         while i < j:
#             # 从右向左找到第 1 个小于基准数的元素
#             while i < j and nums[j] >= pivot:
#                 j -= 1
#             # 从左向右找到第 1 个大于基准数的元素
#             while i < j and nums[i] <= pivot:
#                 i += 1
#             # 交换元素
#             nums[i], nums[j] = nums[j], nums[i]
        
#         # 将基准数放到正确位置上
#         nums[j], nums[low] = nums[low], nums[j]
#         return j

#     def quickSort(self, nums: [int], low: int, high: int, k: int, size: int) -> [int]:
#         if low < high:
#             # 按照基准数的位置，将数组划分为左右两个子数组
#             pivot_i = self.partition(nums, low, high)
#             if pivot_i == size - k:
#                 return nums[size - k]
#             if pivot_i > size - k:
#                 self.quickSort(nums, low, pivot_i - 1, k, size)
#             if pivot_i < size - k:
#                 self.quickSort(nums, pivot_i + 1, high, k, size)

#         return nums[size - k]


#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         size = len(nums)
#         return self.quickSort(nums, 0, len(nums) - 1, k, size)




## Ordinary quick sort
# import random
# def randomPartition(nums, low, high):
#     i = random.randint(low, high)
#     nums[i], nums[low] = nums[low], nums[i]
#     return partition(nums, low, high)
# def partition(nums, low, high):
#     pivot = nums[low]
    
#     i, j = low, high
    
#     while i < j:
#         while i < j and nums[j] >= pivot:
#             j -= 1
#         while i < j and nums[i] <= pivot:
#             i += 1
#         nums[i], nums[j] = nums[j], nums[i]
    
#     nums[i], nums[low] = nums[low], nums[i]
    
#     return i
    
    
# def quick(nums, low, high):
#     if low < high:
#         pivot_i = randomPartition(nums, low, high)
#         quick(nums, low, pivot_i - 1)
#         quick(nums, pivot_i + 1, high)
#     return nums
    
# # def sortA(nums):
# #     return quick(nums, 0, len(nums) -1 )
    
    
# nums = [4,7,5,2,6,1,3]
# # sortA(nums)
# quick(nums, 0, len(nums) -1 )
        