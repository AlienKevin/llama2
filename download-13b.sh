cd llama.cpp

# Download model
export MODEL=llama-2-13b-chat.ggmlv3.q4_0.bin
if [ ! -f models/${MODEL} ]; then
    curl -L "https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML/resolve/main/${MODEL}" -o models/${MODEL}
fi
