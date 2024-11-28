for i in range(1, 50, 2):
    print(f"Number: {i}")

size = 5
for i in range(size):
    print("* " * size)

width = 7
height = 4
for i in range(height):
    print("* " * width)

for num1 in range(1, 4):
    for num in range(1, 4):
        print(f"Outer loop: {num1}, Inner loop: {num}")
