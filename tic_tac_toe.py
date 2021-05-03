from collections import defaultdict
class TicTacToe:
	def __init__(self, n = 3, current = 0):
		# current symbols: 0 or 1
		self.n = n
		self.board = [[None] * n for _ in range(n)]
		self.current = current
		self.count = 0
		self.is_finished = False

		self.out = {0: "O", 1: "X", None: " "}

		# marks moves
		self.rows = [defaultdict(int), defaultdict(int)]
		self.cols = [defaultdict(int), defaultdict(int)]
		self.diag1 = [0, 0]
		self.diag2 = [0, 0]

	def move(self, r, c):
		if self.is_finished:
			raise Exception("game finished")
		if not self.board[r][c] is None:
			raise Exception("already occupied")

		self.count += 1
		self.board[r][c] = self.current

		self.rows[self.current][r] += 1
		self.cols[self.current][c] += 1
		if r == c:
			self.diag1[self.current] += 1
		if r + c == self.n - 1:
			self.diag2[self.current] += 1

		if self.check(r, c):
			self.is_finished = True
			self.print()
			return

		self.current = (self.current + 1) % 2

	def check(self, r, c):
		# check if current symbol wins
		# or no more available spot
		if self.count == self.n * self.n:
			return True

		if (self.rows[self.current][r] == self.n
            or self.cols[self.current][c] == self.n
            or self.diag1[self.current] == self.n
            or self.diag2[self.current] == self.n):
            return True
            return False

	def print(self):
		for r in self.board:
			print([self.out[x] for x in r])
TicTacToe()
