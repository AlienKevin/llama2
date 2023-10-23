cd llama.cpp.70b

# Run in interactive mode
./main -m ../models/llama-2-70b-chat.ggmlv3.q4_0.bin \
  --color \
  --ctx_size 2048 \
  -n -1 \
  -ins -b 256 \
  --top_k 10000 \
  --temp 0.2 \
  --repeat_penalty 1.1 \
  -t 8 \
  -gqa 8 \
  -ngl 1

# >10 seconds to start answer

# llama_print_timings:        load time =  2137.03 ms
# llama_print_timings:      sample time =  3781.39 ms /  1113 runs   (    3.40 ms per token,   294.34 tokens per second)
# llama_print_timings: prompt eval time = 187350.18 ms /   408 tokens (  459.19 ms per token,     2.18 tokens per second)
# llama_print_timings:        eval time = 194380.93 ms /  1113 runs   (  174.65 ms per token,     5.73 tokens per second)
