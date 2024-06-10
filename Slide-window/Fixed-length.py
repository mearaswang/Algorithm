# use LC 1343 as an example
def numofSub(arr, k, threshold):
    left, right = 0, 0      #Initiate left and right to be 0
    ans = 0                 #The count/return value
    window_sum = 0          #Use this to track window sum directly instead of using an actual list

    while right < len(arr):
        # Traverse whole list until right reaches the end
        window_sum += arr[right]    #Expand the window

        if right - left + 1 >= k:
            #Window reaches or over the reuired size
            #Test requirement first
            if window_sum >= k*threshold:    #We use multiply instead of divide
                ans += 1    #Update ans since this statisfies the requirement
            
            #Slide the window's left boundary to the right by 1
            #Delete the leftest value
            window_sum -= arr[left]
            left += 1
        
        right += 1      # Slide the window to the right

    return ans