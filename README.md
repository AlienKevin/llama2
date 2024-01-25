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

Specify the prompt on the first line of `run-code-34b.sh`:
```
python expand_prompt.py autoregressive list.filter_int
```

`expand_prompt.py` will expand the `autorgressive.template`, write the expanded form
to `autoregressive.prelude`, and then concatenate the query from `queries/list.filter_int.txt` to the prelude and write the whole prompt (prelude + query) to `autoregressive.prompt`.
