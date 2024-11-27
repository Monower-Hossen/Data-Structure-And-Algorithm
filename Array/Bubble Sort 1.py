a = [7, 3, 9, 12, 11]

for i in range(len(a)-1):
    swapped = False
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            swapped = True
    if not swapped:
        break

print("Sorted array:", a)