import sys

with open("input.txt", 'r') as file:
    v, m = map(int, file.readline().split())
    degs = [0] * v

    for _ in range(m):
        u, w = map(int, file.readline().split())
        degs[u-1] += 1
        degs[w-1] += 1

degs.sort(reverse=True)

with open("output.txt", 'w') as file:
    file.write(" ".join(map(str, degs)))