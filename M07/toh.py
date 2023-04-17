def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print(f'Buku {n} pindah dari rak {from_rod} ke rak {to_rod}')
        return
    tower_of_hanoi(n-1, from_rod, aux_rod, to_rod)
    print(f'Buku {n} pindah dari rak {from_rod} ke rak {to_rod}')
    tower_of_hanoi(n-1, aux_rod, to_rod, from_rod)

n = int(input())
tower_of_hanoi(n, 'A', 'C', 'B')

#kompleksitas O(2^n)

def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        moves.append((n, from_rod, to_rod))
        return
    tower_of_hanoi(n-1, from_rod, aux_rod, to_rod)
    moves.append((n, from_rod, to_rod))
    tower_of_hanoi(n-1, aux_rod, to_rod, from_rod)

n = int(input())
moves = []
tower_of_hanoi(n, 'A', 'C', 'B')

for move in moves:
    print(f'Buku {move[0]} pindah dari rak {move[1]} ke rak {move[2]}')
