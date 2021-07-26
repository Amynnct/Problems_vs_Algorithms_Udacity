This problem is similiar to problem 5, except we are working with a hierarchy of web pages instead of strings and each TrieNode is associated with a handler instead of the is_word property.

Time complexity:

- Insert takes O(n) with n is the number of path_part
- Find also takes O(n) with n is the number of path_part

Space complexity:

- Insert takes O(n) as the worst case if we insert the entire new path from the root.
- Find also takes O(n) for the worst case
