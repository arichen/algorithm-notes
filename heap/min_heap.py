class MinHeap:
    def __init__(self):
        self.array = []

    def insert(self, value):
        self.array.append(value)
        self.heapify_up(len(self.array) - 1)

    def pop(self):
        if not len(self.array):
            raise IndexError()

        value = self.array[0]
        last = self.array.pop()
        if len(self.array) > 0:
            self.array[0] = last
            self.heapify_down(0)

        return value

    def heapify_up(self, index):
        if not 0 <= index < len(self.array):
            return

        a = self.array
        parent = index // 2
        while a[index] < a[parent]:
            a[index], a[parent] = a[parent], a[index]
            index, parent = parent, parent // 2

    def heapify_down(self, index):
        a = self.array
        n = len(a)
        if not 0 <= index < n:
            return

        # the children index to swap
        child = None
        for i in range(index * 2, min(index * 2 + 2, n)):
            if a[i] < a[index]:
                child = i if (child is None or a[i] < a[child]) else child
        if child:
            a[child], a[index] = a[index], a[child]
            self.heapify_down(child)


if __name__ == "__main__":
    nums = [10,13,15,2,3,6,1,18,7,9]
    obj = MinHeap()
    [obj.insert(x) for x in nums]
    print(obj.array)

    print("-")
    print(obj.pop())
    print(obj.array)
    print(obj.pop())
    print(obj.array)
    print(obj.pop())
    print(obj.array)
    print(obj.pop())
    print(obj.array)