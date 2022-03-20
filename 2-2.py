from utils.timer import timer


@timer
def brute_force(height: list):
    max_area = 0
    for i in range(len(height)-1):
        for j in range(1, len(height)):
            h = min(height[i], height[j])
            w = j - i
            max_area = max(max_area, w*h)
    return max_area


@timer
def two_pointer(height: list):
    max_area = 0
    left, right = 0, len(height)-1
    while left != right:
        area = (right - left) * min(height[left], height[right])
        max_area = max(max_area, area)
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return max_area


brute_force([1, 8, 6, 2, 5, 4, 8, 3, 7])
two_pointer([1, 8, 6, 2, 5, 4, 8, 3, 7])
brute_force([1, 4, 6, 5, 3, 7, 6, 2])
two_pointer([1, 4, 6, 5, 3, 7, 6, 2])
