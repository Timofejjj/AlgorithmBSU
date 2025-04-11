from collections import deque

def BFS(G, root, n, ord, visited, index):
    q = deque()
    ord[root] = index  
    visited[root] = True
    q.append(root)
    index += 1

    while q:
        v = q.popleft()
        for u in range(n):
            if G[v][u] and not visited[u]: 
                visited[u] = True
                ord[u] = index  
                index += 1
                q.append(u)
    return index


arr = []
with open("input.txt", 'r') as file:
    n = int(file.readline())
    arr = [list(map(int, file.readline().split())) for _ in range(n)]


ord = [0] * n  
visited = [False] * n
index = 1


for j in range(n):
    if not visited[j]:
        index = BFS(arr, j, n, ord, visited, index)


with open("output.txt", "w") as file:
    for i in ord:
        file.write(str(i) + " ")
