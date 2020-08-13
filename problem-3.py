count = 0
i = 1000
while i > 0:
    count += 1
    if count % 5 == 0:
        print(i, '\t', end='\n')
    else:
        print(i, '\t', end='')
    i -= 1
