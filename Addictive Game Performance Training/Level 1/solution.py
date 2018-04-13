def pretty_print(mat, rows, cols):
	print('_' * 2 * cols)
	for row in mat:
		print('|'.join([str(v) for v in row]))
		print('_' * 2 * cols)
	print()




def read_input():

	with open('level1-1.in') as in_file:
		numbers = in_file.read().split()

		tc = int(numbers[0])
		idx = 1

		for _ in range(tc):
			rows, cols = int(numbers[idx]), int(numbers[idx+1])
			nb_points = int(numbers[idx+2])

			# Define the matrix
			mat = []
			for k in range(rows):
				mat.append([0] * cols)

			idx += 3
			for x in range(nb_points):
				# Read next point
				pos, colour = int(numbers[idx]), int(numbers[idx+1])
				pos -= 1
				mat[pos//cols][pos%cols] = colour

				idx += 2

			idx += 1 # Skip the 0 at the end of the test case
			pretty_print(mat, rows, cols)


read_input()