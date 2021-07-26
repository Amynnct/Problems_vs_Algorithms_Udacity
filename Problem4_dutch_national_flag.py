def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    zero_idx = 0
    two_idx = len(input_list) - 1
    i = 0
    while (i <= two_idx):
        if input_list[i] == 0:
            input_list[zero_idx], input_list[i] = input_list[i], input_list[zero_idx]
            zero_idx += 1
            i += 1
        elif input_list[i] == 2:
            input_list[two_idx], input_list[i] = input_list[i], input_list[two_idx]
            two_idx -= 1
        else:
            i += 1
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
#[0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
#Pass
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
#Pass
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
#[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
#Pass
test_function([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
# Pass

#Edge cases
test_function([])
#[]
#Pass
test_function([0, 0, 0, 0, 0])
#[0, 0, 0, 0, 0]
#Pass


