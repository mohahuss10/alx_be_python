# control-flow/pattern_drawing.py

size = int(input("Enter the size of the pattern: "))
i = 1

while i <= size:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1
