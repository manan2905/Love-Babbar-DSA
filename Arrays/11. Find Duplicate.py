def findDuplicate(nums):
    # sorting
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]


def findDuplicate2(nums):
    # hashset
    s = set()
    for ele in nums:
        if ele not in s:
            s.add(ele)
        else:
            return ele


def findDuplicate3(nums):
    # freq array
    new = [0] * len(nums)
    for i in range(len(nums)):
        new[nums[i]] += 1
        if new[nums[i]] == 2:
            return nums[i]


def findDuplicate4(nums):
    # Approach 4: Negative Marking
    # flip the signs of the elements
    # without modifying wali condition fail
    for i in range(len(nums)):
        ind = abs(nums[i])
        if nums[ind] < 0:
            return ind
        nums[ind] = -nums[ind]


# Logic : har element se kitne chhote elements array me present hai:
# Jab bhi ek duplicate exist krega to vo ek number par count exceed karjayega and that is our answer
def findDuplicate5(nums):
    # binary search approach
    s, e = 0, len(nums) - 1
    ans = -1
    while s <= e:
        mid = (s + e) // 2
        count = 0
        for i in range(1, len(nums)):
            if nums[i] <= mid:
                count += 1
        if count > mid:
            ans = mid
            e = mid - 1
        else:
            s = mid + 1
    return ans


def findDuplicate6(nums):
    # Floyd's tortoise and Hare
    pass


arr = [int(i) for i in input().split()]
print(findDuplicate5(arr))
