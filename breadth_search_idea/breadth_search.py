import queue


#--------------------------------
# Сложность BFS при списке смежности O(n + m)


def BFS(G, v):
    q = queue.Queue()
    q.put(v)

    while len(queue) > 0:
        # pop() - удаляет последний элемент из списка и возвращает его
        v = queue.pop(0)

        if not mark_vertaxes[v]:
            print(v)
            mark_vertaxes[v] = True

            # Двигаеся по всем вершинам, соседним с текущей v
            for w in G[v]:
                if not mark_vertaxes[w]:
                    q.put(w)

# G - список вершин графа
# n - число вершин в графе
n = 10

# G - список вершин ориентированного графа, Задается в виде списка смежности, cгенерируем список смежности

#!!!!!!!!!!!!!!!!!!!
G = [
    [1, 2],  # 1
    [3, 4],  # 2
    [5, 6],  # 3
    [7, 8],  # 4
    [9, 10], # 5
]

mark_vertaxes = [False]*n

# v - стартовая вершина
for i in range(n):
    BFS(G, i)



#--------------------------------
# Сложеность BFS при матрице смежности O(n^2)

def BFS(G, v):
    q = queue.Queue()
    q.put(v)

    while len(queue) > 0:
        # pop() - удаляет последний элемент из списка и возвращает его
        v = queue.pop(0)

        if not mark_vertaxes[v]:
            print(v)
            mark_vertaxes[v] = True

        for w in range(n):
            if G[v][w] == 1 and not mark_vertaxes[w]:
                q.put(w)    
    
    return mark_vertaxes

# G - матрица смежности
# n - число вершин в графе
n = 10

G = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
]

for i in range(n):
    BFS(G, i)



#--------------------------------
# Хотим найти наименьший путь между стартовой вершиной поиска вширину и всеми достижимыми из неё вершинами 

# dist - массив расстояний от стартовой вершины до всех достижимых вершин
dist = [float('inf')]*n
visited = [False]*n

def BFS(G, start):
    q = queue.Queue()
   
    dist[start] = 0
    visited[start] = True

    # Добавляем стартовую вершину в очередь
    q.enqueue(start)

    while not q.empty():

        # Извлекаем вершину из очереди (очередь - FIFO)
        v = q.dequeue() 

        # При G[v] - список смежности, w - вершина, соседняя с v
        for w in G[v]:
            if not visited[w]:
                visited[w] = True
                
                # Обновляем расстояние до вершины w. Итоговое расстояние - расстояние от начальной вершины до v
                dist[w] = dist[v] + 1

                # Добавляем вершину w в очередь
                q.enqueue(w)

#--------------------------------
# Когда хотим восстановить коротчайший путь между стартовой вершиной и конечной вершиной

pred = [None]*n

def BFS(G, start):
    q = queue.Queue()

    pred[start] = None
    visited[start] = True

    q.enqueue(start)

    while not q.empty():
        v = q.dequeue()

        for w in G[v]:
            if not visited[w]:
                visited[w] = True

                # Создаем список предыдущих вершин, надо для того чтобы восстановить путь. Например в действии:
                # 1 -> 2 -> 3 -> 4
                # Тогда pred[4] = 3, pred[3] = 2, pred[2] = 1
                # То есть предыдущая вершина для 4 - 3, для 3 - 2, для 2 - 1
                pred[w] = v

                # Добавление итерируемой вершины w в очередь
                q.enqueue(w)


# Алгорити, как восставим минимальный путь:
def restore_path(start, end):
    if not visited[end]:
        return None
    
    path = []
    v = end

    while v != start:
        path.append(v)

# Пример, как может заполниться массив pred: 
# -------------------------------------------------
# 1    | 2 | 3 | 4 | 5 |  6 | 7 | 8 |  9 | 10 | 11 |
#--------------------------------------------------
# None  1   1   1   3    8   9   2    4    5   -1      pred[i]
#
# 
# Тогда путь будет:
# 10 -> 5 -> 3 -> 1

        v = pred[v] # Переходим к предыдущей вершине

    path.append(start)

    return path[::-1] # Разворачиваем путь      

        
    
#--------------------------------
# Пометки вершин графа в порядке обхода BFS

# Принцип работы

next_idx = 0
ord = [None]*n

def BFS(G, v):
    q = queue.Queue()

    # Помечаем вершину v
    ord[v] = next_idx
    next_idx += 1

    visited[v] = True
    q.enqueue(v)

    while not q.empty():

        v = q.dequeue()

        for w in G[v]:
            if not visited[w]:
                visited[w] = True

                ord[w] = next_idx
                next_idx += 1

                q.enqueue(w)


