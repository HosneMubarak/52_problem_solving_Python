n = int(input("Enter a value for take input?"))
for i in range(0, n):
    j = input("Enter value:")
    k = int((j[-1:]))
    if k % 2 == 0:
        print("Even")
    else:
        print("Odd")
