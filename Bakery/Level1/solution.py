
def solve(test):
	tokens = test.split()
	idx = 0
	days = [0] * (len(tokens) // 6 + 1)
	while True:
		if idx == len(tokens):
			break
		status, day, value = tokens[idx:idx+3]
		if status == 'F':
			days[int(day)] += int(value)
		elif status == 'B':
			days[int(day)] -= int(value)

		idx += 3
	result = [i for i, val in enumerate(days) if val != 0]

	return result





if __name__ == '__main__':

	with open('level1.in', 'r') as in_file, open('level1.out', 'w') as out_file:
		tc = int(in_file.readline())

		for _ in range(tc):
			test = in_file.readline()
			result = solve(test)

			print(*result, file=out_file)
