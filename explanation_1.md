In order to find the square root of an integer, we need to find a value that will get us itself when we used it as a divisor. First, we using an initial approximate value which equals to half of the given integer. Then, we divide the given integer by the guessed value. In some of our first loops, the guessing value (divisor) and the result usually far from each other. By using the avergage of these values as the next guess, we reduce the difference between the two.

As we only care about the floor value of the square root, we can stop when we reached a certain accuracy, and return the floor value.

Time and Space Complexity:
In this case time complexity is approximately O(log(n)) as if we image the divisor and its correspoding result define two ends of an array, we'll find that the size of this imaginary array will become smaller and smaller after each loop by approximately a factor of 2.
As for space complexity, it is independent of the input, thus O(1).
