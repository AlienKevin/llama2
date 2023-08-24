cd llama.cpp

# Download model
export MODEL=codellama-34b.Q5_K_M.gguf
if [ ! -f models/${MODEL} ]; then
    curl -L "https://huggingface.co/TheBloke/CodeLlama-34B-GGUF/resolve/main/${MODEL}" -o models/${MODEL}
fi
