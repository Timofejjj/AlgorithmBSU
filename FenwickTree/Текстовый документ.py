import numpy as np

class FenwickTree:
    def __init__(self, length_arr):
        self.length_arr = length_arr
        self.Tree = [0] * (length_arr + 1)

    def Add(self, index, num):
        while index <= self.length_arr:
            self.Tree[index] += num
            index += index & -index

    def FindSum(self, position):
        sum = 0
        while position > 0:
            sum += self.Tree[position]
            position -= position & -position
        return sum

n = int(input())
arr = np.fromstring(input().strip(), sep=' ', dtype=int)

tree = FenwickTree(n)
for j in range(n):
    tree.Add(j + 1, arr[j])

requests_num = int(input())
for _ in range(requests_num):
    requests = input().split()

    if requests[0] == "Add":
        index = int(requests[1])
        num = int(requests[2])
        tree.Add(index + 1, num)

    elif requests[0] == "FindSum":
        l = int(requests[1])
        r = int(requests[2])
        res = tree.FindSum(r) - tree.FindSum(l)
        print(res)
