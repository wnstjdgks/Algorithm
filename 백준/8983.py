from typing import List
import bisect

def can_shoot(max_distance: int, bird_x: int, bird_y: int, shooters: List[int]) -> bool:
    """
    Determines if a bird can be shot by any shooter given the maximum shooting distance.

    :param max_distance: The maximum distance a shooter can shoot.
    :param bird_x: The x-coordinate of the bird.
    :param bird_y: The y-coordinate of the bird.
    :param shooters: A list of x-coordinates representing the positions of the shooters.
    :return: True if the bird can be shot by any shooter within the max_distance, else False.
    """
    closest_shooter_distance = find_closest_shooter_distance(bird_x, shooters)
    return closest_shooter_distance + bird_y <= max_distance

def find_closest_shooter_distance(bird_x: int, shooters: List[int]) -> int:
    """
    Finds the minimum distance from bird to the nearest shooters.
    :param bird_x: The x-coordinate of the bird.
    :param shooters: A list of x-coordinates representing the positions of the shooters.
    :return: The minimum distance from the bird to the nearest shooter.
    """
    left_index = bisect.bisect_left(shooters, bird_x)
    right_index = bisect.bisect_right(shooters, bird_x)
    left_index = adjust_index(left_index, shooters)

    left_distance = calculate_distance(bird_x, shooters[left_index])
    right_distance = calculate_distance(bird_x, shooters[right_index - 1])

    return min(left_distance, right_distance)

def adjust_index(index: int, shooters: List[int]) -> int:
    """
    Adjusts the index if it is greater than the size of the shooters list.
    :param index: The index to be adjusted.
    :param shooters: A list of x-coordinates representing the positions of the shooters.
    :return: The adjusted index.
    """
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