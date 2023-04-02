def biner(n):
   if n > 1:
       biner(n//2)
   print(n % 2,end = '')

n = 2000

biner(n)
print()
