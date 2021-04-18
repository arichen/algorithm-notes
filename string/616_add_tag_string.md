616. Add Bold Tag in String

### Thoughts
1. First used trie. Then n^2 search. => trie for early termination.
    -> code is kind of long
    -> used stack to handle merging intervals
    -> any unnecessary search? maybe can early terminate when a range already reached the end of string.
2. Search all words and mark a flag on the array which has len(s) length.