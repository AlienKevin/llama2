cd llama.cpp

# Run in interactive mode
./server -m models/codellama-34b.Q5_K_M.gguf \
  --ctx_size 2048 \
  --threads 10 \
  --n-gpu-layers 32 \
  --batch-size 256
