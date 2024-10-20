# Define the graph for the Romanian map
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

def dfs(graph, start, goal, path=None, visited=None):
    """Depth-first search"""
    if path is None:
        path = [start]
    if visited is None:
        visited = {start}
    if start == goal:
        return path
    for next_node in graph[start]:
        if next_node in visited:
            continue
        visited.add(next_node)
        new_path = dfs(graph, next_node, goal, path + [next_node], visited)
        if new_path:
            return new_path
    return None

# Example usage
start_city = 'Arad'
goal_city = 'Bucharest'
path = dfs(romania_map, start_city, goal_city)

if path:
    print(f"Path from {start_city} to {goal_city}: {' -> '.join(path)}")
else:
    print(f"No path found from {start_city} to {goal_city}")