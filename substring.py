a = ['String','pattern']#list(input().split())
b = ['String','teks']#list(input().split())

arr_a = []
arr_b = []

for i in range(len(a)):
    temp=[]
    for j in range(len(a[i])):
        temp.append(a[i][j])
    arr_a.append(temp)

for i in range(len(b)):
    temp=[]
    for j in range(len(b[i])):
        temp.append(b[i][j])
    arr_b.append(temp)

print(arr_a)
print(arr_b)

# Belum Solved
