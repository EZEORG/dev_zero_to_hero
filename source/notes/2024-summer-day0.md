---
title: Tutorial for markdown
tags: Markdown, Notes
author: WinstonCHEN1
date: June, 30, 2024
title: Day0-Markdown
---

# Day0 Markdown


目前，大部分的Github项目都是通过markdown进行轻量标注和沟通交流。
因此，掌握必要的语法，有利于进行沟通交流。

日常学习工作中， 避免不了使用别人的代码或者出现Bug需要上下游开发者帮助修复。提供较好的日志信息，将会项目的高效沟通。

除此之外，掌握一些markdown语法，也有利于未来自己的项目进行文档化的构建。
软件工程需要与人协作开发，并且需要别人能更容易的使用你的代码，在不用关注代码细节的情况下。

```{notes}
使用markdown的场景包括但不局限于：

1. 项目交流: Github Issues
2. 文档书写: [Pytorch Docs](https://pytorch.org/docs/stable/nn.html)
3. 写书
4. 做笔记
5. 发公众号

```



以下的一些资料将会有利于快速上手有一些常见的语法: 

- Markdown语法说明 [^markdown]
- [基本撰写和格式语法](https://docs.github.com/zh/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [An interesing introduction by us](./2024-summer-day0-1.md)



## Advanced Usages
正如前文提到，Markdown可以很好的用来写文档。因此除了标准语法外，[^MyST] 也提供了很多的高级功能，比如画流程图：

```{mermaid}
sequenceDiagram
  participant Alice
  participant Bob
  Alice->John: Hello John, how are you?
  loop Healthcheck
      John->John: Fight against hypochondria
  end
  Note right of John: Rational thoughts <br/>prevail...
  John-->Alice: Great!
  John->Bob: How about you?
  Bob-->John: Jolly good!
```





## Referenes:

1. [GitHub Flow](https://gitbeijing.com/github_flow.html)
2. [^markdown]: [The MyST Syntax Guide](https://myst-parser.readthedocs.io/en/v0.17.1/syntax/syntax.html#)
3. [^MyST]: [MyST Syntax Guide](https://myst-parser.readthedocs.io/en/v0.17.1/syntax/syntax.html#)

