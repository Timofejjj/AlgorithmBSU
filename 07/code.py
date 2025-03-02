N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

max_sum = 0

for top in range(N):

    temp = [0] * M
    for bottom in range(top, N):

        for j in range(M):

            # temp[j] = temp[j] + arr[bottom][j]
            temp[j] += arr[bottom][j]

        current = 0
        current_max = 0
        for x in temp:
            current = max(0, current + x)
            current_max = max(current_max, current)

        max_sum = max(max_sum, current_max)

print(max_sum)
