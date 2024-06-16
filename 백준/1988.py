def calculate_count(min_dist, distes):
    count = 0
    before = 0

    for idx, dist in enumerate(distes):
        if dist - before < min_dist:
            count += 1
        else:
            before = dist
    return count


if __name__ == "__main__":
    d, n, m = map(int, input().split())
    distes = list(int(input()) for _ in range(n)) + [d]
    distes.sort()

    left  = 0
    right = d + 1
    answer = -1

    while left < right:
        mid = (left + right)
        count = calculate_count(mid, distes)

        if count > m:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1

    print(answer)
