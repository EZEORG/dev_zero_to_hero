# Ollama导入自定义模型

Ollama 支持从 GGUF 文件导入模型，通过以下步骤来实现：

1. 下载 `.gguf` 文件

> 下载链接：<https://huggingface.co/RichardErkhov/Qwen_-_Qwen2-0.5B-gguf/resolve/main/Qwen2-0.5B.Q3_K_M.gguf?download=true>

下载后复制到第一部分的根目录下。可参考以下目录结构：

```bash
├── 从gguf直接导入/    
│   ├── Modelfile      
│   └── Qwen-0.5B.Q3_K_M.gguf 
   
```

2. 新建创建 Modelfile 文件

```python
FROM ./Qwen2-0.5B.Q3_K_M.gguf
```

3. 在 Ollama 中创建模型

> [!NOTE]
> 一定是在 Modelfile 文件所在的目录下运行以下终端指令！

```bash
ollama create mymodel -f Modelfile
```

4. 终端内运行模型

```bash
ollama run mymodel
```