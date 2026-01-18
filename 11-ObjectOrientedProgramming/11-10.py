class C:
	def __init__(self, points):
		# points: list of [x, y] pairs
		self.points = points

	def m(self, n):
		# count points strictly in the first quadrant (x>0 and y>0)
		count = 0
		for p in self.points:
			try:
				x, y = p
			except Exception:
				continue
			if x > 0 and y > 0:
				count += 1
				if count >= n:
					return True
		return False


def main():
	c = C([[2,3],[1,8],[-6,4],[3,-7]])
	print("m(2) ->", c.m(2))
	print("m(3) ->", c.m(3))


if __name__ == "__main__":
	main()

