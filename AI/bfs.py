from collections import deque

romania_map = {
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
    'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}

def bfs(graph, start, goal):
    """Breadth-first search"""
    queue = deque([(start,[start])])
    while queue:
        (vertex,path) = queue.popleft()
        for next_node in graph[vertex]:
            if next_node in path:
                continue
            if next_node == goal:
                return path + [next_node]
            queue.append((next_node,path + [next_node]))

    # return None

    # queue = deque([(start, [start])])
    # while queue:
    #     (vertex, path) = queue.popleft()
    #     for next_node in graph[vertex]:
    #         if next_node in path:
    #             continue
    #         if next_node == goal:
    #             return path + [next_node]
    #         queue.append((next_node, path + [next_node]))
    return None

start = 'Arad'
goal = 'Bucharest'
path = bfs(romania_map, start, goal)
print(f"Path from {start} to {goal}: {path}")