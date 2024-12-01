# HtmlRAG: HTML is Better Than Plain Text for Modeling Retrieved Knowledge in RAG Systems
[Jiejun Tan](https://scholar.google.com/citations?user=qHzX-cMAAAAJ&hl=en&oi=sra), [Zhicheng Dou](http://playbigdata.ruc.edu.cn/dou/), Wen Wang, Mang Wang, Weipeng Chen, Ji-Rong We  
https://arxiv.org/pdf/2411.02959
## Introduction
LLMs have demonstrated remarkable capabilities in natural language processing tasks. However, they often struggle with forgetting long-tailed knowledge, providing outdated information, and hallucination.  
<div style="text-align:center">
<img src="./imgs/HTMLRAG-2.png" width="500" style="text-align:center"/>  
</div>
RAG systems address these issues by incorporating external knowledge. Traditionally, RAG systems convert HTML to plain text, losing crucial structural and semantic information. This paper introduces HtmlRAG, a novel approach that utilizes HTML as the format for retrieved knowledge, preserving more information and improving RAG system performance.
## Methodology
![HTML for RAG pipeline overview](./imgs/HTMLRAG-1.png)
HtmlRAG tackles the challenge of excessive input length and noisy context in HTML documents. The methodology involves two main steps:  
**1. HTML Cleaning**  
![](./imgs/HTMLRAG-4.png)
- Removes irrelevant content like CSS, JavaScript, and comments.
- Merges redundant HTML structures without losing semantic information.  

For example, simplify the following
```html
<div><div><p>some  text</p></div></div>
```
as
```html
<p>some text</p>
```
**2. HTML Pruning**
- **Building a Block Tree**: Transforms the DOM tree into a block tree for efficient pruning.  
<div style="text-align:center">
<img src="./imgs/HTMLRAG-5.png" width="400" style="text-align:center"/>  
</div>
Suppose we have the following documents:  

```html
<!DOCTYPE html>
<html>
<body>
  <div>
    <h1>Title</h1>
    <p>This is a paragraph.</p>
    <p>This is another paragraph.</p>
  </div>
  <div>
    <h2>Subtitle</h2>
    <p>This is a subparagraph.</p>
  </div>
</body>
</html>
```
After the block tree is constructed, the block tree structure is as follows:
```
Block 1: <div><h1>Title</h1><p>This is a paragraph.</p><p>This is another paragraph.</p></div>
Block 2: <div><h2>Subtitle</h2><p>This is a subparagraph.</p></div>
```
The detailed pruning algorithm is as follows:  
<img src="./imgs/HTMLRAG-3.png" width="380" style="text-align:center"/>  
- **Pruning Blocks based on Text Embedding**: Removes blocks with low similarity to the user's query.  
<div style="text-align:center">
<img src="./imgs/HTMLRAG-6.png" width="380" style="text-align:center"/>  
</div>  

The approach involves extracting plain text from HTML blocks and calculating similarity scores with the user's query using text embeddings. A greedy algorithm is applied to prune the block tree by removing low-similarity blocks, while preserving higher ones. The pruning continues until the total length of the HTML documents fits within the set context window. Afterward, redundant HTML structures are removed, and nested tags are merged and empty tags are eliminated.
- **Generative Fine-Grained Block Pruning**: Further refines the block tree using a generative model.  
![](./imgs/HTMLRAG-7.png)  
The prompt for this step using a generative model is as follows:  
<div style="text-align:center">
<img src="./imgs/HTMLRAG-8.png" width="380" style="text-align:center"/>  
</div>  
To achieve finer granularity in block pruning, this paper expands the leaf nodes of the pruned block tree to obtain a finer-grained block tree. Given the limitations of embedding-based pruning, the paper proposes using a ** generative model **, as it can handle the entire block tree and is not limited to modeling one block at a time. However, directly processing the cleaned HTML (averaging 60K) with the generative model is impractical due to high computational costs. Inspired by CFIC, the paper uses a sequence of tags to identify a block, where the sequence starts from the root tag and ends at the block's tag, referred to as the "block path." During inference, the generative model calculates block scores based on the structure of the block tree.  

## Experiments and Results
HtmlRAG was tested on six QA datasets, including:  
- **ASQA**: a QA dataset consists of ambiguous questions that can be answered by multiple  answers supported by different knowledge sources;
- **HotpotQA**: a QA dataset consists of multi-hop questions;
- **NQ**:  A QA dataset containing real user’s queries collected by Google;
- **Trivia-QA**: a QA dataset containing real user’s questions;
- **MuSiQue**: A synthetic multi-hop QA dataset;
- **ELI5**: A  long-form QA dataset with questions collected from Reddit forum.  
## Conclusion
HtmlRAG demonstrates that using HTML as the format for retrieved knowledge in RAG systems is more effective than plain text. It retains richer semantics and structure, leading to improved performance. This work opens a new direction for research and provides a simple yet effective solution for processing HTML in RAG systems.
## Future Works
As LLMs continue to evolve, HTML's suitability as the format for external knowledge is expected to grow. Future work may develop better solutions for processing HTML in RAG systems, further enhancing the capabilities of LLMs.