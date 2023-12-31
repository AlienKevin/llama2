cd llama.cpp

./main \
    --grammar-file ../hazel.gbnf \
    -t 10 \
    -ngl 64 \
    -b 512 \
    -m ../models/mistral-7b-v0.1.Q5_K_S.gguf \
    --color -c 2000 \
    --temp 0.7 \
    --repeat_penalty 1.1 \
    -n -1 \
    -f ../prompt_adt-autoregressive.txt
