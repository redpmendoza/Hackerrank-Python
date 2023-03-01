# Get n
n = int(input())

# Get A values
A = map(int, input().split())

# Sort A
A = sorted(list(set(A)), reverse=True)

# Output index 1 in the list
print(A[1])