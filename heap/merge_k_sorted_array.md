Merge K Sorted Array

### Approach 1:
Iterate through each array and pick the min each time. Until all items are picked.
Time complexity: O(k * (k * n))

### Approach 2:
Heap.
1. Push the front element of each list to the heap. -> O(k)
2. Take out the min from heap. And add this element's next element to the heap. -> O(log(k) + log(k))
3. Continue until the heap is empty.

Time complexity: O(kn * log(k))

* key: Not pushing all items into heap all at once! Utilize the feature that each list is sorted.