def revert(array, i, j):
    reverted = array[:i]
    for k in range(j - i + 1):
        reverted += [array[j - k]]
    return reverted + array[j+1:]


def make_array(number, indices):
    array = [i for i in range(1, number + 1)]
    for i in range(number - 1, 0, -1):
        j = indices[i-1] + i - 1
        array = revert(array, i-1, j-1)
    return array


def calculate_solution(number, cost):
    indices = (number - 1) * [1]
    cost -= (number - 1)

    indices = reduce(number, cost, indices)

    if len(indices) != number-1:
        return []

    return make_array(number, indices)


def reduce(number, cost, indices):
    if cost == 0:
        return indices
    for i in range(1, number):
        for j in range(1, number + 1 - i):
            cost -= 1
            indices[i-1] += 1
            if cost == 0:
                return indices

    return []


def main():
    T = int(input())
    for case in range(1, T + 1):
        N, C = [int(i) for i in input().split(" ")]
        result = calculate_solution(N, C)
        answer = " ".join([str(r) for r in result]) if len(result) == N else "IMPOSSIBLE"
        print("Case #{}: {}".format(case, answer))


if __name__ == '__main__':
    main()
