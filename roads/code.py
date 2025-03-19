import numpy as np 


def search_gen(x):
  if parent[x] != x: 
    parent[x] = search_gen(parent[x])

  return parent[x]


def Union(el_1, el_2):

  global general_el
  el_1_gen = search_gen(el_1)
  el_2_gen = search_gen(el_2)

  if el_1_gen != el_2_gen:
    if size[el_1_gen] < size[el_2_gen]:
      el_1_gen, el_2_gen = el_2_gen, el_1_gen

    parent[el_2_gen] = el_1_gen
    size[el_1_gen] += size[el_2_gen]
    general_el -= 1



with open('input.txt', 'r') as file:
  towns_and_roads = file.read().split()

towns = int(towns_and_roads[0])
roads = int(towns_and_roads[1])

global parent, size, general_el

parent = np.arange(towns + 1)         
size = np.ones(towns + 1, dtype=int)

general_el = towns
connectivity_components = []


n = 2
for _ in range(roads):
  el_1 = int(towns_and_roads[n])
  el_2 = int(towns_and_roads[n + 1])

  Union(el_1, el_2)
  n += 2
  connectivity_components.append(general_el)


with open('output.txt', 'w') as file:
  for el in connectivity_components:
    file.write(str(el) + '\n')