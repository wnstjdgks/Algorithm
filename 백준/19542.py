def find_max_depth(node : int):
    visited[node] = True

    if len(tree[node]) == 0:
        max_depths[node] = 0
        return 0

    max_depth = 0
    for next_node in tree[node]:
        if not visited[next_node]:
            max_depth = max(max_depth, find_max_depth(next_node) + 1)

    max_depths[node] = max_depth
    return max_depths[node]


def calculate_cost(node : int):

    visited_node[node] = True

    if max_depths[node] <= D:
        return 2

    cost = 2

    for next_node in tree[node]:
        if visited_node[next_node]:
            continue

        if max_depths[next_node] >= D:
            current = calculate_cost(next_node)
            cost += current

    return cost

if __name__ == "__main__":
    N, S, D = map(int, input().split())
    tree = [[] for _ in range(N + 1)]

    for _ in range(N - 1):
        x, y = map(int, input().split())
        tree[x].append(y)
        tree[y].append(x)

    max_depths = [0 for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]
    visited_node = [False for _ in range(N + 1)]

    find_max_depth(S)
    print(calculate_cost(S) - 2)