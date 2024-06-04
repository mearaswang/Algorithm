class Solution:
    def insertionSort(self, nums):
        # use insert sorting to sort inside the bucket
        for i in range(1, len(nums)):
            temp = nums[i]
            j = i

            while j > 0 and nums[j - 1] > temp:
                nums[j] = nums[j - 1]
                j -= 1
            
            nums[j] = temp
        return nums

    def bucketSort(self, nums, bucket_size = 5):
        # Set the boundaries for the bucket
        nums_min, nums_max = min(nums), max(nums)
        # Determine the number of buckets
        bucket_count = (nums_max - nums_min) // bucket_size + 1 
        # Buckets is an list contains a number of bucket_count empty lists
        buckets = [[] for _ in range(bucket_count)]

        for num in nums:
            # based on the magnititude of the num, append it to the corresponding sub list
            buckets[(nums - nums_min) // bucket_size].append(num)

        res = []
        # Initialize the result empty list

        for bucket in buckets:
            self.insertionSort(bucket) # For each bucket, sort it with insertSort method
            res.extend(bucket) # Extend the bucket

        return res