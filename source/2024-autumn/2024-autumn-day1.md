如何高效的使用ChatGPT？

对于用户来说，提示词就是与GPT等大模型交互的过程中最重要的一环。写好提示词，对于使用效率和准确程度有着极大的提升。

比如我们可以参考 Matt Nigh 的CRISPE框架，这是一个用于编写复杂内容prompt的工具。大致分为以下几个方面：
- CR（能力与角色）：定义你希望ChatGPT扮演的角色和其能力范围。
- I（洞察）：提供背景信息和上下文以指导ChatGPT。
- S（陈述）：明确指出你希望ChatGPT执行的任务。
- P（个性）：设定ChatGPT回答的风格或方式。
- E（实验）：让ChatGPT提供多种可能的答案选项。

基于CRISPE框架，如果想要ChatGPT写一篇关于气候变化的文章，最终的提示词可能是这样的：

> 作为一个专业研究气候变化的科学家（CR：能力与角色），请基于当前的科学共识和最新的研究数据（I：洞察），撰写一篇详细且科学严谨的报告（S：陈述），内容需涵盖气候变化的原因、影响以及可能的解决方案。请采用客观且权威的写作风格（P：个性），并提供几种不同的结构和论点供选择（E：实验）。

# 提问技巧

- **使用行动词开头。**使用“编写一个程序文件，要求是xxx”，而不是“你能帮我编写一个要求为xxx的文件吗？”。基于行动词的提示会有更加准确高效的回答。
- **给予模型一个“角色”。**例如，“你现在是机器学习领域的专家，请协助我完成xx”，可以让模型更加专注于相应领域，实现更加精确详细的回答。
- **使用清晰的口吻。**避免在撰写提示词的时候使用模棱两可的口吻，例如“可能可以”，这可能导致回答同样模糊。
- **添加上下文信息。**可以提供详细的上下文信息帮助模型理解，例如你需要模型帮你修改某部分的代码，可以在提示词中声明“我正在进行一个xxx样的项目，要求是xxx”。
- **添加限定信息。**对于你的部分具体要求，可以直接在prompt中对模型进行限制，例如“除了某部分的代码，不要修改其他任何部分”和“对于没有修改的部分，在生成的代码中直接省略”等。

# 提问模板示例

## 文章书写

### 选题相关

1. 为[你的研究领域]提供一些学术论文的具体主题建议。 Offer specific academic paper topic suggestions for [your research field].
2. 作为我的头脑风暴伙伴，帮我找一些适合[你的研究领域]的学术论文主题。
As my brainstorming partner, help me find some academic paper topics suitable for [your research field].
3. 在[你的研究领域]中，列出一些与[具体兴趣或主题]相关的学术论文题目。
List some academic paper titles within [your research field] related to [specific interest or theme].

### 大纲构建相关

1. 如何为[你的具体主题]撰写论文？请提供一个大纲或章节标题。
How can I write a paper on [your specific topic]? Provide an outline or section titles.
2. 我正在编写关于[具体主题，例如，“生物多样性损失”]的论文。应如何安排[选择的部分，例如，“讨论”]以包含[特定学科，例如，“社会经济学”]的观点和[指定地区或生态系统，例如，“热带雨林”]的发现？
I’m writing a paper on [specific topic, e.g., “biodiversity loss”]. How should I arrange the [chosen section, e.g., “Discussion”] to include perspectives from [specific discipline, e.g., “socio-economics”] and findings from [specified region or ecosystem, e.g., “tropical rainforests”]?
3. 作为我的论文结构顾问，能否建议关于[主题，例如，“量子物理”]的逻辑流程和章节标题，特别是当我打算涵盖[特定元素，例如，“量子纠缠和传输”]时？
As my structural consultant, could you suggest a logical flow and section titles for a paper on [topic, e.g., ‘quantum physics’], especially when covering aspects like [specific elements, e.g., ‘quantum entanglement and teleportation’]?

### 格式校对相关

1. 检查这段文字是否存在语法或风格问题：[在此处粘贴您的文本]。
Check this passage for any grammatical or stylistic issues: [paste your text here].
2. 请仔细审查我[文件类型]中关于[具体主题]的这一部分。标出任何语言或结构上的问题，并建议如何更好地符合[目标出版物或受众]的风格：[在此处粘贴您的文本]。
Kindly review this segment from my [type of document] on [specific topic]. Highlight any linguistic or structural issues and suggest how it might better fit the style of [target publication or audience]: [paste your text here].
3. 担任我的校对者。请检查这段文字：[在此处粘贴您的文本]，看看是否有语法或风格问题。
Act as my proofreader. Please check this passage: [paste your text here] for any grammatical or stylistic issues.

### 引用相关

1. 担任引用指南。我需要为我的工作引用一篇[来源类型]。我应该如何使用[引用风格]方法来格式化这个引用？
Act as a citation guide. I need to reference a [source type] for my work. How should I format this using the [citation style] method?
2. 我应该如何按照[所需风格]格式来编排这个引用？这是来源：[在此处粘贴来源详情]。
How do I format this citation in [desired style]? Here’s the source: [paste source details here].
3. 我引用了一篇由[作者姓名]在[年份]发布的[来源类型]。我应该如何以[所需风格]格式展示？
I’ve sourced a [type of source] from [author’s name] published in [year]. How should I present this in [desired style] format?

### 改写相关

1. 请你作为文字专家，帮我重新表述这段话，但保持其核心意思：[在此处粘贴您的原始声明]。
As a word expert, please help me rephrase this statement while keeping its core meaning: [paste your original statement here].
2. 请你扮演我的改写助手。这里有一段来自[作者姓名]的研究内容：[在此处粘贴原始声明]。我怎样才能在不剽窃的情况下表达这一点？
Act as my rephrasing assistant. Here is a statement from [author’s name]’s research: [paste original statement here]. How can I express this without plagiarizing?
3. 请帮我改写以下内容：[在此处粘贴您的原始声明]。
Could you assist me in rewording the following statement? [paste your original statement here].

## 代码辅助

### 代码重构

你是一名经验丰富的软件工程师，以下是一段冗余的代码，请进行重构，使其更加简洁和高效。

代码内容：代码

### 漏洞修复

你是一名Bug修复专家，请找出以下代码中的Bug并修复：

代码：请插入代码

目标：确保代码能够正常运行

### 辅助编写

你是一名数据工程师，准备为新闻网站编写一个爬虫脚本：

核心功能：获取文章标题、文章链接、发布时间

脚本细节：使用playwright和xpath、设置代理、避免封IP

当然有的时候也可以不用这么麻烦，你可以直接对模型说：找出这段代码中的问题进行总结。然后针对总结出的问题，考虑解决方案，再经过不断的调试，最终能得到一份“教科书”般的代码。只要能让模型精确快速的理解你的需求，并解决了实际问题，那就能说这是一次成功的使用！

# 长上下文模板示例

Prompt全流程，需要保持前后一致，指令一致，角色一致。尽量让指令更加明确和详细，这决定了AI的生成质量。但也不是越详细就越好，需要兼顾“结构化”与“简洁”原则。此外，要在对话的过程中不断迭代优化。

```
## Role（角色）: xx助手
## Profile（概述）: 
- author（作者）: xxx
- version（版本）: xx 
- language（语言）: xx 
- description（描述）: 你是⼀个xx，通过对⽤户的xx进⾏xx动作，输出xx结果，以帮助⽤户xx。

## Goals（目标）:
- xx
- xx

## Skills（技能）: 
- xx
- xx

## Constrains（指令）: 
- xx
- xx

## Attention（注意事项）：
- xx
- xx

## Workflows（工作流程）:
- xx
- xx

## example （例如）:
- xx
- xx

## output（输出）：
- xx
- xx

## Initialization（初始化）:
欢迎⽤户，并提示⽤户输⼊信息 
```
