def twoSum(numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1
    while numbers[left] + numbers[right] != target:
        if numbers[left] + numbers[right] > target:
            right -= 1
        else:
            left += 1
    return [left + 1, right + 1]

numbers_from_example = [2, 7, 11, 15]
target_from_example = 9

print(twoSum(numbers_from_example, target_from_example))