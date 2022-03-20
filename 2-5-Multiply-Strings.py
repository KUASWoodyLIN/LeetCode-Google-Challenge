from utils.timer import timer


@timer
def multiply(num1: str, num2: str) -> str:
    num1 = num1[::-1]
    num2 = num2[::-1]
    results = []
    if len(num1) == 1 and num1 == '0':
        return '0'
    for i, b in enumerate(num2):
        results.append(multiply_str(num1, b, i))
    answer = sum_results(results)
    return answer


def multiply_str(num1, b, b_index):
    current_result = [0] * b_index
    carry = 0
    b = int(b)
    if not b:
        return [0]
    for a in num1:
        multiplication = int(a) * b + carry
        carry = multiplication // 10
        current_result.append(multiplication % 10)
    if carry != 0:
        current_result.append(carry)
    return current_result


def sum_results(results):
    carry = 0
    result = []
    for i in range(len(results[-1])):
        cur_sum = sum([r[i] for r in results if i < len(r)] + [carry])
        carry = cur_sum // 10
        result.insert(0, str(cur_sum % 10))
    if carry != 0:
        result.insert(0, str(carry))
    return ''.join(result)


multiply("9133", "0")
# multiply("0", "52")
