def sort_names(names):
    if len(names) <= 1:
        return names
    pivot = names[len(names) // 2]
    left = [name for name in names if (len(name), name) < (len(pivot), pivot)]
    middle = [name for name in names if (len(name), name) == (len(pivot), pivot)]
    right = [name for name in names if (len(name), name) > (len(pivot), pivot)]
    return sort_names(left) + middle + sort_names(right)

n = int(input())
names = []
for i in range(n):
    name = input().strip()
    names.append(name)
sorted_names = sort_names(names)
for name in sorted_names:
    print(name)
    
# kompleksitas O(n log n)
