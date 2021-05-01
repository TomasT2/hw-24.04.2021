def binserch(arr, a):
    '''a-искомое число; arr- отсортированный массив
    если искомое число не найдено - None'''
    mid = len(arr) // 2
    min = 0
    max = len(arr) - 1

    while (arr[mid] != a) and (min <= max):
        if a > arr[mid]:
            min = mid + 1
        else:
            max = mid - 1
        mid = (min + max) //2

    if min > max: return None
    else: return mid+1
