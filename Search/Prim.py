cost  = [[0, 4, 4, 0, 0, 0],
         [4, 0, 2, 0, 0, 0],
         [4, 2, 0, 3, 1, 6],
         [0, 0, 3, 0, 0, 2],
         [0, 0, 1, 0, 0, 3],
         [0, 0, 0, 2, 3, 0]]
selected = [0, 0, 0, 0, 0, 0]

def min_path_to_end(cost, start_node):
    mincost = 0
    selected[0] = True
    path = [len(cost) - 1]
    edge_count = 0

    while (edge_count < len(cost) - 1):    
        minimum = 9999
        x = 0
        y = 0
        for start_node in range(len(cost)):
            if selected[start_node]:
                for j in range(len(cost)):
                    if ((not selected[j]) and cost[start_node][j]):  
                        if minimum > cost[start_node][j]:
                            minimum = cost[start_node][j]
                            x = start_node
                            y = j
        print('Edge {}:({}, {}) cost:{}'.format(edge_count, x, y, cost[x][y]))
        selected[y] = True
        edge_count += 1
        mincost += minimum
        path.append(mincost)
    return path[::-1]

def Prim(cost,start_node):
    if (start_node == len(cost) - 1):
        print('You has already been at the destination!')
        return    

    min_path_list = min_path_to_end(cost,start_node)
    print(f"Minimum cost= {min_path_list}")

Prim(cost, 0)