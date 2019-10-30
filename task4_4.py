"""
There are a number of spherical balloons spread in two-dimensional space.
For each balloon, provided input is the start and end coordinates of the
horizontal diameter. Since it's horizontal, y-coordinates don't matter
and hence the x-coordinates of start and end of the diameter suffice.
Start is always smaller than end. There will be at most 10^4 balloons.

An arrow can be shot up exactly vertically from different points along the
x-axis. A balloon with xstart and xend bursts by an arrow shot at x
if xstart ≤ x ≤ xend. There is no limit to the number of arrows that
can be shot. An arrow once shot keeps travelling up infinitely.
The problem is to find the minimum number of arrows that must be shot
to burst all balloons.

example:
input
10,16 2,8 1,6 7,12

output
2
"""


def find_minimal_arrows(points):
    result = 0
    points.sort(key=lambda x: x[1], reverse=True)
    while points:
        result += 1
        current = points.pop()[1]
        while points and points[-1][0] <= current:
            points.pop()

    return result


points = [point.split(',') for point in input().split(' ')]
points = [[float(point[0]), float(point[1])] for point in points]

print(find_minimal_arrows(points))
