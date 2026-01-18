class C:
	def __init__(self, data):
		# store a copy of the sectors dictionary
		self.data = dict(data)

	def m1(self, s, n):
		# set or update sector s with n fans
		self.data[s] = n

	def m2(self, s):
		# sum fans for sectors listed in string s
		return sum(self.data.get(ch, 0) for ch in s)


def main():
	stadium = C({"A":120, "D":150, "G":90, "K":110})
	stadium.m1("G", 130)
	print("m2('GD') ->", stadium.m2("GD"))   # expected 130 + 150 = 280
	print("m2('KEJ') ->", stadium.m2("KEJ")) # expected 110 (K) + 0 + 0 = 110


if __name__ == "__main__":
	main()

