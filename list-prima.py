def prima(x):
    if x == 1:
        return False
    
    for i in range(2,x):
        if x % i == 0:
            return False
        
    return True

a = list(map(int,input().split()))

jlh=0
for i in range(len(a)):
    if prima(a[i]) == True:
        jlh+=1

print(jlh)
