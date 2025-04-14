import heapq


with open('input.txt', "r") as file:
  n, m = map(int, file.readline().split())
  arr = [[] for _ in range(n + 1)]
  
  for _ in range(1, (m + 1)):
    u, v, w = map(int, file.readline().split())
    arr[u].append((v, w))


INF = 10**18
dist = [INF] * (n + 1)
visited = [False] * (n + 1)
dist[1] = 0

heap = []
heapq.heapify(heap)

# Как это работает внутри?
# 1 - страртовая вершина, 0 - метка
start_param = (1, 0)
heapq.heappush(heap, start_param)


while heap:
  u, dist_v = heapq.heappop(heap)

  if visited[u]:
    continue

  visited[u] = True
  
  for v, w in arr[u]: 

    # За счет такой строчки получили сложность O(m*log(m)) + O(n + m)
    if not visited[u] and dist[u] + w < dist[v]:
      dist[v] = dist[u] + w
      heapq.heappush(heap, (dist[v], v))
  