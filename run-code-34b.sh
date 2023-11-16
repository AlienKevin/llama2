python expand_prompt.py autoregressive exp.subst

cd llama.cpp

./main \
    --grammar-file ../hazel.gbnf \
    -t 10 \
    -ngl 64 \
    -b 512 \
    -m ../models/codellama-34b.Q5_K_M.gguf \
    --color -c 3400 \
    --temp 0.7 \
    --repeat_penalty 1.1 \
    -n -1 \
    -f ../autoregressive.prompt
