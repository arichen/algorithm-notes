class KMP:
    def __init__(self):
        self.partial = None

    def find(self, s: str, pattern: str):
        pass

    def build_table(self, s: str):
        length = len(s)
        self.partial = [0 for _ in range(length)]

        for i in range(length):
            sub = s[:i + 1]
            for j in range(i, 0, -1):
                if sub[:j] == sub[i - j + 1:]:
                    self.partial[i] = j

        print(self.partial)

obj = KMP()
obj.build_table("abcdabd")