If we were given a sorted array then to form two number with the maximum sum, we can simply set the larger elements to be the more significant digits. For ex, with 1, 2, 3, 4, 5 -> gives us 531, 42
with the first and second largest are 5 and 4, also are the most significant digits for two result numbers (then next are 3 then 2, and 1 to be the least significant digit).

=> We will sort the input array
=> iterate over the sorted array, poping the largest element, append it to first_num and the next one to second_num

Time and Space complexity

- As we use merge sort, the time complexity is O(nlogn)
- Iterate through the sorted list and form two required numbers takes O(n)
  => O(nlogn)
  Space complexity is O(logn) as we using recursive method.
