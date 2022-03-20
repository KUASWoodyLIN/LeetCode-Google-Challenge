from utils.timer import timer


@timer
def brute_force(nums: list) -> list:
    result = []
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    add_list = sorted([nums[i], nums[j], nums[k]])
                    if add_list not in result:
                        result.append(add_list)
    return result


@timer
def two_pinter(nums: list) -> list:
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if nums[i] > 0:
            break
        if i == 0 or nums[i - 1] != nums[i]:

            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1

                else:
                    # if [nums[i], nums[left], nums[right]] not in result:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    if left < right and nums[left] == nums[left-1]:
                        left += 1
                    # break
    return result




# brute_force([-1,0,1,2,-1,-4])
# two_pinter([-1,0,1,2,-1,-4])
# two_pinter([0,0,0,0])
# two_pinter([-2,0,1,1,2])
two_pinter([-2,0,0,2,2])
