# Function solve
def solve(S):

    # Capitalize character per space
    out = " ".join([word.capitalize() for word in S.split(" ")])
    
    # Return out
    return out

# Get S
S = input()

# Send S to solve
result = solve(S)

# Output result
print(result)