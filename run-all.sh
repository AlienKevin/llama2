#!/bin/bash

# Navigate to the directory containing the main executable and queries
cd llama.cpp

# Ensure outputs directory exists
mkdir -p ../outputs

# Define an array of file paths
query_files=(../queries/playlist.txt ../queries/todo.add.txt ../queries/todo.remove.txt ../queries/todo.toggle.txt ../queries/todo.update.txt)

skip_files=("list.filter_map_int", "list.find_int")

# Loop through all .txt files in the queries directory
for query_file in "${query_files[@]}"; do
# for query_file in ../queries/*.txt; do
    # Extract the name of the query without the path and extension
    query_name=$(basename "$query_file" .txt)

    for i in "${skip_files[@]}"; do
        if [[ "$i" == "$query_name" ]]; then
            echo "Skipping ${query_name}"
            continue 2
        fi
    done

    echo "Testing ${query_name}"

    cd ../
    python expand_prompt.py autoregressive "${query_name}"
    cd llama.cpp


    # Clears log
    touch log.txt && echo "" truncate -s 0 log.txt

    # Run the main command with modifications for each query
    ./main \
        --dynamic-grammar types \
        -t 10 \
        -ngl 64 \
        -b 512 \
        -m ../models/codellama-34b.Q5_K_M.v3.gguf \
        --color -c 3400 \
        --seed 1 \
        --temp 0 \
        --repeat_penalty 1.1 \
        -n -1 \
        -f "../autoregressive.prompt" \
        --prelude "../autoregressive.prelude"

    # After running the command, move and rename log.txt to the outputs folder with a related name
    mv log.txt "../outputs/${query_name}_log.txt"
done
