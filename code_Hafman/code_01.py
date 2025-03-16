import sys
import numpy as np
from collections import deque

def len_coded_word(arr):

    gen_queue = deque(sorted(arr))
    helper_queue = deque()
    binary_length = 0


    while (len(gen_queue) + len(helper_queue)) > 1:

        if not helper_queue:
            first_min = gen_queue.popleft()
        elif not gen_queue:
            first_min = helper_queue.popleft()
        else:
             if gen_queue[0] <= helper_queue[0]:
                 first_min = gen_queue.popleft()
             else:
                 first_min = helper_queue.popleft()


        if not helper_queue:
            second_min = gen_queue.popleft()
        elif not gen_queue:
            second_min = helper_queue.popleft()
        else:
             if gen_queue[0] <= helper_queue[0]:
                 second_min = gen_queue.popleft()
             else:
                 second_min = helper_queue.popleft()


        helper_queue.append(first_min + second_min)
        binary_length += (first_min + second_min)

    return binary_length


with open("huffman.in", "r") as file:
    n = int(file.readline().strip())
    arr = np.fromstring(file.readline().strip(), sep=' ')

n = int(len_coded_word(arr))

with open("huffman.out", "w") as file:
    file.write(str(n))