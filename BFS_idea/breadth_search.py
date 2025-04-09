import queue


#--------------------------------
# Сложность BFS при списке смежности O(n + m)

# v - Страртовая вершина
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

                    mark_vertaxes[w] = True
                    q.put(w)


# Список смежности задади в виде словаря: 
list_connect = dict()

list_connect = {
    1: [3, 7],  
    2: [3],
    3: [1, 2, 5],
    4: [5],
    5: [3, 4 , 6],
    6: [5, 7],
    7: [1, 6]
}


#--------------------------------
# Сложеность BFS при матрице смежности O(n^2)

def BFS(G, v):
    q = queue()
    
    visited[v] = True
    q.enqueue()

    while len(queue) > 0:
    
        v = q.dequeue()
    
        for u in range(n):
            if G[u][v] and not visited[u]:

                visited[u] = True
                q.enqueue()


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

# Поиск наименьших путей от стартовой вершины до всех достижимых вершин
# Граф G - задан в виде списка смежности

dist = [float('inf')]*n
visited = [False]*n

def BFS(G, start):
    q = queue.Queue()
   
    dist[start] = 0
    visited[start] = True

    # Добавляем стартовую вершину в очередь
    q.enqueue(start)

    while not q.empty():

        # Извлекаем вершину из очереди 
        v = q.dequeue() 

        for w in G[v]:
            if not visited[w]:
                visited[w] = True
                
                dist[w] = dist[v] + 1

                q.enqueue(w)

#--------------------------------
# Когда хотим восстановить наименший путь между стартовой вершиной и конечной вершиной
# Формируем массив pred

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

                pred[w] = v

                # Добавление итерируемой вершины w в очередь
                q.enqueue(w)



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



#--------------------------------
#Определение двудольности грфа: 


# Есть код определения двудольности на основе DFS (код на основе идеи присвоения меток)



#--------------------------------
# Определение связности графа:

# Пересмотри:
for vertage in range(vertages):
    if not visited[vertage]:
        BFS(vertage)
