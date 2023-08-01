cd llama.cpp

# Download model
export MODEL=llama-2-70b-chat.ggmlv3.q4_0.bin
if [ ! -f models/${MODEL} ]; then
    curl -L "https://huggingface.co/TheBloke/Llama-2-70B-chat-GGML/resolve/main/${MODEL}" -o models/${MODEL}
fi
