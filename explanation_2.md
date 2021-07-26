A rotate sorted array is a nearly sorted array, in fact, we can divide it into two sorted subarray using the pivot point and perform binary search on each part.At the pivot point,two consecutive elements are out-of-order. We can utilize this properties to perform a binarysearch like algorithm to find the pivot.

Time and Space complexity:

- Find the pivot -> O(logn)
- Based on the condition, using binary search on the left or the right portion -> O(logn)
  --> O(logn)
  Since we implemented binary search using the iterative method, the space complexity is O(1)
