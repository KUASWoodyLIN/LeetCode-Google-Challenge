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


# best implement
@timer
def solution_3(fruits):
    max_number = 0
    sliding_window = []
    items_tmp = []
    for i in fruits:
        sliding_window.append(i)
        if i not in items_tmp:
            if len(items_tmp) == 2:
                keep_item = sliding_window[-2]
                items_tmp.remove(keep_item)
                remove_item = items_tmp[0]
                items_tmp = [keep_item, i]
                remove_last_idx = sliding_window[::-1].index(remove_item)
                sliding_window = sliding_window[-remove_last_idx:]
            else:
                items_tmp.append(i)
                max_number = max(max_number, len(sliding_window))
        else:
            max_number = max(max_number, len(sliding_window))
    return max_number

# test = [1,2,1]                    # 3
# test = [3,3,3,1,2,1,1,2,3,3,4]    # 5
# test = [0,1,2,2]                  # 3
# test = [0]                        # 1
# test = [1,0,3,4,3]                  # 3
# test = [0 for _ in range(1000)]
test = [4,1,1,1,3,1,7,5]

# print(solution_1(test)) #51.8s
# print(solution_2(test)) #51.8s
print(solution_3(test)) #51.8s