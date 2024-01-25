python expand_prompt.py autoregressive list.filter_int

cd llama.cpp

rm log.txt
rm log-pieces.txt

./main \
    --dynamic-grammar \
    -t 10 \
    -ngl 64 \
    -b 512 \
    -m ../models/codellama-34b.Q5_K_M.v3.gguf \
    --color -c 3400 \
    --seed 1 \
    --temp 0 \
    --repeat_penalty 1.1 \
    -n -1 \
    -f ../autoregressive.prompt \
    --prelude ../autoregressive.prelude
