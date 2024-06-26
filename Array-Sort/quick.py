import random

def randomPartition(nums, low, high):
    ## Set a random initial pivot, to minimize the impact of worst case
    ## Achieved by: choose a random number, and swap it with the lower boundary
    i = random.randint(low, high)
    nums[i], nums[low] = nums[low], nums[i]
    return partition(nums, low, high)


def partition(nums, low, high):
    # Set the pivot to the lower boundary generated by the random initializaiton step
    pivot = nums[low]

    i, j = low, high
    while i < j:
        #loop until i=j
        while i < j and nums[j] >= pivot:
            #From right to left, find the first value samller than pivot
            j -= 1
        
        while i < j and nums[i] <= pivot:
            #From left to right, find the first value greather than pivot
            i += 1
        #Swap valus in i and j
        nums[i], nums[j] = nums[j], nums[i]

    # Return the index of the pivot should be placed
    # At this stage, the left side of pivot are all smaller than it, and the right side are all greater than it.
    return i

def quickSort(nums, low, high):
    # recursively apply random and partition for each interval
    # Until the gap is 1
    if low < high:
        pivot_i = randomPartition(nums, low, high)
        quickSort(nums, low, pivot_i - 1)
        quickSort(nums, pivot_i + 1, high)

    return nums