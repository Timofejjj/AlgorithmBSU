import sys
sys.setrecursionlimit(10000)

with open('input.txt', 'r') as file: 
  n = int(file.redline())
  data = [list(map(int, fille.readline().split())) for _ in range(2)]

jobs = []

for arr in data:
  s = arr[0]
  ops = [(arr[2*i + 1], arr[2*i + 2]) for i in range(s)]
  jobs.append(ops)

s1, s2 = len(jobs[0]), len(jobs[1])

INF = 10**18
dp = [[INF] * (s2+1) for _ in range(s1+1)]
dp[0][0] = 0


for i in range(s1 + 1):
  for j in range(s2 + 1):

    # Запоминаем такущее время
    cur = dp[i][j]

    if cur == INF:
      continue

    if i < s1:                               #тут берем время
      dp[i + 1][j] = min(dp[i + 1][j], cur + jobs[0][i][1])

    if j < s2:
      dp[i][j + 1] = min(dp[i][j + 1], cur + jobs[1][i][1])

    if i < s1 and j < s2:
      k1, t1 = jobs[0][i]
      k2, t2 = jobs[1][j]

      if k1 != k2:
        dp[i + 1][j + 1] = min(dp[i + 1][j + 1], cur + max(t1, t2))
      
      else:
        dp[i + 1][j + 1] = min(dp[i + 1][j + 1], cur + t1 + t2)
      

with open('output.txt', 'w') as file:
  file.write(str(dp[s1][s2]))