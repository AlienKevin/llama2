cd llama.cpp

# Run in interactive mode
./server -m models/codellama-34b-instruct.Q5_K_M.gguf \
  --grammar-file grammars/hazel.gbnf \
  --ctx_size 2048 \
  --threads 10 \
  --n-gpu-layers 32 \
  --batch-size 256
