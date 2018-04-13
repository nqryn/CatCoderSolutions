
def solve(test):
	print('_'*100)
	tokens = test.split()
	idx = 0
	fs, bs, bps = [], [], []
	while True:
		if idx == len(tokens):
			break
		status, day, value = tokens[idx:idx+3]
		day, value = int(day), int(value)
		if status == 'F':
			fs.append(value)
		elif status == 'B':
			bs.append(value)
			bps.append(day)

		idx += 3

	copy_fs = fs[:]
	end = len(bs)


	for day, pay in enumerate(fs):
		pass


	days = []
	print('_'*100)
	print(*fs)
	print(*copy_fs)
	for day, pay in enumerate(fs):
		if pay in copy_fs:
			days.append(day+1)
			print('For day {day} pay was not computable : {pay}'.format(day=day, pay=pay))


	return days





if __name__ == '__main__':

	with open('level3.in', 'r') as in_file, open('level3.out', 'w') as out_file:
		tc = int(in_file.readline())

		for _ in range(tc):
			test = in_file.readline()
			result = solve(test)

			print(*result, file=out_file)
