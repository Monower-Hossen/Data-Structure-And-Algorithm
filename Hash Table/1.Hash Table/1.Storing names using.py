my_array = ['Pete', 'Jones', 'Lisa', 'Bob', 'Siri']

def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)

    return sum_of_chars % 10

print("'Bob' has hash code:",hash_function('Bob'))
