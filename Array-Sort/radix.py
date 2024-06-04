class Solution:
    # The key for this method is that each sorting in each digit will retain the correponding order
    def radixSort(self, nums):
        # The size is the number of digits of the max number
        size = len(str(max(nums)))

        for i in range(size): # loop for each digit
            # Initialize a bucket to store each digits
            buckets = [[] for _ in range(10)]

            for num in nums:
                # Based on the magnitude of the current digit, store number into corresponding bucket
                buckets[num // (10 ** i) % 10].append(num)

            nums.clear()
            # Clear the original list

            for bucket in buckets:
                # Based on the current order, append number inside each bucket back to nums list
                for num in bucket:
                    nums.append(num)

        return nums