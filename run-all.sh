#!/bin/bash

# Navigate to the directory containing the main executable and queries
cd llama.cpp

# Ensure outputs directory exists
mkdir -p ../outputs

# Define an array of file paths
query_files=(todo2)

# Loop through all .txt files in the queries directory
for query_file in "${query_files[@]}"; do
# for query_file in ../queries/*.txt; do
    # Extract the name of the query without the path and extension
    query_name=$(basename "$query_file" .txt)

    echo "Testing ${query_name}"

    cd ../
    python expand.py "${query_name}"
    cd llama.cpp


    for i in {1..3}; do
        # Clears log
        touch log.txt && echo "" > log.txt

        # Run the main command with modifications for each query
        ./main \
            --dynamic-grammar context \
            -t 10 \
            -ngl 64 \
            -b 512 \
            -m /Volumes/crucialx9/models/codellama-34b.Q5_K_M.v3.gguf \
            --color -c 3400 \
            --seed $i \
            --temp 0.8 \
            --top_k 5 \
            --repeat_penalty 1.1 \
            -n -1 \
            -f "../autoregressive.prompt" \
            --prelude "../autoregressive.common_prelude"

        # After running the command, move and rename log.txt to the outputs folder with a related name
        mv log.txt "../outputs/${query_name}_log_${i}.txt"
    done
done
