# s = "5F3Z-2e-9-w"
# k = 4
# s = "2-5g-3-J"
# k = 2
s = "2"
k = 2


def solution_1():
    tmp_result = []
    tmp_str = ''
    for i in s.split('-')[::-1]:
        tmp_str = i + tmp_str
        if len(tmp_str) == k:
            tmp_result.insert(0, tmp_str)
            tmp_str = ''

    if tmp_str:
        tmp_result.insert(0, tmp_str)

    print('-'.join(tmp_result).upper())

# def solution_2():
tmp_s = ''.join(s.split('-')).upper()
first_len = len(tmp_s) % k
other_num = len(tmp_s) // k

if first_len:
    result = tmp_s[:first_len]
else:
    result = ''
if other_num and result:
    result = result + '-' + '-'.join([tmp_s[first_len + k * i:first_len+k*(i + 1)] for i in range(other_num)])
elif not result:
    result = '-'.join([tmp_s[first_len + k * i:first_len+k*(i + 1)] for i in range(other_num)])

print(result)
