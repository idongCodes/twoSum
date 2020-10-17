'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

def two_sum(nums, target):

   # initialise empty dictionary
   x = {}
            
   # Loop through each number in arr
   # enumerate() returns index of ea. item in arr
   for i, n in enumerate(nums):

        # Find num in arr that when added to 'n' sums up to target
        # Store that num to a variable
        d = target - n

        # while stored num is not in dict. 'x'
        if d not in x:

            # get index (from enumerate()) of stored num
            x[n] = i

        else:

            # else return index both indexes
            print(f"{[x[d], i]}")
                   
nums = [2,7,11,15]
target = 9
two_sum(nums, target)

nums = [3,2,4]
target = 6
two_sum(nums, target)

nums = [3,3]
target = 6
two_sum(nums, target)
