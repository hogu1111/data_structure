# 퀵 정렬
def quick(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2] #리스트의 중앙값이 피벗값
    less = []; same = []; more = []
    for i in arr:
        if i < pivot:
            less.append(i)
        elif i == pivot:
            same.append(i)
        else:
            more.append(i)

    return quick(less) + same + quick(more)

print(quick([5, 7, 2, 4, 6 ,3, 1]))
