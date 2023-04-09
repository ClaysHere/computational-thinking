def pangkat(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        y = pangkat(x, n//2)
        print(f"x: {y} n/2: {n//2}")
        return y*y
    else:
        y = pangkat(x, (n-1)//2)
        print(f"x: {y} n/2: {(n-1)//2}")
        return x*y*y

x, n = map(int, input().split())
hasil = pangkat(x, n)
print(hasil)
