graph = [[0, 4, 4, 0, 0, 0],
         [4, 0, 2, 0, 0, 0],
         [4, 2, 0, 3, 1, 6],
         [0, 0, 3, 0, 0, 2],
         [0, 0, 1, 0, 0, 3],
         [0, 0, 0, 2, 3, 0]]
def min_node_val(node_vals, visited_nodes):
    min_val = float('inf')
    min_index = -1

    for i in range(len(node_vals)):
        if node_vals[i] < min_val and i not in visited_nodes:
            min_val = node_vals[i]
            min_index = i

    return min_index
def find_min(index_list, val_list):
    min_val = val_list[0]
    min_index = index_list[0]
    for i in range(len(val_list)):
        if(val_list[i] < min_val):
            min_val = val_list[i]
            min_index = index_list[i]
    return min_index
def min_time_to_nodes(graph, start_node):
    node_vals = [float('inf')] * len(graph)
    
    node_vals[start_node] = 0

    visited_nodes = []

    for i in range(len(graph)):

        current_node = min_node_val(node_vals, visited_nodes)

        visited_nodes.append(current_node)

        # distances from current node to other nodes
        distances_from_current = graph[current_node]

        for j in range(len(graph)):
            if distances_from_current[j] != 0:

                updated_node_val = node_vals[current_node] + distances_from_current[j]

                if updated_node_val < node_vals[j]:
                    node_vals[j] = updated_node_val
    return node_vals
def min_path_to_end(min_time_list, start_node):
    cont = True
    current_node = graph[-1]
    path = [len(graph) - 1]
    while (cont == 1):
        neibor_node_index = [i for i in range(len(current_node)) if current_node[i] > 0]
        # print(neibor)
        neibor_node_val = list(map(lambda index: min_time_list[index], neibor_node_index))
        # print(neibor_val)
        min_neibor = find_min(neibor_node_index, neibor_node_val)
            
        path.append(min_neibor)
        current_node = graph[min_neibor]

        if(min_neibor == start_node):
            cont = False
            break
    return path[::-1]
def dijkstra_algorithm(graph, start_node):
    if (start_node == len(graph) - 1):
        print('You has already been at the destination!')
        return
    min_time_list = min_time_to_nodes(graph, start_node)

    min_path_list = min_path_to_end(min_time_list, start_node)
    print(f'Shortest path: {min_path_list}')
    print(f'Min time to each node: {min_time_list}')

shortest_distances = dijkstra_algorithm(graph, 0)