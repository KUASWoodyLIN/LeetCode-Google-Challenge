from timer import timer

@timer
def solution_1(fruits):
    max_pick = 0
    j = 0
    for i in range(len(fruits)):
        tmp_set = {fruits[i]}
        for j in range(i+1, len(fruits)):
            if fruits[j] not in tmp_set:
                tmp_set.add(fruits[j])
            if len(tmp_set) > 2:
                j -= 1
                break
        if max_pick < j-i+1:
            max_pick = j-i+1
    return max_pick


@timer
def solution_2(fruits):
    max_pick = 0
    j = 0
    i = 0
    while i < len(fruits):
        tmp_set = {fruits[i]}
        last_continue_index = [i, fruits[i]]
        for j in range(i + 1, len(fruits)):
            tmp_set.add(fruits[j])
            if len(tmp_set) > 2:
                j -= 1
                break
            if last_continue_index[1] != fruits[j]:
                last_continue_index = [j, fruits[j]]
        if max_pick < j - i + 1:
            max_pick = j - i + 1
        if len(tmp_set) <= 2:
            i += 1
        else:
            i = last_continue_index[0]
        if j - last_continue_index[0] + 1 > len(fruits) // 2:
            break
    return max_pick


@timer
def solution_3(fruits):
    max_pick = 0
    tmp_list = [(0, fruits[0])]
    for i, v in enumerate(fruits[1:], 1):
        if v != tmp_list[-1][1]:
            tmp_list.append((i, v))

    # TODO: finish here
    tmp_set = []
    for i, v in tmp_list:
        if v not in tmp_set:
            tmp_set.append(v)
    print(tmp_list)
    return max_pick


# test = [1,2,1]                    # 3
test = [3,3,3,1,2,1,1,2,3,3,4]    # 5
# test = [0,1,2,2]                  # 3
# test = [0]                        # 1
# test = [1,0,3,4,3]                  # 3
# test = [0 for _ in range(1000)]

# print(solution_1(test)) #51.8s
# print(solution_2(test)) #51.8s
print(solution_3(test)) #51.8s