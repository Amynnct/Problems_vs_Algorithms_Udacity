def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) <= 1:
        return [0, 0]
    sorted_list = merge_sort(input_list)
    first_num = ""
    second_num = ""
    for i in range(len(sorted_list)-1, -1, -2):
        if sorted_list[i] not in range(0, 10):
            print("Invalid input list. This function only supports list with elements in range [0, 9].")
            return [0, 0]
        first_num += str(sorted_list[i])
    for i in range(len(sorted_list)-2, -1, -2):
        if sorted_list[i] not in range(0, 10):
            print("Invalid input list. This function only supports list with elements in range [0, 9].")
            return [0, 0]
        second_num += str(sorted_list[i])
    return [int(first_num), int(second_num)]
    

def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    
    mid = len(input_list) // 2
    left = merge_sort(input_list[:mid])
    right = merge_sort(input_list[mid:])

    return merge(left, right)

def merge(left, right):
    merged = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    merged += left[left_idx:]
    merged += right[right_idx:]

    return merged

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])  #Pass
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])  #Pass

test_function([[7, 3, 4, 2, 3, 2, 7], [7432, 732]])  #Pass
test_function([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [97531, 86420]])  #Pass

#Edge cases
test_function([[], [0, 0]])  #Pass
test_function([[-1, 3, 4, -9, -2, 3, 5], [0, 0]]) #Pass
#Invalid input list. This function only supports list with elements in range [0, 9].
test_function([[5, 7, 22, 5, 24, 89, 40], [0, 0]]) #Pass
#Invalid input list. This function only supports list with elements in range [0, 9].



