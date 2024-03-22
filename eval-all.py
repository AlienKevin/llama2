import os
import subprocess

# Define the array of file paths
query_files = ['playlist1', 'todo2']

outputs_dir = "outputs"

# Function to extract text between last occurrences of start and end strings in a file
def extract_text_between_last_occurrences_of(start, end, file_path):
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        content = file.read()
        start_index = content.rfind(start) + len(start)
        end_index = content.rfind(end)
        if start_index != -1 and end_index != -1:
            return content[start_index:end_index].strip()
    return ""

# Loop through all .txt files in the queries directory
for query_file in query_files:
    # Extract the name of the query without the path and extension
    query_name = os.path.basename(query_file).replace('.txt', '')

    subprocess.run(['python', 'expand.py', query_name])

    for i in range(1, 4):
        input_file_path = f"{outputs_dir}/{query_name}_log_{i}.txt"
        result = extract_text_between_last_occurrences_of("================", "LSP: Command: Completions(Context)", input_file_path)
        # result = extract_text_between_last_occurrences_of("================", "\n", input_file_path)
        
        output_file_path = f"{outputs_dir}/{query_name}_program_{i}.txt"
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(result)
        
        print(f"========{query_name}_{i}========")
        subprocess.run(['node', './lsp.js', 'CHECK', 'syntax', '--common', 'autoregressive.common', '--prelude', 'autoregressive.prelude', '--main', output_file_path])
        subprocess.run(['node', './lsp.js', 'CHECK', 'statics', '--common', 'autoregressive.common', '--prelude', 'autoregressive.prelude', '--main', output_file_path])
        subprocess.run(['node', './lsp.js', 'CHECK', 'dynamics', '--common', 'autoregressive.common', '--prelude', 'autoregressive.prelude', '--epilogue', f'testdata/{query_name}/epilogue.haze', '--main', output_file_path])
