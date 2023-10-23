cd llama.cpp

# Run in interactive mode
./server -m ../models/llama-2-13b-chat.ggmlv3.q4_0.bin \
  --ctx_size 2048 \
  --threads 8 \
  --n-gpu-layers 1 \
  --rms-norm-eps 1e-5 \
  --batch-size 256 \
  -gqa 1
