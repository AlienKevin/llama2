from hazel_samples import queries
import sys

# Check if an argument has been provided
if len(sys.argv) < 2:
    print("Usage: python gen_query.py <index>")
    sys.exit(1)

# Get the index 'i' from the command line
try:
    i = int(sys.argv[1])
except ValueError:
    print("Error: Please provide a valid integer for index.")
    sys.exit(1)

# Check if index 'i' is valid for the list of queries
if i < 0 or i >= len(queries):
    print(f"Error: Index out of range. Valid range is 0-{len(queries)-1}.")
    sys.exit(1)

prompt = [
    "USER: ",
    "ASSISTANT: ",
]

print(prompt[0] + queries[i].strip().replace("\n", "\\\n") + "\\")
print(prompt[1], end="")
