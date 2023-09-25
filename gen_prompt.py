from hazel_samples import samples

prompt = [
    "USER: ",
    "ASSISTANT: ",
]

print(f"You are a coding assistant whose job is to complete the holes marked as ?? in a sketch and turn it into a full program.\n")

for (sketch, program) in samples:
    print(prompt[0] + sketch.strip())
    print(prompt[1] + program.strip())
    print()
