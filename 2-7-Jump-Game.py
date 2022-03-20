from utils.timer import timer


@timer
def recursive_solution(nums):
    def jump(nums, position):
        if position == len(nums) - 1:
            return True

        next_step_max = min(position + nums[position], len(nums) - 1)

        for i in range(next_step_max, position, -1):
            # print(position, nums[position], next_step_max, i)
            if jump(nums, i):
                return True
        return False
    return jump(nums, 0)


@timer
def dp_solution(nums):
    if len(nums) == 1:
        return True
    last_index = len(nums)-1
    next_index_list = [min(i+v, last_index) for i, v in enumerate(nums)]
    tmp = []
    tmp.append(next_index_list[0])
    i = 0
    while len(tmp) > i:
        if tmp[i] >= last_index:
            return True
        else:
            for j in range(len(tmp), tmp[i] + 1):
                tmp.append(next_index_list[j])
        i += 1
    return False


@timer
def dp_solution_top_down(nums):
    memo = [0 for i in range(len(nums))]    # Unknown: 0, Good: 1, Bad: 2
    memo[-1] = 1

    def jump(nums, position):
        if memo[position] != 0:
            return memo[position] == 1
        furthestJump = min(position+nums[position], len(nums)-1)
        for i in range(position+1, furthestJump+1):
            if jump(nums, i):
                memo[position] = True
                return True
        memo[position] = 2
        return False
    return jump(nums, 0)


recursive_solution([2,3,1,1,4])
dp_solution([0,2,3])
dp_solution([3,2,1,0,4])
dp_solution([2,3,1,1,4])
dp_solution([1,2,3])

dp_solution_top_down([0,2,3])
dp_solution_top_down([3,2,1,0,4])
dp_solution_top_down([2,3,1,1,4])
dp_solution_top_down([1,2,3])