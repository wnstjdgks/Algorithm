from typing import List
import bisect

def can_shoot(max_distance: int, bird_x: int, bird_y: int, shooters: List[int]) -> bool:
    closest_shooter_distance = find_closest_shooter_distance(bird_x, shooters)
    return closest_shooter_distance + bird_y <= max_distance

def find_closest_shooter_distance(bird_x: int, shooters: List[int]) -> int:
    left_index = bisect.bisect_left(shooters, bird_x)
    right_index = bisect.bisect_right(shooters, bird_x)
    left_index = adjust_index(left_index, shooters)

    left_distance = calculate_distance(bird_x, shooters[left_index])
    right_distance = calculate_distance(bird_x, shooters[right_index - 1])

    return min(left_distance, right_distance)

def adjust_index(index: int, shooters: List[int]) -> int:
    return index if index < len(shooters) else index - 1

def calculate_distance(point_a: int, point_b: int) -> int:
    return abs(point_a - point_b)

if __name__ == "__main__":
    M, N, L = map(int, input().split())
    shooters = list(map(int, input().split()))
    shooters.sort()

    birds = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for bird_x, bird_y in birds:
        if can_shoot(max_distance=L, bird_x=bird_x, bird_y=bird_y, shooters=shooters):
            result += 1

    print(result)