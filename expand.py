# Takes in two command arguments:
# 1. template name
# 2. prompt name

import sys

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
    if len(sys.argv) != 2:
        print("Usage: python expand.py <query_name>")
        sys.exit(1)
    
    query_name = sys.argv[1]

    common_content = read_file(f"testdata/common.haze") # + read_file(f"testdata/llama_extra.haze")
    write_file(f"autoregressive.common", common_content)

    prelude_content = read_file(f"testdata/{query_name}/prelude.haze")
    write_file(f"autoregressive.prelude", prelude_content)

    write_file(f"autoregressive.common_prelude", common_content + "\n" + prelude_content)

    sketch_content = read_file(f"testdata/{query_name}/sketch.haze").removesuffix("  ??\nin")
    write_file(f"autoregressive.sketch", sketch_content)

    prompt_content = common_content + "\n" + prelude_content + "\n" + sketch_content
    write_file(f"autoregressive.prompt", prompt_content)

if __name__ == "__main__":
    main()
