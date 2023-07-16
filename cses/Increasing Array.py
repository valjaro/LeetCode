# https://cses.fi/problemset/task/1094
n = int(input())
line = list(input().replace(" ",""))
line = [int(x) for x in line]
count = 0
for i in range(n):

	swapped = False

	for j in range(0, n - i - 1):
		
		if line[j] > line[j + 1]:
			line[j], line[j + 1] = line[j + 1], line[j]
			count += 1

			swapped = True
	
	if not swapped:
        break

print(count)
