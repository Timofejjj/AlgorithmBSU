#Решение задачи "Наибольшая общая подпоследовательность"

import numpy as np

def max_sub_line(word_a, word_b, l, cell):

    for i in range(1, l+1):
        for j in range(1, l+1):

            if word_a[i-1] == word_b[j-1]:
                cell[i][j] = cell[i-1][j-1] + 1
            else:
                cell[i][j] = max(cell[i-1][j], cell[i][j-1])
    return cell[l][l]


def search_sub_line(word_a, word_b, cell, l, indices_A, indices_B):
    i, j = l, l  
    while i > 0 and j > 0:
        if word_a[i-1] == word_b[j-1]:
            indices_A.append(i-1)
            indices_B.append(j-1)
            i -= 1
            j -= 1
        elif cell[i-1][j] >= cell[i][j-1]:
            i -= 1
        else:
            j -= 1

    indices_A.reverse()
    indices_B.reverse()


l = int(input())
word_a = list(map(int, input().split()))
word_b = list(map(int, input().split()))

cell = np.array([[0]*(l+1) for _ in range(l+1)])

print(max_sub_line(word_a, word_b, l, cell))  

indices_A = []
indices_B = []
search_sub_line(word_a, word_b, cell, l, indices_A, indices_B)

print(" ".join(map(str, indices_A)))
print(" ".join(map(str, indices_B)))