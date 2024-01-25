# Set up

1. Download the code llama model from: https://huggingface.co/AlienKevin/codellama-34b.Q5_K_M.v3.gguf/blob/main/codellama-34b.Q5_K_M.v3.gguf

2. Compile llama.cpp:
```
cd llama.cpp
make
```

3. Run model:
```
chmod +x run-code-34b.sh
./run-code-34b.sh
```

Uncomment the first line in `run-code-34b.sh` to change the prompt:
```
# python expand_prompt.py autoregressive list.filter
```
