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
            
def calculate_steps(matrices):
    n = len(matrices)
    
    # Base case: jika hanya ada satu matriks, maka tidak ada langkah yang perlu dilakukan
    if n == 1:
        return 0
    
    # Jika ada dua matriks, hitung langkah untuk mengalikan kedua matriks tersebut
    if n == 2:
        return matrices[0][0] * matrices[0][1] * matrices[1][1]
    
    # Hitung langkah-langkah untuk semua kemungkinan pemisahan matriks
    min_steps = float('inf')  # Menyimpan jumlah langkah terkecil yang ditemukan
    
    for i in range(1, n):
        left_matrices = matrices[:i]
        right_matrices = matrices[i:]
        
        left_steps = calculate_steps(left_matrices)
        right_steps = calculate_steps(right_matrices)
        
        current_steps = (left_steps + right_steps +
                         left_matrices[0][0] * left_matrices[-1][1] * right_matrices[-1][1])
        
        # Update nilai langkah terkecil
        min_steps = min(min_steps, current_steps)
    
    return min_steps

# Membaca masukan
N = int(input())
matrices = []
for _ in range(N):
    row, col = map(int, input().split())
    matrices.append((row, col))
question = int(input())

# Menjalankan fungsi untuk menghitung langkah-langkah
if question == 1:
    # Pertanyaan 1: Berapa total langkah yang dilakukan gajah Pak Ganesh dalam mengalikan matriks-matriks tersebut?
    total_steps = calculate_steps(matrices)
    print(total_steps)
elif question == 2:
    # Pertanyaan 2: Berapakah sisa pembagian banyaknya cara membentuk E yang menghasilkan langkah optimal dengan bilangan bulat 26101991?
    total_steps = calculate_steps(matrices)
    remainder = total_steps % 26101991
    print(remainder)
elif question == 3:
    # Pertanyaan 3: Berapakan sisa pembagian banyaknya cara membentuk E di mana langkahnya tidak harus optimal dengan bilangan bulat 26101991?
    # Karena tidak diberikan batasan pada langkah-langkahnya, jumlah kemungkinan adalah 2^(N-1)
    possibilities = pow(2, N-1)
    remainder = possibilities % 26101991
    print(remainder)
            
