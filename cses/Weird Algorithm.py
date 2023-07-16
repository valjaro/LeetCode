# https://cses.fi/problemset/task/1068

n = int(input())
lst = []
lst.append(n)
while n != 1:
    n = int(n / 2 if n % 2 == 0 else n * 3 + 1)
    lst.append(n)
print(' '.join([str(elem) for elem in lst]))