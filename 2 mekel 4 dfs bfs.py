graph = {
    "A": ["A1", "A2", "A3"],
    "A1" :["B1", "B20"],
    "B1" :["C10"],
    "C10": [],
    "B20" :[],
    "A2" :["D10", "D2"],
    "D10": [],
    "D2": ["E10"],
    "E10": [],
    "A3" :["F10"],
    "F10": [],
}

# #----------
# #   dfs
# #----------

# visited = set()
# count = 0

# def dfs(node):
#     global count
#     if node not in visited:
#         print(node)
#         visited.add(node)
#         count += 1
#         for neighbor in graph[node]:
#             dfs(neighbor)

# dfs('A')

# total_rooms = len(graph)
# print(f"Visited {count} out of {total_rooms} rooms.")



#----------
#   bfs
#----------

visited = set()
count = 0
queue = ['A']

while queue:
    node = queue.pop(0)
    if node not in visited:
        print(node)
        visited.add(node)
        count += 1
        for neighbor in graph[node]:
            queue.append(neighbor)

total_rooms = len(graph)
print(f"Visited {count} out of {total_rooms} rooms.")