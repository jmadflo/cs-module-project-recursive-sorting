# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    # Your code here
    merged_arr = []

    while elements > 0:
        # if arrA or arrB has length of 0, simply add the other array to the end
        # print(f'A: {arrA}', f'B:{arrB}')
        # print(merged_arr)
        if len(arrA) == 0:
            merged_arr.extend(arrB)
            arrB = []
        elif len(arrB) == 0:
            merged_arr.extend(arrA)
            arrA = []
        # if both still have elements, then add the lesser element to the merged_arr
        elif arrA[0] > arrB[0]:
            merged_arr.append(arrB.pop(0))
        else:
            merged_arr.append(arrA.pop(0))

        elements = len(arrA) + len(arrB)
    # print(merged_arr)
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    midpoint = len(arr) // 2
    first_half = merge_sort(arr[:midpoint])
    second_half = merge_sort(arr[midpoint:])

    return merge(first_half, second_half)


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

# print(merge([1,3,5,7,9], [2,4,6,8]))