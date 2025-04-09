visited_vertage

def DFS(v):
    visited_vertage[v] = True

    for u in G[v]:
        if not visited_vertage[u]:
            print(u)
            DFS[u]

# start - насальная вернина, откуда начинаем обход

list_connect = {
    1: [3],  
    2: [3],
    3: [1, 2, 5],
    4: [5],
    5: [3, 4 , 6],
    6: [5]
}


start = 1
DFS(start)

