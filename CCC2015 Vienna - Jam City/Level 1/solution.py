
def solve(n, m, cars):
	sol = [str(x[1] - x[0] + 2) for x in cars]
	return ','.join(sol)



if __name__ == '__main__':

	in_filename, out_filename = 'level1_{}.in', 'level1_{}.out'

	for i in range(1, 7):
		with open(in_filename.format(i), 'r') as in_file, open(out_filename.format(i), 'w') as out_file:
			n = int(in_file.readline()) # number of road segments
			m = int(in_file.readline()) # number of cars

			cars = []
			for _ in range(m):
				start, end = (int(x) for x in in_file.readline().split(',')) # Start and end segment for the current car
				cars.append((start, end))

			result = solve(m, n, cars)
			print(result)
			print(result, file=out_file)