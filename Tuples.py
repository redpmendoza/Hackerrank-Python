# Get n
n = int(input())

# Get values of int list
int_list = map(int, input().split())

# Create tuple
t = tuple(int_list)

# Output hash
print(hash(t))