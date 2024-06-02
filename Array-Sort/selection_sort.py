def selection_sort(nums):
    """
    >>> selection_sort([5,2,3,6,1,4])
    [1, 2, 3, 4, 5, 6]
    >>> selection_sort([9,4,2,4,3,1,9])
    [1, 2, 3, 4, 4, 9, 9]
    """

    for i in range(len(nums)-1):    #Traverse len(nums) -1 times, since one digit do not require a sort.
        min_i = i   # At the i_th traverse, initialize the minimum index at i 
        for j in range(i+1, len(nums)):
            # Update the minimum index
            if nums[min_i] > nums[j]:
                min_i = j
        
        if i != min_i:
            # Swap the values if the i_th value is not the minimum
            nums[i],nums[min_i] = nums[min_i],nums[i]
    return nums