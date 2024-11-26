---
title: Tutorial for markdown
tags: Markdown, Notes
author: eze-root
date: 2024-07-16
title: Markdown
---

# Day0 Markdown

```{article-info}
:avatar: https://avatars.githubusercontent.com/u/154419224
:avatar-link: https://github.com/eze-root
:avatar-outline: muted
:author: [@eze-root](https://github.com/eze-root)
:date: 2024-07-16
:read-time: "10 min read"
:class-container: sd-p-2 sd-outline-muted sd-rounded-1
```



```{note}
除了本文的内容外，也可以参考某同学写的[学习心得](./2024-summer-day0-1.md)

```



目前，大部分的Github项目都是通过markdown进行轻量标注和沟通交流。
因此，掌握必要的语法，有利于进行沟通交流。

日常学习工作中， 避免不了使用别人的代码或者出现Bug, 需要上下游开发者帮助修复。提供较好的日志信息，将会推进项目的高效沟通。

除此之外，掌握一些markdown语法，也有利于未来自己的项目进行文档化的构建。
软件工程需要与人协作开发，并且需要别人能更容易的使用你的代码，在不用关注代码细节的情况下。

```{note}
使用markdown的场景包括但不局限于：

1. 项目交流
2. 文档书写
3. 写书
4. 做笔记
5. 发公众号

```


以下的一些资料将会有利于快速上手有一些常见的语法: 

- [基本撰写和格式语法](https://docs.github.com/zh/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [An interesing introduction by us](./2024-summer-day0-1.md)


## Advanced Usages
正如前文提到，Markdown可以很好的用来写文档。因此除了标准语法外，[^MyST] 也提供了很多的高级功能, 举例如下：

> [!NOTE]
> 高级用法需要用到sphinx，因此可能渲染需要用[^MyST]才有效果。

### 流程图

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

### 柄图

```{mermaid}

   pie title Pets adopted by volunteers
     "Dogs" : 386
     "Cats" : 85
     "Rats" : 15
```


### 添加Logo

> {octicon}`logo-github;1em;sd-text-info` is awesome!

{octicon}`logo-github;1em;sd-text-info` is awesome!


### Sphinx-Design

[sphinx-design](https://sphinx-design.readthedocs.io/en/latest/index.html)

::::{tab-set}

:::{tab-item} MacOS
这里是MacOS
:::

:::{tab-item} Windows
这里是windows
:::

::::


:::{card} Card Title
Header
^^^
Card content
+++
Footer
:::


## Awesome Usaegs:

1. 项目交流：[Report a bug for pytorch](https://github.com/pytorch/pytorch/issues/130666)
2. 文档书写：[Pytorch Docs Github](https://github.com/pytorch/pytorch/tree/main/docs)
3. 写书： [动手学深度学习](https://github.com/d2l-ai/d2l-zh)
4. 做笔记or写博客: [Chris Holdgraf](https://chrisholdgraf.com/)
5. 发公众号: [Doocs](https://doocs.github.io/md/)

欢迎添加更多的例子, 在下面的评论区，我们会尽快加入列表


## Referenes:
[^MyST]: [MyST Syntax Guide](https://myst-parser.readthedocs.io/en/latest/index.html)


 <div class="section" />
