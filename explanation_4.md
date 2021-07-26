This problem can be done using two pointers, one for index of the next Zero and one for index of the next Two. We iterate through the array and swap the element if needed (swap zero to the head part of array, and two to the end part of the array)

Time and Space complexity:

- Iterate through the input list -> O(n)
  Due to non usage of auxiliary space -> space O(1)
