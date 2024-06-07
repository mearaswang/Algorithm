# Use LC 11 as an example
def maxArea(height):
    left, right = 0, len(height) - 1
    result = 0      # stores the current max area
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        result = max(result, area)

        # Since we have to move the pointer anyways, either to the right or to the left
        # both ways shorten the width by 1
        # Hence we keep the hihger pointer
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return result