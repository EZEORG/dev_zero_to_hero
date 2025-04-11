# 使用llama.cpp量化模型

1. 首先克隆github中仓库

   ```
   git clone https://github.com/ggml-org/llama.cpp.git
   cd llama.cpp
   ```

2. CPU build

   ```
   cmake -B build
   cmake --build build --config Release -j 8
   ```

3. 从huggingface上下载模型，将模型转化为gguf格式

   ```
   python convert_hf_to_gguf.py [模型路径]
   ```

   运行结束之后，是fp16的gguf文件格式。

4. 之后进入到build/bin目录下

   ```
   ./llama-quantize -h   //查看有哪些量化方式
   ./llama-quantize models/gpt-2/ggml-model-f16.gguf(第三步转化好的文件) models/gpt-2/ggml-model-Q5_K_M.gguf(转化后的文件名称) Q5_K_M
   ```
