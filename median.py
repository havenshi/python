from sys import argv

nums = argv[1:]
for i, value in enumerate(nums):
    nums[i] = float(value)
nums.sort()
if len(nums) % 2 == 0:
    median = (nums[len(nums)/2- 1] + nums[len(nums)/2]) / 2
else:
    median = nums[len(nums)]
print median
