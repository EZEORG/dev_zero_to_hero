---
title: Tutorial for Staring a Python project
tags: Markdown, Notes
author: WinstonCHEN1
date: July, 03, 2024
title: Day2-Missing MIT Semester
---


# Day3 Python 开发环境搭载


## Install Oh My Bash

```{note}
如果你更新了oh my bash，可能会出现终端配置清除的情况。这里影响最大的就是conda的配置，所以可以用这行命令：`~/anaconda3/bin/conda init`
```

## Tmux知识点补充

在Day2的semester课程中已经提到了Tmux的一些基本操作了。之前我们提过，多个 tmux 会话之间本质上是相互独立的。这里补充一些关于Tmux的概念：

- **tmux 会话之间没有共享的环境** ：每个会话有自己的窗口和窗格，每个窗格中运行的 shell 或程序也是独立的。会话之间不会自动共享任何环境变量、工作目录或进程状态
- **虚拟环境（virtualenv）是进程级别的** ：虚拟环境在 Python 中是通过修改环境变量来实现的，特别是 `PATH` 变量。当你在一个 tmux 窗格中激活虚拟环境时，这个虚拟环境的激活状态仅限于当前的 shell 会话。在其他 tmux 会话或窗格中，你需要单独激活所需的虚拟环境。

## Python虚拟环境的配置

现在我们默认已经在你想要的目录下了，接下来开始配置**Python**虚拟环境。

当然，首先你得需要相关依赖。

```
pip install virtualenv
```
接下来在安装好依赖之后，可以开始部署虚拟环境了。

- 创建一个虚拟环境：`virtualenv venv`
- 激活虚拟环境：`source venv/bin/activate`
- 退出虚拟环境：`deactivate`
  - 有些虚拟环境管理工具不支持 `deactivate` 命令，可以用`source deactivate`
  

## Python虚拟环境之Anaconda3
