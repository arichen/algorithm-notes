Stack of Boxes

You are given a set of n types of rectangular 3-D boxes, where the i^th box has height h(i), width w(i) and depth d(i) (all real numbers). You want to create a stack of boxes which is as tall as possible, but you can only stack a box on top of another box if the dimensions of the 2-D base of the lower box are each strictly larger than those of the 2-D base of the higher box. Of course, you can rotate a box so that any side functions as its base. It is also allowable to use multiple instances of the same type of box.

Variation: cannot rotate boxes; Only one instance of each type of box.

## Thoughts (no rotation. one instance)
- Sort the box by width, and try each combination iteratively. -> Time Complexity: O(2^n)
- Optimization: dfs + memoization. we might already calculated the best result starting at this box.
- Bottom up: sort the box by width desc. DP array to track maximum height that ends with each box