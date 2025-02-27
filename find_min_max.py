def find_min_max(arr):
    def min_max(left, right):
        if left == right:
            return arr[left], arr[left]
        
        if right - left == 1:
            if arr[left] < arr[right]:
                return arr[left], arr[right]
            else:
                return arr[right], arr[left]

        mid = (left + right) // 2
        min1, max1 = min_max(left, mid)
        min2, max2 = min_max(mid + 1, right)

        return min(min1, min2), max(max1, max2)

    return min_max(0, len(arr) - 1)

arr = [35, 23, 1, 3, -4, 36, 99, 5, 1, 9, 2, 8, -4, 7]
print(find_min_max(arr))