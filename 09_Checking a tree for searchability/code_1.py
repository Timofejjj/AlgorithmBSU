import sys
import math

def main():
 
    # low и hight - задаём границы нешему промежутку (основной алгоритм)
    def cheaking_for_search(i, low, hight):
        if i == -1:
            return True
       if (nodeValues[i] < minBounds[i]) or (nodeValues[i] >= maxBounds[i]):
            return False
        return cheaking_for_search(left[i], low, values[i]) and cheaking_for_search(right[i], values[i], hight)

    ###############################

    data = []
    while True:
        user_input = input().strip()  
        if user_input == "": 
            break

        data.extend(user_input.split())
     
    n = int(data[0])

    values = [0] * n
    left = [-1] * n
    right = [-1] * n

    values[0] = int(data[1])
    index = 2

    #Заполнение данных
    for i in range(1, n):
        val = int(data[index])
        parent_index = int(data[index + 1]) - 1
        direction = data[index + 2]
        index += 3

        values[i] = val
        if direction == "L":
            left[parent_index] = i
        elif direction == "R":
            right[parent_index] = i

    # Вызываем функцию
    if cheaking_for_search(0, -math.inf, math.inf):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()


#######################################

# values[i] = val
# if child_dir == "L":
#     left[parent_index] = i - вот тут разобраться с идеей, то есть что
                                # даёт такое хранение
# elif child_dir == "R":
#     right[parent_index] = i

############################# Разбор, то есть меня интерисует как организованы left и right, что мы можнем так писать: 
# return check_bst(left[i], low, values[i]) and check_bst(right[i], values[i], high) - 

#############################

#     data.extend(user_input.split())

#     .extend() - так же как и .append, но в качестве аргумента принимает итератор (итератор, итерируемый объект) и объединяет его со списком
