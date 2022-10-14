"""
output

012345
01234
0123
012
01
"""
rows = 5
for i in range(rows, 0, -1):
    for j in range(0, i + 1):
        print(j, end=' ')
    print("\r")
