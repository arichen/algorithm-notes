# Calculator Problems

- Notes: universal way: use parser implementation. start with lowest priority, and recursive go to higher and higher priority.

- [224. Basic Calculator](https://leetcode.com/problems/basic-calculator/)
    - only `+`, `-`, `()`
    - special case:
        - handle signed numbers. e.g. `-1+2`, `+2+2`
        - signed paranthesis. e.g. `-(1+2)`
    - stack method:
        - think of `a-b` as `a+(-b)`, tracking sign and always do plus
        - use stack to track the result before `(` and the sign for this parenthesis.

- [227. Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/)
    - has `+`, `-`, `*`, `/`
    - stack method:
        - first thought: use two stacks, one for operands, and one for operators. If a low priority operation will be pushed over high priority operation, collapse (process the * or /, pop top two values, process and push back the result) until stack empty or a low priority operation is reached.
        - second thought: use the observation that `a-b` equals to `a+(-b)`, we don't need a separate stack for operators. if we see a minus operation, we push the `-b` onto stack. And when we see * and /, we immediately process the value and push the result to stack. Only 1 stack is needed.

- [772. Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/)


# Binary Expression Tree

- [1597. Build Binary Expression Tree From Infix Expression](https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/)
    - convert infix to postfix, and build the tree from postfix
    - use parser implementation. "a standard expression parser implementation where you call parse-functions on those with the lowest precendence and recursively invoke parse-functions of things with higher precendence."