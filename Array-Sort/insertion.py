def insertion(nums):

    for i in range(1, len(nums)):
        #Traverse unsorted interval
        inser = nums[i]
        j = i

        while j > 0 and nums[j - 1] > inser: 
            # Traverse from right to left
            nums[j] = nums[j-1]
            # shift the bigger number to the right for one index
            j -= 1
        
        nums[j] = inser
        # Insert the numer to the right index

    return nums

