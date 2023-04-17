def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

n = int(input())
weights = list(map(int, input().split()))

sorted_weights = quicksort(weights)

for i in range(n):
    print(f"Bebek {i+1}: {sorted_weights[i]}")

# kompleksitas O(n log n)
