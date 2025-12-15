#8. gci hatum
def orient(a, b, c):
    val = (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
    if val > 0: return 1
    if val < 0: return -1
    return 0

def on_segment(a, b, c):
    return (min(a[0], b[0]) <= c[0] <= max(a[0], b[0]) and
            min(a[1], b[1]) <= c[1] <= max(a[1], b[1]))

def segments_intersect(p1, p2, q1, q2):
    o1 = orient(p1, p2, q1)
    o2 = orient(p1, p2, q2)
    o3 = orient(q1, q2, p1)
    o4 = orient(q1, q2, p2)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and on_segment(p1, p2, q1): return True
    if o2 == 0 and on_segment(p1, p2, q2): return True
    if o3 == 0 and on_segment(q1, q2, p1): return True
    if o4 == 0 and on_segment(q1, q2, p2): return True

    return False

print(segments_intersect((1,1), (4,4), (1,4), (4,1)))  # True
print(segments_intersect((1,1), (2,2), (3,3), (4,4)))  # False