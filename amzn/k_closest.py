

def closest(points, k):
    # (X1-0)2 * (X2-0)2
    points.sort(key=lambda P: P[0]**2 + P[1]**2)
    return points[:k]


points = [[3, 3], [5, -1], [-2, 4]]
k = 2
print(closest(points, k))
