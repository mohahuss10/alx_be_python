size = int(input("enter the size of the patter"))
row = 0

while row<size:
    for _ in range(size):
        print("*", end="")
    print()
    row +=1
    