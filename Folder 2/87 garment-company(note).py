import math

def count_square_plots(areas):
    count = 0
    for area in areas:
        root = math.sqrt(area)
        if int(root + 0.5) ** 2 == area:
            count += 1
    return count

N, *areas = map(int, input().split())
print(count_square_plots(areas))