

def get_optimal_mult(dimentions):
    lenght = len(dimentions)
    arr = [[0] * lenght for _ in range(lenght)]

    for l in range(2, lenght):  # Число матриц
        for i in range(1, lenght - l + 1):  # Начальный индекс
            j = i + l - 1
            arr[i][j] = float('inf')

            for k in range(i, j):
                cost = arr[i][k] + arr[k + 1][j] + dimentions[i - 1] * dimentions[k] * dimentions[j]

                if cost < arr[i][j]:
                    arr[i][j] = cost

    return arr[1][lenght - 1]


dimentions = []

file = open('input.txt', 'r')

num_matrics = int(file.readline())

for i in range(num_matrics):
    n, m = map(int, (file.readline()).split())
    if i == 0:
        dimentions.append(n)
    dimentions.append(m)

file.close()

file = open('output.txt', 'w')

uns = get_optimal_mult(dimentions)

file.write(str(uns))

file.close()