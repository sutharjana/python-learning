n = 5

for i in range(1, n + 1):
    # Left pattern
    left = "* " * i

    # Middle pattern
    middle = "* " * (n - i + 1)

    # Right pattern (right-aligned)
    right = " " * (n - i) + "* " * i

    print(f"{left:<12} {middle:<12} {right}")