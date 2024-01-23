# функция для нахождения корня множества
def find(parent, v):
    # если вершина v не является корнем своего множества, рекурсивно ищем корень
    if parent[v] != v:
        parent[v] = find(parent, parent[v])  # обновляем родителя вершины v
    return parent[v]


# функция для объединения двух множеств
def union(parent, rank, v1, v2):
    # находим корни множеств для вершин v1 и v2
    root1 = find(parent, v1)
    root2 = find(parent, v2)

    # если корни разные, выбираем корень с меньшим "рангом" в качестве нового родителя
    if root1 != root2:
        if rank[root1] < rank[root2]:
            parent[root1] = root2
        elif rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            # если ранги одинаковы, выбираем любой корень и увеличиваем его ранг
            parent[root1] = root2
            rank[root2] += 1


# функция для алгоритма Краскала
def kruskal(edges, vertices):
    # сортируем рёбра по их весу (по возрастанию)
    edges.sort(key=lambda x: x[2])

    # инициализируем родительские вершины и ранги множеств
    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}

    # инициализируем список рёбер остовного дерева
    mst = []

    # проходим по всем рёбрам, начиная с самого легкого
    for edge in edges:
        v1, v2, weight = edge
        # проверяем, не принадлежат ли вершины v1 и v2 к одному множеству (избегаем цикла)
        if find(parent, v1) != find(parent, v2):
            # если не принадлежат, объединяем множества
            union(parent, rank, v1, v2)
            # добавляем ребро в остовное дерево
            mst.append([v1, v2])

    return mst


edge_list = [[1, 5], [1, 3], [1, 7], [2, 5], [2, 6], [2, 7], [3, 4], [3, 8], [4, 8], [6, 7]] #Список рёбер

# получение уникальных вершин из списка рёбер
vertices = set()
for edge in edge_list:
    vertices.update(edge)

# преобразование списка рёбер в формат, под алгоритм Краскала
edges = []
for edge in edge_list:
    v1, v2 = edge
    edges.append([v1, v2, 1])

# построение остовного дерева
mst = kruskal(edges, list(vertices))


print("Остовное дерево:")
for edge in mst:
    print(edge)

