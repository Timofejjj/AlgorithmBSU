import numpy as np

with open("input.txt", "r") as file:
  n = int(file.readline())

n_bin = (bin(n)[2:])

lst = list(map(int, str(n_bin)))
lst.reverse()

n_int = np.array(lst)
len_arr = len(n_int)

counter = 0
temp = list()


for i in range(len_arr):

 if n_int[i] == 1:
  temp.append(i)


with open("output.txt", "w") as file:
  for B in temp:
    file.write(str(B) + '\n')

