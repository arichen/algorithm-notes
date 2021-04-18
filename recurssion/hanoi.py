class Hanoi:
    def __init__(self, n):
        self.n = n
        self.stacks = [list(range(n, 0, -1)), [], []]

    def play(self):
        self._move(self.n, 0, 2)

    def _move(self, num_discs, src, dst):
        print(self.stacks, num_discs, src, dst)
        if not num_discs or not self.stacks[src]:
            raise Exception()

        if num_discs == 1:
            self.stacks[dst].append(self.stacks[src].pop())
        else:
            tmp = 3 - src - dst
            self._move(num_discs - 1, src, tmp)
            self.stacks[dst].append(self.stacks[src].pop())
            self._move(num_discs - 1, tmp, dst)

if __name__ == "__main__":
    obj = Hanoi(3)
    print(obj.stacks)
    obj.play()
    print(obj.stacks)