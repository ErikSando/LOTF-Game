import math
import random

world_height = 15
world_length = 100

def generate_world():
    output = []

    halfway_x = math.floor(world_length / 2)
    halfway_y = math.floor(world_height / 2)

    for i in range(1, world_height):
        output.append([])

        for v in range(1, world_length):
            output[i][v] = 0

    output[halfway_y][halfway_x] = 2

    total_elevation = 0

    for i in range(halfway_x + 1, world_length):
        elevation = random.randint(-1, 1)

        if total_elevation + elevation > 5 or total_elevation + elevation < 5: elevation = 0

        output[halfway_y + total_elevation + elevation][i] = 2

    x = halfway_x - 1

    while(x > 0):
        elevation = random.randint(-1, 1)

        if total_elevation + elevation > 5 or total_elevation + elevation < 5: elevation = 0

        output[halfway_y + total_elevation + elevation][i] = 2

        x -= 1

    print(output)

    return output