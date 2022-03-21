from utils.timer import timer


@timer
def solution(digits):
    carry = 0
    digits[-1] += 1
    for i in range(len(digits) - 1, -1, -1):
        tmp = digits[i] + carry
        carry = tmp // 10
        if carry:
            digits[i] = tmp % 10
        else:
            digits[i] = tmp
            break
    if carry == 1:
        digits.insert(0, 1)
    return digits


solution([9,9])
