num_waterLilies = int(input())
arr_mosquitos = list(map(int, input().split()))

# Every position is (-1)
arr_sum = [-1]*num_waterLilies

# Initialization arr of indexes
paSS_frog = [-1]*num_waterLilies

arr_sum[0] = arr_mosquitos[0]

for i in range(num_waterLilies):

  if arr_sum[i] == (-1):
    continue

  if (i + 2) < num_waterLilies:
    elementFrom_arr_sum = arr_sum[i] + arr_mosquitos[i + 2]

    if elementFrom_arr_sum > arr_sum[i + 2]:
      arr_sum[i + 2] = elementFrom_arr_sum
      paSS_frog[i + 2] = i

  if (i + 3) < num_waterLilies:
    elementFrom_arr_sum = arr_sum[i] + arr_mosquitos[i + 3]

    if elementFrom_arr_sum > arr_sum[i + 3]:
      arr_sum[i + 3] = elementFrom_arr_sum
      paSS_frog[i + 3] = i


if arr_sum[num_waterLilies - 1] == -1:
  print(-1)

else:

  print(arr_sum[num_waterLilies - 1])

  path = list()

  i = num_waterLilies - 1
  while i != (-1):
    path.append(i + 1)
    i = paSS_frog[i]

  path.reverse()
  print(" ".join(map(str, path)))



