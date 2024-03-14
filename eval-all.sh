# Define an array of file paths
query_files=(../queries/playlist.txt ../queries/widget.find_all_widgets_of_type.txt)

find_last_occurrence() {
  local textA="$1"
  local textB="$2"
  local file="$3"

  # Use awk to process the file, find the last occurrence of the pattern
  awk -v textA="$textA" -v textB="$textB" '
  {
    if ($0 ~ textA) {
      capture = 1; 
      buffer = ""; 
      next; 
    }
    if ($0 ~ textB && capture) {
      capture = 0;
      lastMatch = buffer;
      next;
    }
    if (capture) {
      if (buffer == "") {
        buffer = $0;
      } else {
        buffer = buffer "\n" $0;
      }
    }
  }
  END {
    if (lastMatch != "") print lastMatch;
  }' "$file"
}

# Loop through all .txt files in the queries directory
for query_file in "${query_files[@]}"; do
    # Extract the name of the query without the path and extension
    query_name=$(basename "$query_file" .txt)

    result=$(find_last_occurrence "================" "LSP: Process" "outputs/${query_name}_log.txt")
    echo "$result" > outputs/${query_name}_program.txt
    
    echo "========${query_name}========"
    node ./lsp.js CHECK syntax --prelude autoregressive.prelude --main outputs/${query_name}_program.txt
    node ./lsp.js CHECK statics --prelude autoregressive.prelude --main outputs/${query_name}_program.txt
done
