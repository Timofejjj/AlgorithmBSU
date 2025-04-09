

#---------------------------
# DFS на списке смежности при помощи рекурсии.
# Время работы O(n + m)

def DFS(v):
    visited_vertage[v] = True

    for u in G[v]:
        if not visited_vertage[u]:
            DFS[u]

# start - насальная вернина, откуда начинаем обход

DFS(start)


# DFS на матрице смежности


def DFS(v):
    visited[v] = True

    for u in range(n):

        if G[v][u] and not visited[u]:
            DFS(u)


G = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
]


#--------------------------
# Нерекурсивный DFS





#--------------------------
# Порядок обхода вершин при помощи DFS. Граф задан списком смежности

counter = 0

def DFS(v):
    visited[v] = True

    # тут 
    index_v[v] = counter
    counter += 1

    for u in G[v]:
        if not visited[u]:
            DFS(u)


#--------------------------
# Корневое дерево поиска вглубину
# Дерево задано списком смежности

'''
Зачем хранить pred? Зная предков, легко восстановить пути от корня компоненты к любой вершине
(пройдя назад по цепочке pred). Это удобно, например, чтобы быстро вывести путь из стартовой вершины к любой другой.
'''
# Двигаемся по каждой вершине и для каждой вершины запускаем поиск вглубину

def DFS(v):
    visited[v] = True

    for u in G[v]:
        pred[u] = v
        DFS(u)


# n - число вершин 
for v in range(n):
    if not visited[v]:

        # Задали корень (+ ещё в конце pred[] будет None )
        pred[v] = None
        DFS(v)


#--------------------------
# Компоненты связности графа

def DFS(v):
    visited[v] = True
    components[v] = components

    for u in G[v]:
        if not visited[u]:
            DFS(u)


for v in range(n):
    if not visited[v]:

        DFS(v)
        components += 1


#--------------------------
# Определение двудольности графа


# Пусть изначальн он двудольный
is_partable = True

def DFS(v):
    visited[v] = True


    for u in G[v]:
        if visited[u] and part[v] == part[u]:
            is_partable = False

        if not visited[u]:
            part[u] = not part[v]
            DFS(u)


for v in range(n):
    if not visited[v]:
        visited[v] = True

        DFS(v)

