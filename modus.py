angka = list(map(int,input().split()))

jumlah = []

for i in range(10):
    jumlah.append(0)

print(f'\n{jumlah}\n')

for i in range(len(angka)):
    jumlah[angka[i]]+=1

print(f'\n{jumlah}\n')

maxi = -1

for i in range(len(jumlah)):
    if jumlah[i]>maxi:
        maxi = jumlah[i]
        modus = i
        print(f'\n{maxi}\n')
        print(f'\n{jumlah}\n')

print("Modus :", modus)
