def cari_jenis_hewan(x, y, n, urutan):
    if n == 1:
        return x
    
    total = []
    for i in range(n):
        total.append(x[i])
        if i > 0:
            total[i] += total[i-1]
    
    for i in range(n):
        if urutan <= total[i]:
            if i == 0:
                return y[i]
            return y[i-1] if urutan <= total[i-1] else y[i]
    
    return -1

n = int(input())
x = []
y = []
hasil = []

for i in range(n):
    x.append(int(input()))
    y.append(i+1)
q = int(input())

for i in range(q):
    urutan = int(input())
    jenis = cari_jenis_hewan(x, y, n, urutan)
    hasil.append(jenis)

for i in range(len(hasil)):
    print(hasil[i])
