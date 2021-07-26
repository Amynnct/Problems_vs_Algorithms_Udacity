def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    end_idx = len(input_list) - 1
    if end_idx < 0:
        return -1
    pivot_point = find_pivot_point(input_list, 0, end_idx)
    if pivot_point == None:
        return binary_search(input_list, number, 0, end_idx)
    if number >= input_list[0]: 
        return binary_search(input_list, number, 0, pivot_point)
    else:
        return binary_search(input_list, number, pivot_point+1, end_idx)



def find_pivot_point(input_list, start_idx, end_idx):
    start = input_list[start_idx]
    end = input_list[end_idx]
    pivot_point = None

    if start > end: #if not then no rotate occured
        if start_idx == (end_idx - 1):  #found two out-of-order elements that are next to each other
            return start_idx 

        mid_idx = (start_idx + end_idx) // 2
        mid = input_list[mid_idx]
        if start > mid: #pivot is before mid
            pivot_point = find_pivot_point(input_list, start_idx, mid_idx)
        else: #pivot is after mid
            pivot_point = find_pivot_point(input_list, mid_idx, end_idx)
        
    return pivot_point

def binary_search(input_list, target, start_idx, end_idx): #input_list must be an ordered list
    while (start_idx <= end_idx):
        mid_idx = (start_idx + end_idx) // 2
        if target == input_list[mid_idx]:
            return mid_idx
        elif target < input_list[mid_idx]:
            end_idx = mid_idx
        else:
            start_idx = mid_idx + 1
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]) #Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]) #Pas
test_function([[6, 7, 8, 1, 2, 3, 4], 8]) #Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1]) #Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10]) #Pass
test_function([[1, 2, 3, 5, 6, 7, 8], 6]) #Pass

#Edge cases
test_function([[], 6]) #Pass
test_function([[-2, 0, 1, 2, 3, -7, -6, -5], -6]) #Pass

