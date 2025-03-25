def binary_search(array, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, right)
    else:
        return binary_search(array, target, left, mid - 1)

if __name__ == "__main__":
    array = [3, 9, 10, 27, 38, 43, 82]
    target = 27
    result = binary_search(array, target, 0, len(array) - 1)
    print("Target found at index:", result if result != -1 else "Not found")
