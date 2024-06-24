def calculate(arr, stack):
    L = len(arr)
    values = [0] + arr
    total = [0] * (L + 1)

    for i in range(1, L + 1):
        total[i] = total[i - 1] + values[i]

    result = -int(1e9)
    result_pair = (0, 0)

    for i in range(L + 1):
        for j in range(i):

            tmp = total[i] - total[j]
            if result < tmp:
                result = tmp
                result_pair = (j + 1, i)

            if result == tmp and (i - (j + 1)) < result_pair[1] - result_pair[0]:
                result_pair = (j + 1, i)

    stack.append(result_pair)
    return result

if __name__ == "__main__":
    N = int(input())
    stack = []
    total = 0
    for _ in range(N):
        L = int(input())
        total += calculate(list(map(int, input().split())), stack)

    print(total)
    for x,y in stack:
        print(x,y)