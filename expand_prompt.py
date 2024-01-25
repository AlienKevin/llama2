# Takes in two command arguments:
# 1. template name
# 2. prompt name

import sys
import re

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")
        sys.exit(1)

def write_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except IOError as e:
        print(f"Error writing to file {file_path}: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Usage: python expand_prompt.py <template_name> <query_name>")
        sys.exit(1)

    template_name = sys.argv[1]
    query_name = sys.argv[2]

    prompt_content = read_file(f"{template_name}.template")
    included_modules = re.findall(r'\\include (\w+)', prompt_content)

    for module in included_modules:
        module_content = read_file(f"modules/{module}.txt")
        prompt_content = prompt_content.replace(f"\\include {module}", module_content)

    write_file(f"{template_name}.prelude", prompt_content)

    prompt_content += read_file(f"queries/{query_name}.txt")

    write_file(f"{template_name}.prompt", prompt_content)
    print(f"Processed prompt saved as {template_name}.prompt")

if __name__ == "__main__":
    main()
