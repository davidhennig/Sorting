# TO-DO: complete the help function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    aIndex = 0
    bIndex = 0

    for i in range(len(merged_arr)):
        if aIndex == len(arrA) and bIndex <= len(arrB):
            merged_arr[i] = arrB[bIndex]
            bIndex += 1
        elif aIndex <= len(arrA) and bIndex == len(arrB):
            merged_arr[i] = arrA[aIndex]
            aIndex += 1
        elif arrA[aIndex] < arrB[bIndex]:
            merged_arr[i] = arrA[aIndex]            
            aIndex += 1
            # print(merged_arr)
            # print('A index in for loop',aIndex)
        elif arrA[aIndex] > arrB[bIndex]:
            merged_arr[i] = arrB[bIndex]            
            bIndex += 1
            # print(merged_arr)
            # print('B index in for loop',bIndex)


    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        half = len(arr)//2
        left = merge_sort(arr[:half])
        right = merge_sort(arr[half:])

        arr = merge(left,right)

    return arr
print(merge_sort([1,43,56,7,45,3]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
