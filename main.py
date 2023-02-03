
for i in a:
    print(i)

print()

for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = 10
        elif i > j:
            a[i][j] = 999
