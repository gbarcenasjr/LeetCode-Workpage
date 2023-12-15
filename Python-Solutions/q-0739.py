temp_example = [73, 74, 75, 71, 69, 72, 76, 73]


def dailyTemperatures(temperatures: list[int]):
    ans = [0] * len(temperatures)
    stack = []

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            tempt, tempi = stack.pop()
            ans[tempi] = i - tempi
        stack.append([t, i])
    return ans

print(dailyTemperatures(temp_example))
