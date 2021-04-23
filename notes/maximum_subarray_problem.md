# Maximum Subarray Problems

- [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

- [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
    - Thought: same intuition of maximum subarray: for each item, see if we can take "append" to the max subarray ending with the previous item.
        - what's different: negative numbers. we can't just throw away negative products since a negative item will make it positive.

- [628. Maximum Product of Three Numbers](https://leetcode.com/problems/maximum-product-of-three-numbers/)
    - Thought 1 (Wrong!): use min heap, as iterating through array, always keep the max 3 item and heap. return the product of those 3.
        - What's wrong: doesn't work for e.g. [-100,-98,-1,2,3,4]
    - Thought 2: use backtrack and pick 3 numbers iteratively.
        - any duplicated work? -> not needed because we only need the 3 that makes top product. If we already seen (7,8,9) combo, a combo (1,2,3) is out of consideration -> sort the array, start from the largest number -> we just need largest 3 -> what about negative numbers? -> if there are negative numbers, the smallest 2 negative numbers can become a large positive number.
        - => largest 3 or smallest 2 and largest 1
        - => we don't need to sort the whole array, just need to keep track of largest 3 and smallest 2.