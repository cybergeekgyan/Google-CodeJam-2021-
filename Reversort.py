def process_input(inputs):
    output = []
    for input in inputs:
        N, nums = input
        nums = [int(item) for item in nums.split(' ')]
        score = 0
        for i in range(1,len(nums)+1):
            j = nums.index(i) # j is now the index of the element we are going to sort.
            nums[i-1:j+1] = reversed(nums[i-1:j+1])
            score += j-i+2
        output.append(score-1)
    return output


if __name__ == "__main__":
    T = int(input())
    inputs = []
    for _ in range(T):
        N = int(input())
        str = input()
        inputs.append([N, str])

    output_lines = process_input(inputs)

    i = 1
    for l in output_lines:
        print("Case #{}: {}".format(i, l))
        i += 1
