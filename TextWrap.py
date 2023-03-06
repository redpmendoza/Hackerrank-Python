import textwrap

# Function wrap
def wrap(string, width):

    # Wrap the string
    wrapped = textwrap.wrap(string, width)

    # Join the strings
    wrapped = "\n".join(wrapped)

    # Return wrapped
    return wrapped

# Get input and width
inp = input()
wid = int(input())

# Output wrapped input
print(wrap(inp,wid))