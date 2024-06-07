# Use LC 26 as the example
def removeDup(nums):
    if len(nums) <= 1:
        return len(nums)
    slow, fast = 0, 1

    while fast < len(nums):
        # loop for the whole list, fast moves anyways
        # When encounters different elements, replace slow's next value to be the value of fast
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]
        fast += 1
    return slow + 1     #Since it is 0-indexed