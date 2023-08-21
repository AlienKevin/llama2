cd llama.cpp

# Run in interactive mode
./server -m ./models/llama-2-13b-chat.ggmlv3.q4_0.bin \
  --ctx_size 2048 \
  -t 8 \
  -ngl 1 \
  -eps 1e-5 \
  -b 256 \
  -gqa 1
