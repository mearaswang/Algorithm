def insertion(nums):

    for i in range(1, len(nums)):
        #Traverse unsorted interval
        inser = nums[i]
        j = i

        while j > 0 and nums[j - 1] > inser: 
            # Traverse from right to left
            nums[j] = nums[j-1]
            j -= 1
        
        nums[j] = inser

    return nums

