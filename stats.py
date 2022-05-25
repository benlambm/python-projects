def main():
    nums = [3, 1, 7, 1, 4, 10]
    nums.sort()
    print("List ordered:", nums)
    print("Mean: ", mean(nums))
    print("Median: ", median(nums))
    print("Mode: ", mode(nums))

def mean(nums):
    if not nums:
        return 0
    total = 0
    for num in nums:
        total += num
    return total / len(nums)
def median(nums):
    if not nums:
        return 0
    midpoint = len(nums) // 2
    if len(nums) % 2 == 1:
        return nums[midpoint]
    else:
        return (nums[midpoint] + nums[midpoint - 1]) / 2
def mode(nums):
    if not nums:
        return 0
    numDict = {}
    for num in nums:
        number = numDict.get(num, None)
        if number == None:
            numDict[num] = 1
        else:
            numDict[num] = number + 1
    theMax = max(numDict.values())
    for x in numDict:
        if numDict[x] == theMax:
            return x
main()
