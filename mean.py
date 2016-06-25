from sys import argv

nums = argv[1:]
for i, value in enumerate(nums):
    nums[i]=float(value)
mean=sum(nums)/len(nums)
print mean
