def counting(nums):
    nums_max, nums_min = max(nums), min(nums)
    nums_range = nums_max - nums_min + 1
    counts = [0 for _ in range(nums_range)]

    for num in nums:
        counts[num - nums_min] += 1

    for i in range(1, nums_range):
        counts[i] += counts[i-1]

    res = [0 for _ in range(len(nums))]

    for i in range(len(nums)-1, -1 ,-1):
        num = nums[i]
        res[counts[num - nums_min] - 1 ]= num
        counts[nums[i]- nums_min] -=1
    return res

