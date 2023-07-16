# https://cses.fi/problemset/task/1069/
line = input()

if len(line) == 1:
    print(1)
else:
    lst = []
    count = 1
    for i in range(1, len(line)):
        if line[i] == line[i -1]:
            count += 1
        else:
            lst.append(count)
            count = 1
    lst.append(count)
    print(max(lst))

