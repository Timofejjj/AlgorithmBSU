def search_palindrome_len(lst_str, l):

    cell = [[0] * n for _ in range(n)]
    
    for i in range(l):
        cell[i][i] = 1

   
    for length in range(2, l + 1): 
        for i in range(l - length + 1):
            j = i + length - 1 

            if lst_str[i] == lst_str[j]:
                cell[i][j] = cell[i + 1][j - 1] + 2  
            else:
                cell[i][j] = np.max(cell[i + 1][j], cell[i][j - 1]) 
    
    return cell, cell[0][l - 1]


def search_palindrome(cell, lst_str, l):
    i, j = 0, l - 1
    left_part = []
    right_part = []

    while i <= j:
        if lst_str[i] == lst_str[j]:
            left_part.append(lst_str[i])

            if i != j:
                right_part.append(lst_str[j])
            i += 1
            j -= 1
        elif cell[i + 1][j] >= cell[i][j - 1]:
            i += 1
        else:
            j -= 1

    return "".join(left_part + right_part[::-1])


with open("input.txt", "r", encoding="utf-8") as fin:
    in_str = fin.readline().rstrip("\n")

lst_str = list(in_str)
l = len(lst_str)


cell, pal_len = search_palindrome_len(lst_str, l)
pal_seq = search_palindrome(cell, lst_str, l)

with open("output.txt", "w", encoding="utf-8") as fout:
    fout.write(str(pal_len) + "\n")
    fout.write(pal_seq + "\n")