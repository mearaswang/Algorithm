def shell(nums):

    # Initialize the gap with half of the length
    size = len(nums)
    gap = size // 2
    # Within each shell, use any type of sort method, such as insertion sort
    # Until shell gap is 1
    while gap > 0:
        for i in range(gap, size):
            temp = nums[i]
            j = i
            
            while j>=gap and nums[j - gap] > temp:
                nums[j] = nums[j - gap]
                j -= gap
            
            nums[j] = temp
        gap = gap // 2
    return nums