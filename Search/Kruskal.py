cost = [[0, 4, 4, 0, 0, 0],
        [4, 0, 2, 0, 0, 0],
        [4, 2, 0, 3, 1, 6],
        [0, 0, 3, 0, 0, 2],
        [0, 0, 1, 0, 0, 3],
        [0, 0, 0, 2, 3, 0]]

parent = [i for i in range(len(cost))]

def find(i):
    while parent[i] != i:
        i = parent[i]
    return i
 
def union(i, j):
    a = find(i)
    b = find(j)
    parent[a] = b
    
def min_path_to_end(cost, start_node):
    mincost = 0 
 
    for start_node in range(len(cost)):
        parent[start_node] = start_node
    path = [len(cost) - 1]
    edge_count = 0
    while edge_count < len(cost) - 1:
        min = float('inf')
        a = -1
        b = -1
        for start_node in range(len(cost)):
            for j in range(len(cost)):
                if find(start_node) != find(j) and cost[start_node][j] < min and cost[start_node][j] > 0:
                    min = cost[start_node][j]
                    a = start_node
                    b = j
        union(a, b)
        print('Edge {}:({}, {}) cost:{}'.format(edge_count, a, b, min))
        edge_count += 1
        mincost += min
        path.append(mincost)
    return path[::-1]

def kruskalMST(cost,start_node):
    if (start_node == len(cost) - 1):
        print('You has already been at the destination!')
        return    

    min_path_list = min_path_to_end(cost,start_node)
    print(f"Minimum cost= {min_path_list}")
 
kruskalMST(cost,0)