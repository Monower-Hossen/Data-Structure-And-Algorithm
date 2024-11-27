# def selectionsort(a):
#     for i in range(len(a)):
#         cur_index = i
#         for j in range (i,len(a)):
#             if a[cur_index] < a[j]:
#                 cur_index = j
#         a[i],a[cur_index] = a[cur_index],a[i]
#     return a
# a=[2,1,3,5,4]
# print(selectionsort(a))


m = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(m)
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if m[j] < m[min_index]:
            min_index = j
    m[i], m[min_index] = m[min_index], m[i]

print("Sorted array:", m)