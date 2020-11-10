"""
Given a list of integers and a target value, return the indices of the two numbers in the list that add up to a specific target.

*Note: You can assume that each input has exactly one solution, and the same element cannot be used more than once.*

Example:

Given nums = [3, 8, 12, 17], target = 15,

Because nums[0] + nums[2] = 3 + 12 = 15,
return [0, 2].
"""

# What is UPER?

###### Understand ######

# Return the indices (of the numbers that add up to the target)
# What's our input: nums (list of integers), target (int)
# Edge Cases:
# What if no combo of numbers sum up to the target? -- We are told we can assume each input has exactly one solution
# nums can be arbitrary length

###### Plan ######

# can't sort the list because we lose the original indices

# see below


###### Execute ######

# see below

###### Reflect / Revise ######

def two_sum(nums, target):
    # Your code here
    # how do we return the index and not the value?
    # iterate over nums list using range so that we have access to the indices
    for idx1 in range(len(nums)):
        # check if the current number + any of the rest of the numbers == target
        # use another loop to go over the rest of the numbers:
        for idx2 in range(idx1, len(nums)):
            # sum them up and compare against the target
            sum = nums[idx1] + nums[idx2]
            # if they're equal:
            if sum == target:
                # grab their indices and return them as a list [num1, num2]
                return [idx1, idx2]


result = two_sum([3, 8, 12, 17], 15)
print(result)
