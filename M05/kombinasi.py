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
