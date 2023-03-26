def coin(s,m):
    for i in range(len(s)):
        if i == 0:
            if s[i] != string[(i+1)] and s[i] != s[i+2]:
                m = i + 1 
        elif i == (len(string)-1):
            if s[i] != s[(i-1)] and s[i] != s[i-2]:
                m = i + 1
        else:
            if s[i] != s[(i-1)] and s[i] != s[i+1]:
                m = i + 1
    
    print(m)

s = input()

string = []
for i in range(len(s)):
    string.append(s[i])

maxi = -1

n = 0

for i in range(len(string)):
    if i > (len(string)-1):
        if string[i] == string[i+1]:
            n+=1

if n == 8:
    print(maxi)
else:
    coin(string,maxi)
    
# kompleksitas = O(n)





# versi short

koin = input()
posisi = -1
beda = koin[0]
if(beda != koin[1]):
    posisi = 1
else:
    for i in range(len(koin)):
        if(koin[i] != beda):
            posisi = i+1
            break
print(posisi)

# code by : gonstealyoman
