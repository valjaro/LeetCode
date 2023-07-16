# https://cses.fi/problemset/task/1083/
n = int(input())
line = input().split()

missing_number = set(range(1, n+1)) - set(map(int, line))

print(missing_number.pop())