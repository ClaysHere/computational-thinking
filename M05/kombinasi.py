def find_combinations(numbers, target):
    """
    Fungsi ini menerima sebuah list bilangan bulat (numbers) dan sebuah bilangan bulat (target).
    Fungsi ini mengembalikan semua kombinasi penjumlahan dari bilangan dalam list numbers yang
    menghasilkan bilangan target.
    """
    results = []  # list untuk menyimpan hasil kombinasi penjumlahan
    current = []  # list untuk menyimpan kombinasi penjumlahan saat ini
    
    def backtrack(start, remain):
        # Jika remain == 0, artinya kita telah menemukan sebuah kombinasi yang valid
        if remain == 0:
            results.append(list(current))  # simpan kombinasi saat ini ke dalam results
            return
        
        # Jika remain < 0, artinya kombinasi saat ini tidak valid, hentikan pencarian
        if remain < 0:
            return
        
        # Cari kombinasi penjumlahan yang memungkinkan dengan bilangan selanjutnya dalam list
        for i in range(start, len(numbers)):
            current.append(numbers[i])  # tambahkan bilangan ke dalam kombinasi saat ini
            backtrack(i, remain - numbers[i])  # cari kombinasi dengan bilangan selanjutnya
            current.pop()  # hapus bilangan dari kombinasi saat ini
    
    backtrack(0, target)  # mulai pencarian kombinasi dari bilangan pertama
    return results

# Contoh penggunaan
numbers = list(map(int, input().split()))  # masukkan sekumpulan bilangan acak
target = int(input())  # masukkan bilangan yang ingin dicari kombinasi penjumlahannya
combinations = find_combinations(numbers, target)  # cari kombinasi penjumlahan yang memungkinkan
for i in range(len(combinations)):
    for j in range(len(combinations[i])):
        print(combinations[i][j],end=' ')
    print()# cetak hasil kombinasi
    
    
'''
Kompleksitas waktu dari kode tersebut adalah O(2^n), di mana n adalah jumlah bilangan dalam list numbers. 
Ini disebabkan oleh fungsi find_combinations, yang memiliki kompleksitas waktu sebesar O(2^n), 
karena pada setiap level rekursif kita memiliki dua pilihan: menambahkan bilangan ke dalam kombinasi saat ini atau tidak menambahkan bilangan tersebut.

Kompleksitas ruang dari kode tersebut adalah O(n), di mana n adalah jumlah bilangan dalam list numbers. 
Hal ini disebabkan oleh list results dan list current, yang masing-masing menyimpan data dengan ukuran O(n). 
Selain itu, karena fungsi backtrack dipanggil secara rekursif, maka setiap pemanggilan fungsi akan menambahkan frame pada stack, 
sehingga jumlah maksimum stack frame yang dibutuhkan adalah O(n). Oleh karena itu, kompleksitas ruang dari kode tersebut adalah O(n).
'''


def find_combinations(arr, n, i, res, results):
    if n == 0:
        results.append(res[:])
        return
    if i == len(arr) or n < 0:
        return
    res.append(arr[i])
    find_combinations(arr, n - arr[i], i, res, results)
    res.pop()
    find_combinations(arr, n, i + 1, res, results)

# contoh penggunaan
arr = list(map(int,input().split()))
n = int(input())
results = []
find_combinations(arr, n, 0, [], results)

for i in range(len(results)):
    for j in range(len(results[i])):
        print(results[i][j],end=' ')
    print()# cetak hasil kombinasi

'''
Kompleksitas dari kode di atas adalah O(2^N), di mana N adalah jumlah elemen dalam list arr. 
Hal ini karena untuk setiap elemen dalam list arr, ada dua kemungkinan aksi yang dapat diambil, 
yaitu memilih atau tidak memilih elemen tersebut, sehingga jumlah kombinasi yang mungkin adalah 2 pangkat N. 
Oleh karena itu, kompleksitas fungsi find_combinations() secara keseluruhan adalah O(2^N).
'''
