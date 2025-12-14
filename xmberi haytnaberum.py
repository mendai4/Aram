#3. Կապակցված գագաթների խմբերի հայտնաբերում գրաֆերում 

def connected_components(graph):
    visited = set()
    comps = []

    for node in graph:
        if node in visited:
            continue
        stack = [node]
        comp = []
        visited.add(node)

        while stack:
            u = stack.pop()
            comp.append(u)
            for v in graph.get(u, []):
                if v not in visited:
                    visited.add(v)
                    stack.append(v)

        comps.append(comp)

    return comps

noder = {
    0: [1],
    1: [0, 2],
    2: [1],
    3: [4],
    4: [3],
    5: []
}

print(connected_components(noder))