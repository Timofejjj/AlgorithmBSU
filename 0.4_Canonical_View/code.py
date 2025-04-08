from collections import deque


def search_root(G, n):

    for j in range(n):
        is_root = True
        for i in range(n):
            if G[i][j] == 1:
                is_root = False
                break

        if is_root:
            return j
    return None



def build_canonical_tree(G, root, n):
    q = deque()
    
    visited = [False] * n
    visited[root] = True
    q.append(root)

    P = [0] * (n + 1)

    while q:
        v = q.popleft()

        for u in range(n):
            if G[v][u] and not visited[u]:
                visited[u] = True
                P[u + 1] = v + 1

                q.append(u)
    return P

# Пример
G = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0]
]

n = len(G)
root = search_root(G, n)
P = build_canonical_tree(G, root, n)

P.pop(0)
print(P)
