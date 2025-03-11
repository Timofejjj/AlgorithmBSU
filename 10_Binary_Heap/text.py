
# with open('input.txt', 'r') as file:
#     n = int(file.readline())
#     arr = np.array([n], dtype=np.int32)
#     arr = np.fromstring(file.readline().strip(), sep=' ', dtype=np.int32)

n = int(input().strip())
arr = np.fromstring(input().strip(), sep=' ', dtype=np.int32)

result = "Yes"

for i in range(n):

  if (2*i + 1) <= (n - 1) and arr[i] > arr[2*i + 1]:
    result = "No"
    break

  if (2*i + 2) <= (n - 1) and arr[i] > arr[2*i + 2]:
    result = "No"
    break


print(result)

# with open('output.txt', 'w') as file:
#   file.write(result)

#10
#9 17 16 25 21 20 60 25 40 33
