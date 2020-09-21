# Example 1:

# Input: [1,2,3]
# Output: 6

#3,2,1
class Solution:
    def maximumProduct(self, nums):
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3],nums[-1]*nums[0]*nums[1])


example = Solution()
numso = [1, 3, 6, 5, 4]
example.maximumProduct(numso)

print(example.maximumProduct(numso))


-4, -3, -2, -1, 60

print( max(1,2,4))