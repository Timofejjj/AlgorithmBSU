def Bild_Dict_Graph(vertices, edges):
    Dict_graph = {}
    for vertex in vertices:
        Dict_graph[vertex] = []

    for edge in edges:
        v1 = edge[0]
        v2 = edge[1]
        Dict_graph[v1].append(v2)
        Dict_graph[v2].append(v1)


    return Dict_graph


with open("input.txt", "r") as file:
    line_1 = file.readline().strip()
    # Считаем списое ребер:

    edges = set()  
    for line in file:
        u, v = line.strip().split()  
        edges.add((u, v))


n, m = map(int, line_1.split())
vertices = set()

for i in range(1, n + 1):
    vertices.add(str(i))

Dict_graph = Bild_Dict_Graph(vertices, edges)




with open("output.txt", "w") as file:
    for i in range(1, n + 1):
        neighbors = Dict_graph[str(i)]  # список смежных вершин
        num = len(neighbors)
        file.write(f"{num} ")
        
        for neighbor in neighbors:
            file.write(f"{neighbor} ")
        
        file.write("\n")

