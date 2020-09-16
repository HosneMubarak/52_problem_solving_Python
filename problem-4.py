T = int(input())
i = 1
while i < T:
    N = int(input())
    print("Case {0} :".format(i), end='')
    for j in range(1, N+1):
        if N % j == 0:
            print(j, end=' ')
    print('\n')
    i -= 1
