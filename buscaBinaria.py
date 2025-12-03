def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        shot = list[mid]
        if shot == item:
            return mid
        if shot > item:
            high = mid - 1
        else:   
            low = mid + 1
    return None

list = [1,3,5,7,9]

print(binary_search(list, 3))