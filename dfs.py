graph = {
    'A' : ['B'],
    'B' : ['C','I'],
    'C' : ['P','D'],
    'D' : ['E'],
    'E' : ['F'],
    'F' : ['G'],
    'G' : ['H'],
    'H' : [],
    'I' : ['J'],
    'J' : ['K'],
    'K' : ['L'],
    'L' : ['M','X'],
    'M' : ['N'],
    'N' : ['O'],
    'O' : [],
    'P' : ['S','Q'],
    'Q' : ['R'],
    'R' : [],
    'S' : ['T'],
    'T' : ['U'],
    'U' : ['V'],
    'V' : ['W'],
    'W' : [],
    'X' : ['Y'],
    'Y' : ['U']
}

visited = []

queue = []

visited.append('A')

queue.append('A')

while queue:
    s = queue.pop(0)

    print(s, end=' ')

    for neighbour in graph[s]:
        if neighbour not in visited:

            visited.append(neighbour)

            queue.append(neighbour)
