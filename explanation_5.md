In this problem, we use Trie or a Prefix Tree to implement an autocomplete function. Thus, the time and space complexity is generally similar to Tree.

Time complexity

- For a trie, time complexity of Insert operation takes O(n) with n is each char in the word (as we iterate over each char, creating a new TrieNode, and assigning as node for next iteration)
- Same with Find operation O(n) (iterate over each char in word, get char in node.children, assign children[char] as node for next iteration)
- Suffixes operation takes O(n \* m) with n is the number of iteration and m is the suffixes operation with the children of each child

Space complexity

- space are used for the recusive stack, thus it is O(n \* m) for n is number of child and m is the children of each child.
