from queue import PriorityQueue

graphy = {
    'Arad': {'Sibiu': 140, 'Zerind': 75, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138},
    'Rimnicu': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},   
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Iasi': 92, 'Urziceni': 142},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}


def uniform_cost(graphy,source,destination):
    priority_queue, visited = PriorityQueue(),{}
    priority_queue.put((0, source, [source]))
    visited[source] = 0
    while not priority_queue.empty():
        (cost, vertex, path)  = priority_queue.get()
        if vertex == destination:
            return cost, path
        for neighbour in graphy[vertex]:
            cost +=graphy[vertex][neighbour]
            if neighbour not in visited or visited[neighbour] > cost:
                visited[neighbour] = cost
                priority_queue.put((cost, neighbour, path + [neighbour]))
    return -1, None


if __name__ == "__main__":
    source, destination = 'Arad', 'Bucharest'
    cost, path = uniform_cost(graphy, source, destination)
    if cost != -1:
        print(f"Path: {' -> '.join(path)}\nCost: {cost}")
    else:
        print(f"No path exists between {source} and {destination}")