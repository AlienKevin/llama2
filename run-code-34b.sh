cd llama.cpp

./main \
    -t 10 \
    -ngl 32 \
    -m models/codellama-34b.Q5_K_M.gguf \
    --color -c 2048 \
    --temp 0.7 \
    --repeat_penalty 1.1 \
    -n -1 \
    -i -ins
