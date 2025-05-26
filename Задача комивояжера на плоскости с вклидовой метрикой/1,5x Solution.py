def solution(cities, coordinates_cities):
    # Построение MST с помощью алгоритма Прима
    in_mst = [False] * cities
    distance = [float('inf')] * cities
    parent = [-1] * cities
    degree = [0] * cities

    distance[0] = 0  # Исправлена опечатка: distace -> distance

    for _ in range(cities):
        u = min((distance[i], i) for i in range(cities) if not in_mst[i])[1]
        in_mst[u] = True

        if parent[u] != -1:
            degree[u] += 1
            degree[parent[u]] += 1

        # Обновление расстояний до соседей
        for v in range(cities):
            if not in_mst[v]:
                d = abs(coordinates_cities[u][0] - coordinates_cities[v][0]) + abs(coordinates_cities[u][1] - coordinates_cities[v][1])  # Исправлена опечатка: coordinated_cities -> coordinates_cities
                if d < distance[v]:
                    distance[v] = d
                    parent[v] = u

    # Список вершин с нечетной степенью
    odd_vertices = [i for i in range(cities) if degree[i] % 2 == 1]

    # Функция для построения минимального совершенного паросочетания жадным методом
    def greedy_mwpm(odd_vertices, coordinates_cities):
        edges = []
        # Создаем список всех возможных ребер между вершинами с нечетной степенью
        for i in range(len(odd_vertices)):
            for j in range(i + 1, len(odd_vertices)):
                u = odd_vertices[i]
                v = odd_vertices[j]
                weight = abs(coordinates_cities[u][0] - coordinates_cities[v][0]) + abs(coordinates_cities[u][1] - coordinates_cities[v][1])
                edges.append((weight, u, v))

        # Сортируем ребра по возрастанию веса
        edges.sort()

        # Строим паросочетание
        matching = []
        used = set()
        for weight, u, v in edges:
            if u not in used and v not in used:
                matching.append((u, v))
                used.add(u)
                used.add(v)
        return matching

    # Вычисляем MWPM - минальное совершенное парасочетание среди вершин нечетной степени
    mwpm_edges = greedy_mwpm(odd_vertices, coordinates_cities)

    # Извлекаем ребра из MST и объединяем с MWPM:
    mst_edges = [(parent[i], i) for i in range(1, cities)]

    # оОбъедияем для построения Эйлерового графа:
    eylerian_edges = mst_edges + mwpm_edges

  # Посторим список смежности для мультиграфа
  adj = [[] for _ in range(cities)]

  for u, v in eylerian_edges:
    adj[u].append(v)
    adj[v].append(u)

  # Функция для нахождения Эйлерова цикла (алгоритм Хирхольцера) --- ????
    def find_eulerian_circuit(adj, start=0):
        circuit = []
        stack = [start]
        while stack:
            u = stack[-1]
            if adj[u]:
                v = adj[u][-1]  # Берем последнего соседа
                adj[u].pop()    # Удаляем ребро из списка u
                adj[v].remove(u)  # Удаляем обратное ребро из списка v
                stack.append(v)
            else:
                circuit.append(stack.pop())
        circuit.reverse()  # Разворачиваем, так как собирали в обратном порядке
        return circuit

  # Найдем этот эйлеров цикл
  eylerian_circuit = find_eulerian_circuit(adj)

  # Сворачивание эйлерового цикла в гамильтонов:
  def shortcut_to_hamilton(circuit):
    visited = set()
    tour = []
    for v in circuit:
      if v not in visited:
        tour.append(v)
        visited.add(v)
  return tour

  tsp_tour = shortcut_to_hamilton(eylerian_circuit)

  return tsp_tour

# Пример вызова функции (исправленный код чтения файла)
with open("input.txt", "r") as file:
    n = int(file.readline().strip())
    coordinates = [tuple(map(int, file.readline().strip().split())) for _ in range(n)]

tour = solution(n, coordinates)
print(tour)
