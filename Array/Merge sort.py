def merge_sort(array):
    # Base case: if the array has 1 or no elements, it is already sorted.
    if len(array) <= 1:
        return array

    # Split the array into left and right halves
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    # Merge the sorted halves
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    # Merge the two sorted subarrays
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Example usage:
a = [1, 3, 2, 5, 4]
sorted_a = merge_sort(a)
print(sorted_a)
