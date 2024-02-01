python expand_prompt.py autoregressive shape.volume

cd llama.cpp

rm log.txt

./main \
    --dynamic-grammar context \
    -t 10 \
    -ngl 64 \
    -b 512 \
    -m ../models/codellama-70b-hf.Q5_K_M.gguf \
    --color -c 3400 \
    --seed 1 \
    --temp 0 \
    --repeat_penalty 1.1 \
    -n -1 \
    -f ../autoregressive.prompt \
    --prelude ../autoregressive.prelude
