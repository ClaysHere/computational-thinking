def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    if x not in arr:
        return -1
    if x == arr[low]:
        return low
    elif x == arr[high]:
        return high
    else:
        while low <= high:
            mid = (high + low) // 2
            # jika x lebih besar, abaikan sebelah kiri
            if arr[mid] < x:
                low = mid + 1
            # jika x lebih keci;, abaikan sebelah kanan
            elif arr[mid] > x:
                high = mid + 1
            # berarti x ada di tengah
            else:
                return mid
        return -1
    
arr = [2,3,4,10,40]
x = 19

result = binary_search(arr, x)

if result != -1:
    print(f'Elemen ada di indeks {result}')
else:
    print('Elemen tidak ada dalam array')
