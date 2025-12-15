#9 convex hull 

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def jarvis_march(points):
    if len(points) < 3:
        return points[:]

    left = min(points)
    hull = []
    p = left

    while True:
        hull.append(p)
        q = points[0]
        for r in points[1:]:
            if q == p or cross(p, q, r) < 0:
                q = r
        p = q
        if p == left:
            break

    return hull

pts = [(0,3),(2,2),(1,1),(2,1),(3,0),(0,0),(3,3)]
print(jarvis_march(pts))