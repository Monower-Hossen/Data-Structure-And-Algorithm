a = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(a)
for i in range(1,n):
    insert_index = i
    current_value = a.pop(i)
    for j in range(i-1, -1, -1):
        if a[j] > current_value:
            insert_index = j
    a.insert(insert_index, current_value)

print("Sorted array:", a)



m = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(m)
for i in range(1,n):
    insert_index = i
    current_value = m[i]
    for j in range(i-1, -1, -1):
        if m[j] > current_value:
            m[j+1] = m[j]
            insert_index = j
        else:
            break
    m[insert_index] = current_value

print("Sorted array:", my_array)