cd llama.cpp

# --grammar-file ../hazel.gbnf \

./main \
    -t 10 \
    -ngl 64 \
    -b 512 \
    -m ../models/codellama-34b-instruct.Q5_K_M.gguf \
    --color -c 3100 \
    --temp 0.7 \
    --repeat_penalty 1.1 \
    -n -1 \
    -i -ins \
    -f ../prompt_adt-instruct.txt
