# Get n
n = int(input())

# Check if n is even
if n % 2 == 0:

    # 2-5
    if n >= 2 and n <= 5:
        print("Not Weird")
    
    # 6-20
    elif n >= 6 and n <= 20:
        print("Weird")
    
    # > 20
    elif n > 20:
        print("Not Weird")

# n is odd
else:
    print("Weird")