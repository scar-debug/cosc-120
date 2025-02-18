# Even numbers between 1 and 100
print("Even numbers between 1 and 100:")
for num in range(2, 101, 2):
    print(num)

# Negative numbers between 1 and 100 (No output expected)
print("\nNegative numbers between 1 and 100:")
# This block will not execute, because it's a logically invalid range (no negative numbers between 1 and 100)
if False:  # This prevents the loop from running
    for num in range(-1, -101, -1):
        print(num)  # No output will happen
