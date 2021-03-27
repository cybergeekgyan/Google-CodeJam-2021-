# the problem can be abstracted away as a binary sort.
def binarySortSolve(N):
    # constantly ping the judge.

    #initial case
    print("1 2 3")
    response = int(input())
    if response == 1:
        solution = [2, 1, 3]
    elif response == 2:
        solution = [1, 2, 3]
    else:
        solution = [1, 3, 2]

    remaining = list(range(4,N+1)) #remaining elements to sort.

    for element in remaining:
        startpoint = 0
        endpoint = len(solution)
        while True:
            midpoint = int((startpoint + endpoint)/2)
            if startpoint == 0 and endpoint == 1:
                print(str(solution[0]) + ' ' + str(solution[1]) + ' ' + str(element))
                response = int(input())
                if response == solution[0]:
                    solution.insert(0,element)
                    break
                else:
                    solution.insert(1,element)
                    break
            elif startpoint == len(solution)-1 and endpoint == len(solution):
                print(str(solution[len(solution)-2]) + ' ' + str(solution[len(solution)-1]) + ' ' + str(element))
                response = int(input())
                if response == solution[len(solution)-1]:
                    solution.insert(len(solution),element)
                    break
                else:
                    solution.insert(len(solution)-1,element)
                    break
            print(str(solution[midpoint-1]) + ' ' + str(solution[midpoint]) + ' ' + str(element))
            response = int(input())
            if response == element:
                #we've found the right spot
                solution.insert(midpoint, element)
                break
            elif response == solution[midpoint-1]: #it's to the left
                endpoint = midpoint
                continue
            elif response == solution[midpoint]:
                startpoint = midpoint
                continue

    print(*solution)
    input()


if __name__ == "__main__":
    T, N, Q = [int(item) for item in input().split(' ')]
    inputs = []
    for _ in range(T):
        binarySortSolve(N)
