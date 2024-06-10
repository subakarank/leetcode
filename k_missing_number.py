def k_missing_number(arr: list, k: int):
    left, right = 0 , len(arr)

    while left < right:
        mid = (left + right) // 2 
        missing = arr[mid] - mid - 1

        if missing < k:
            left = mid + 1 
        else: 
            right = mid 

    return left + k 

def brute_force(arr: list, k: int):
    missing_counter = 0 
    current = 1
    while True:
        if current not in arr:
            missing_counter += 1
            if missing_counter == k:
                return current
        else:
            current += 1 