def merge(left, right):
    # merge two lists
    merged_list = []
    left_i, right_i = 0, 0
    while left_i < len(left) and right_i < len(right):
        if left[left_i] < right[right_i]:
            merged_list.append(left[left_i])
            left_i += 1
        else:
            merged_list.append(right[right_i])
            right_i += 1

    # When one list is exhausted, handle the other.
    while left_i < len(left):
        merged_list.append(left[left_i])
        left_i += 1

    while right_i < len(right):
        merged_list.append(right[right_i])
        right_i += 1
    
    return merged_list

# Recursively split and merge each sub list, until the length is 1.
def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return merge(left, right)