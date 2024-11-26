---
title: Tutorial for Missing MIT
tags: Markdown, Notes
author: WinstonCHEN1
date: July, 03, 2024
title: Day2-Missing MIT Semester
---


# Day2 The Missing Semester of Your CS Education

```{article-info}
:avatar: https://avatars.githubusercontent.com/u/163944337
:avatar-link: https://github.com/WinstonCHEN1/
:avatar-outline: muted
:author: [@WinstonCHEN1](https://github.com/WinstonCHEN1/)
:date: July, 03, 2024
:read-time: 10 min read 
:class-container: sd-p-2 sd-outline-muted sd-rounded-1
```

```{note}
This notes is translated from [The Missing Semester of Your CS Education](https://missing.csail.mit.edu/), 更多详情请参看原文。
```


## Topic 1 Shell

如今我们使用的大部分都是GUI，而有些时候GUI并不能帮我们完成所有的事情，这时候我们不得不回到Shell。

```
echo hello
hello
```

Shell会执行echo，将指定的hello参数打印。


```
missing:~$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
missing:~$ which echo
/bin/echo
missing:~$ /bin/echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

$PATH 指的是环境变量，如果你是Windows系统，你可以在此电脑>属性>高级系统设置里面找到它。通常来说，配置全局环境就与环境变量有关。

shell 中的路径是一组被分割的目录，在 Linux 和 macOS 上使用 / 分割，而在Windows上是 \。假设你进入了一个服务器，在根目录下使用`ls`命令可能会发现什么都没有，这是因为你没有进入磁盘的根目录。在路径中，`.` 表示的是当前目录，而 `..` 表示上级目录。


```
missing:~$ pwd
/home/missing
missing:~$ cd /home
missing:/home$ pwd
/home
missing:/home$ cd ..
missing:/$ pwd
/
missing:/$ cd ./home
missing:/home$ pwd
/home
missing:/home$ cd missing
missing:~$ pwd
/home/missing
missing:~$ ../../bin/echo hello
hello
```

还有一些常用命令：

`pwd`命令查看我们当前所在的路径

`cd`进入指定的路径

`ls` 命令查看指定目录下包含哪些文件

```
ls 显示当前目录下包含的文件
ls -a 显示当前目录下包含的文件，包括隐藏文件
ls -l -a 显示当前目录下包含的文件和隐藏文件，以及他们的详细信息
```

`man`命令查看程序名的文档

```
man ls
```
`mv`用于重命名或移动文件

`cp`用于拷贝文件

`mkdir`新建文件夹

`cat`连接文件，打印输出

我们可以对程序进行重定向。最简单的重定向是 `< file` 和 `> file`。这两个命令可以将程序的输入输出流分别重定向到文件：

```
missing:~$ echo hello > hello.txt
missing:~$ cat hello.txt
hello
missing:~$ cat < hello.txt
hello
missing:~$ cat < hello.txt > hello2.txt
missing:~$ cat hello2.txt
hello
```

使用 `>>` 来向一个文件追加内容。使用管道（ pipes ），我们能够更好的利用文件重定向。`|` 操作符允许我们将一个程序的输出和另外一个程序的输入连接起来。需要注意的是，`|`、`>`、和 `<` 是通过 shell 执行的，而不是被各个程序单独执行。 `echo` 等程序并不知道 `|` 的存在，它们只知道从自己的输入输出流中进行读写。

```
missing:~$ ls -l / | tail -n1
drwxr-xr-x 1 root  root  4096 Jun 20  2019 var
missing:~$ curl --head --silent google.com | grep --ignore-case content-length | cut --delimiter=' ' -f2
219
```

另外，有些操作需要你作为`root`用户才能进行，比如与操作系统有关的文件`sysfs`。`/sys`目录挂载了系统，你可以在`/sys`目录下找到一些`.sysfs`文件控制内核参数。当然，专属于Linux系统。

所以以控制屏幕亮度的程序为例，即使像下面这样写：

`$ sudo find -L /sys/class/backlight -maxdepth 2 -name '*brightness*'
/sys/class/backlight/thinkpad_screen/brightness
$ cd /sys/class/backlight/thinkpad_screen
$ sudo echo 3 > brightness
An error occurred while redirecting file 'brightness'
open: Permission denied`

我们已经使用了`sudo`命令（su是super user的意思，即root用户），系统在设置 `sudo echo` 前尝试打开 brightness 文件并写入，但系统拒绝了shell的操作，因为此时shell不是根用户。

```
$ echo 3 | sudo tee brightness
```

在这个程序中，打开`/sys`的是`tee`程序，而这个程序以**root**权限在运行，所以可以操作。

最后，如果你想更愉快的使用你的shell，你可以安装fish、oh-my-bash或是oh-my-zsh，通过命令行安装，网上都有很简单的教程。、

## Topic 2 Shell工具和脚本

包含以bash作为脚本语言的一些基础操作，以及几种最常用的shell工具。



## Topic 3 编辑器 (Vim)

目前最流行的代码编辑器无疑是VS Code，而VIM是最流行的基于命令行的编辑器。熟练使用VIM之后，编写代码可以完全脱离鼠标且效率极高，但这往往需要很久的时间进行练习。

VIM具有多种操作模式：

- 正常模式：在文件中四处移动光标进行修改
- 插入模式：插入文本
- 替换模式：替换文本
- 可视化模式（一般，行，块）：选中文本块
- 命令模式：用于执行命令

我们了解VIM可以通过这样一个例子开始，在不同的操作模式下，键盘敲击的含义也不同。比如，x 在插入模式会插入字母 x，但是在正常模式 会删除当前光标所在的字母，在可视模式下则会删除选中文块。

你可以按下 **ESC**（退出键）从任何其他模式返回正常模式。在正常模式，键入 **i** 进入插入 模式，**R** 进入替换模式，小写的**v** 进入可视（一般）模式，大写的**V** 进入可视（行）模式，**C-v** （Ctrl-V, 有时也写作 ^V）进入可视（块）模式，**引号:** 进入命令模式。

### 正常模式

- 基本移动: **hjkl** （左， 下， 上， 右）
- 词： **w** （下一个词）， **b** （词初）， **e** （词尾）
- 行： **0** （行初）， **^** （第一个非空格字符）， **$** （行尾）
- 屏幕： **H** （屏幕首行）， **M** （屏幕中间）， **L** （屏幕底部）
- 翻页： **Ctrl-u** （上翻）， **Ctrl-d** （下翻）
- 文件： **gg** （文件头）， **G** （文件尾）
- 行数： **:{行数}CR** 或者 **{行数}G** ({行数}为具体的行数)
- 杂项： **%** （找到配对，比如括号或者 /* */ 之类的注释对）
- 查找： **f{字符}**， **t{字符}**， **F{字符}**， **T{字符}**
  - 查找/到 向前/向后 在本行的{字符}
  - **,** / **;** 用于导航匹配
- 搜索: **/{正则表达式}**, **n** / **N** 用于导航匹配

### 命令行模式

在正常模式下键入 : 进入命令行模式。 在键入 : 后，你的光标会立即跳到屏幕下方的命令行。 这个模式有很多功能，包括打开，保存，关闭文件，以及 退出 Vim。
- :q 退出（关闭窗口）
- :w 保存（写）
- :wq 保存然后退出
- :e {文件名} 打开要编辑的文件
- :ls 显示打开的缓存
- :help {标题} 打开帮助文档
  - :help :w 打开 :w 命令的帮助文档
  - :help w 打开 w 移动的帮助文档  

### 可视化模式

可以用移动命令来选中。

- 可视化：**v**
- 可视化行： **V**
- 可视化块：**Ctrl+v**

### 插入模式

- **i** 进入插入模式
- **O** / **o** 在之上/之下插入行
- **d{移动命令}** 删除 {移动命令}
  - 例如，**dw** 删除词, **d$** 删除到行尾, **d0** 删除到行头。
- **c{移动命令}** 改变 {移动命令}
  - 例如，**cw** 改变词
  - 比如 **d{移动命令}** 再 **i**
- **x** 删除字符（等同于 **dl**）
- **s** 替换字符（等同于 **xi**）
- 可视化模式 + 操作
  - 选中文字, **d** 删除 或者 **c** 改变
- **u** 撤销, **C-r** 重做
- **y** 复制 / “yank” （其他一些命令比如 **d** 也会复制）
- **p** 粘贴
- **~** 改变字符的大小写

### 计数和修饰语

可以用一个计数来结合“名词”和“动词”，这会执行指定操作若干次。

- **3w** 向后移动三个词
- **5j** 向下移动5行
- **7dw** 删除7个词

可以用修饰语改变“名词”的意义。修饰语有 i，表示“内部”或者“在内”，和 a， 表示“周围”。

- **ci(** 改变当前括号内的内容
- **ci[** 改变当前方括号内的内容
- **da'** 删除一个单引号字符串， 包括周围的单引号

最后要说的是，如果你真的非常有耐心且通过长时间的练习掌握了以上这些命令，你可以在网上查找更多关于VIM的扩展资料，它远比目前介绍的要强。不过上手难度确实是很大，如果坚持不下去，还是选择VS Code吧。

## Topic 4 数据整理

数据整理与两样东西密切相关：用来整理的数据，以及相关的应用场景。

## Topic 5 命令行环境

### 信号机制

shell 会使用 UNIX 提供的信号机制执行进程间通信。当一个进程接收到信号时，它会停止执行、处理该信号并基于信号传递的信息来改变其执行。

- `SIGINT`信号：输入 `Ctrl-C` 时，shell 会发送一个**SIGINT**信号到进程，通知前台进程组终止进程。

- `SIGQUIT`信号：输入 `Ctrl-\` 时，shell会发送**SIGQUIT**信号到进程，进程在因收到**SIGQUIT**退出时会产生core文件, 在这个意义上类似于一个程序错误信号。

- `SIGTERM`信号：通常用来要求程序自己正常退出，shell命令kill缺省产生这个信号。如果进程终止不了，我们才会尝试SIGKILL。命令是`kill -TERM <PID>`。

- `SIGSTOP（SIGTSTP）`信号：输入 `Ctrl-Z` 时，shell会发送**SIGTSTP**信号（terminal版本的**SIGSTOP**）让进程暂停。

### 终端多路复用

在使用命令行时通常会希望同时执行多个任务，例如运行编辑器的同时，在终端的另外一侧执行程序，这时候就可以使用终端多路复用器，如**tmux**。

以下是tmux的基本操作：

#### 会话

每个会话都是一个独立的工作区，其中包含一个或多个窗口。

- `tmux` 开始一个新的会话
- `tmux new -s NAME` 以指定名称开始一个新的会话
- `tmux ls` 列出当前所有会话
- 在 `tmux` 中输入 `<C-b> d` ，将当前会话分离
- `tmux a` 重新连接最后一个会话。您也可以通过 `-t` 来指定具体的会话

#### 窗口

相当于编辑器或是浏览器中的标签页，从视觉上将一个会话分割为多个部分。

- `<C-b> c` 创建一个新的窗口，使用 `<C-d>`关闭
- `<C-b> N` 跳转到第 N 个窗口，注意每个窗口都是有编号的
- `<C-b> p` 切换到前一个窗口
- `<C-b> n` 切换到下一个窗口
- `<C-b> ,` 重命名当前窗口
- `<C-b> w` 列出当前所有窗口

#### 面板

像 vim 中的分屏一样，面板使我们可以在一个屏幕里显示多个 shell。

- `<C-b> "` 水平分割
- `<C-b> %` 垂直分割
- `<C-b> <方向>` 切换到指定方向的面板，<方向> 指的是键盘上的方向键
- `<C-b> z` 切换当前面板的缩放
- `<C-b> [` 开始往回卷动屏幕。您可以按下空格键来开始选择，回车键复制选中的部分
- `<C-b> <空格>` 在不同的面板排布间切换

### 别名

别名相当于一个长命令的缩写，shell会将其自动替换成原本的命令，语法如下：

```
alias alias_name="command_to_alias arg1 arg2"
```

等号的两边没有空格，因为`alias`是一个shell命令，只接受一个参数。

以下是一些别名的特性应用：

```
# 创建常用命令的缩写
alias ll="ls -lh"

# 能够少输入很多
alias gs="git status"
alias gc="git commit"
alias v="vim"

# 手误打错命令也没关系
alias sl=ls

# 重新定义一些命令行的默认行为
alias mv="mv -i"           # -i prompts before overwrite
alias mkdir="mkdir -p"     # -p make parent dirs as needed
alias df="df -h"           # -h prints human readable format

# 别名可以组合使用
alias la="ls -A"
alias lla="la -l"

# 在忽略某个别名
\ls
# 或者禁用别名
unalias la

# 获取别名的定义
alias ll
# 会打印 ll='ls -lh'
```

### 配置文件

shell的配置通过点文件来完成，一般来说点文件的文件名以`.`开头，默认是隐藏文件，直接使用`ls`并不会显示它们。

管理配置文件有很多好处，比如可以移植你的工具配置，快速安装，同步配置文件，追踪配置文件的版本历史等等。不同的工具有不同的配置文件目录，可以根据自己的工具查找配置。

可以通过在线文档和手册了解工具的设置项，网上也有很多其他人的配置文件，当然，每个人的操作习惯不同，建议不要直接复制别人的配置文件。

配置文件的一个常见的痛点是它可能并不能在多种设备上生效。可以通过配置文件的`if`语句解决。如果你有多个设备，你可以通过配置文件的管理实现特定配置需求。

### 远端设备

最常用的工具是**SSH**。可以使用ssh连接到其他服务器，例如`ssh foo@bar.mit.edu`。服务器可以通过 URL 指定（例如`bar.mit.edu`），也可以使用 IP 指定（例如`foobar@192.168.1.42`）。

ssh可以直接执行远程命令，`ssh foobar@server ls` 可以直接在用foobar的命令下执行 `ls` 命令。 想要配合管道来使用也可以， `ssh foobar@server ls | grep PATTERN` 会在本地查询远端 `ls` 的输出而 `ls | ssh foobar@server grep PATTERN` 会在远端对本地 `ls` 输出的结果进行查询。

ssh有基于密钥的验证机制，我们只需要向服务器证明客户端持有对应的私钥，而不需要公开其私钥。这样就可以避免每次登录都输入密码的麻烦了。

使用`ssh-keygen`命令可以生成一对密钥。要检查是否持有密码并验证它，您可以运行 `ssh-keygen -y -f /path/to/key`。ssh 会查询 `.ssh/authorized_keys` 来确认那些用户可以被允许登录。

#### 通过ssh复制文件

- `ssh+tee`, 最简单的方法是执行 `ssh` 命令，然后通过这样的方法利用标准输入实现 `cat localfile | ssh remote_server tee serverfile`。
- `scp` ：当需要拷贝大量的文件或目录时，使用`scp` 命令则更加方便，因为它可以方便的遍历相关路径。语法如下：`scp path/to/local_file remote_host:path/to/remote_file；`
- `rsync`对`scp`进行了改进，它可以检测本地和远端的文件以防止重复拷贝。它还可以提供一些诸如符号连接、权限管理等精心打磨的功能。甚至还可以基于`--partial`标记实现断点续传。`rsync`的语法和`scp`类似；

#### 端口转发

在本地设备上的一个端口建立连接，转发到远程端口上。例如在远程服务器上运行Jupyter notebook，监听8888端口，建立从本地9999端口的转发。使用 `ssh -L 9999:localhost:8888 foobar@remote_server` 。这样只需要访问本地的 `localhost:9999` 即可。

#### ssh配置

可以使用`~/.ssh/config`文件创建别名，这个文件也可以被当作配置文件，不过请注意，最好不要将它公开到互联网上，因为这会暴露服务器的各种信息。服务器侧的配置通常放在`/etc/ssh/sshd_config`。

### shell框架

可以通过框架来改进shell，让其拥有更友好的功能，包括但不限于向右对齐、命令语法高亮、历史子串查询、选项补全、智能补全、提示符主题等等，可以在网上自行了解，按需选取安装。

## Topic 6 版本控制(Git)

首先要明确，Git和GitHub完全是两回事！！

版本控制系统 (VCSs) 是一类用于追踪源代码（或其他文件、文件夹）改动的工具。版本控制系统有很多， 其事实上的标准则是 **Git**。

### Git 的数据模型

先用伪代码的形式看下数据模型:

```
// 文件就是一组数据
type blob = array<byte>

// 一个包含文件和目录的目录
type tree = map<string, tree | blob>

// 每个提交都包含一个父辈，元数据和顶层树
type commit = struct {
    parent: array<commit>
    author: string
    message: string
    snapshot: tree
}
```

#### blob object

当我们提交一些文件的时候，git会创建第一类对像**blob object**，每一个**blob object**对应提交的每个文件。

#### tree object

另外，git会创建一种对象**tree object**，包含项目中所有文件的列表，其中包含分配的blob object的指针，通过这种机制，git将文件与blob object相关联。

#### commit object

最后git会创建一个对象**commit object**，具有指向它的tree object的指针以及一些其他信息。

### 暂存区

暂存区允许我们指定下次快照中要包括哪些改动，比如你可以把需要提交的文件逐个放入暂存取，然后进行提交。通过这个机制，我们可以创建不同的独立提交。

### Git的命令行基础

#### 基本使用
- `git help <command>`: 获取 git 命令的帮助信息
- `git init`: 创建一个新的 git 仓库，其数据会存放在一个名为 .git 的目录下
- `git status`: 显示当前的仓库状态
- `git add <filename>`: 添加文件到暂存区
- `git commit`: 创建一个新的提
- `git log`: 显示历史日志
- `git log --all --graph --decorate`: 可视化历史记录（有向无环图）
- `git diff <filename>`: 显示与暂存区文件的差异
- `git diff <revision> <filename>`: 显示某个文件两个版本之间的差异
- `git checkout <revision>`: 更新 HEAD 和目前的分支
  
#### 分支和合并
- `git branch`: 显示分支
- `git branch <name>`: 创建分支
- `git checkout -b <name>`: 创建分支并切换到该分支
  - 相当于 `git branch <name>; git checkout <name>`
- `git merge <revision>`: 合并到当前分支
- `git mergetool`: 使用工具来处理合并冲突
- `git rebase`: 将一系列补丁变基（rebase）为新的基线
  
#### 远程操作

- `git remote`: 列出远端
- `git remote add <name> <url>`: 添加一个远端
- `git push <remote> <local branch>:<remote branch>`: 将对象传送至远端并更新远端引用
- `git branch --set-upstream-to=<remote>/<remote branch>`: 创建本地和远端分支的关联关系
- `git fetch`: 从远端获取对象/索引
- `git pull`: 相当于 git fetch; git merge
- `git clone`: 从远端下载仓库
  
#### 撤销
  
- `git commit --amend`: 编辑提交的内容或信息
- `git reset HEAD <file>`: 恢复暂存的文件
- `git checkout -- <file>`: 丢弃修改
- `git restore`: git2.32版本后取代git reset 进行许多撤销操作

Git也可以通过VS Code使用。

## Topic 7 调试及性能分析

### 调试

调试的第一种方法比较简单，在可能出现问题的地方添加一些打印语句，比如print、console等等，直到发现问题。

第二种方法是使用日志，可以将日志写入文件，socket甚至是发送到远端服务器；日志可以支持严重等级，比如哪些是ERROR、哪些是WARN；另外，日志包含的信息很多，很有可能直接包含了问题信息。

在与Web 服务器、数据库或消息代理等第三方依赖交互的时候，阅读日志非常重要。不过大多数的程序都会把日志保存在系统的某个地方。根据不同的系统有不同的保存位置。如果希望将日志加入到系统日志中，可以使用`logger`（一个shell程序）：

```
logger "Hello Logs"
# On macOS
log show --last 1m | grep Hello
# On Linux
journalctl --since "1m ago" | grep Hello
```

如果通过打印已经不足以满足调试的需求了，可以使用调试器。调试器可以设置断点，从断点开始逐步执行程序，即时查看变量的值，满足条件时暂停程序等。

这里介绍一下Python的调试器`pdb`。

- **l**(ist) - 显示当前行附近的11行或继续执行之前的显示；
- **s**(tep) - 执行当前行，并在第一个可能的地方停止；
- **n**(ext) - 继续执行直到当前函数的下一条语句或者 return 语句；
- **b**(reak) - 设置断点（基于传入的参数）；
- **p**(rint) - 在当前上下文对表达式求值并打印结果。还有一个命令是pp ，它使用 pprint 打印；
- **r**(eturn) - 继续执行直到当前函数返回；
- **q**(uit) - 退出调试器。

此外，针对不同的程序，可以使用不同的开发工具，请针对具体情况具体分析。

### 静态分析

静态分析会将程序的源码作为输入，基于编码规则对其进行分析，并对代码的正确性进行推理。可以使用静态分析工具。大多数的编辑器和 IDE 都支持在编辑界面显示这些工具的分析结果、高亮有警告和错误的位置。 这个过程通常称为 **code linting** 。风格检查或安全检查的结果同样也可以进行相应的显示。

不同的开发工具有不同的静态分析工具，网上有很多优秀的静态分析工具和使用教程。

### 性能分析

如何将一个代码从”能跑“进化到”优秀的代码“呢？性能分析是其中很重要的一环。我们可以学习性能分析和监控工具，借此找到程序中最耗时、最耗资源的部分。

通常来说，用户时间+系统时间代表了进程所消耗的实际CPU。

- 真实时间 - 从程序开始到结束流失掉的真实时间，包括其他进程的执行时间以及阻塞消耗的时间（例如等待 I/O或网络）；
- User - CPU 执行用户代码所花费的时间；
- Sys - CPU 执行系统内核代码所花费的时间。

性能分析工具通常指CPU性能分析工具。CPU 性能分析工具有两种：追踪分析器（tracing）及采样分析器（sampling）。追踪分析器 会记录程序的每一次函数调用，而采样分析器则只会周期性的监测（通常为每毫秒）程序并记录程序堆栈。比如Python使用的就是`cProfile`模块分析每次函数调用消耗的时间。

对于分析器的可视化，采样分析器常见的显示 CPU 分析数据的形式是**火焰图**，火焰图会在 Y 轴显示函数调用关系，并在 X 轴显示其耗时的比例。火焰图同时还是可交互的，可以深入程序的某一具体部分，并查看其栈追踪。

最后，有很多很多的工具可以监控不同的系统资源，比如CPU占用、内存使用、网络、磁盘使用等。

## Topic 8 安全和密码学

这部分会说明一些关于安全和密码学的简单概念。

### 熵

熵的单位是*比特*。对于一个均匀分布的随机离散变量，熵等于log_2(所有可能的个数，即n)。例如 “correcthorsebatterystaple” 这个密码比 “Tr0ub4dor&3” 更安全，因为前者有44比特的熵，后者只有28比特。假设每秒能进行1000次猜测，猜出前者的2^44种可能需要550年，而后者的2^28种可能只需要3天。

大约40比特的熵足以对抗在线穷举攻击（受限于网络速度和应用认证机制）。 而对于离线穷举攻击（主要受限于计算速度）, 一般需要更强的密码 (比如80比特或更多)。

### 散列函数

密码散列函数 (Cryptographic hash function) 可以将任意大小的数据映射为一个固定大小的输出。

### 密钥生成函数

密钥生成函数 (Key Derivation Functions) 被应用于包括生成固定长度，可以使用在其他密码算法中的密钥等方面。 为了对抗穷举法攻击，密钥生成函数通常较慢。

### 对称加密与非对称加密

对称加密，也称为私钥加密，是指加密和解密使用相同密钥的加密算法。在大多数对称算法中，加密密钥和解密密钥是相同的，因此也称为秘密密钥算法或单密钥算法。对称加密要求发送方和接收方在安全通信之前商定一个密钥。优势在于加密效率高，因为加密和解密使用相同的算法和密钥。然而，对称加密的安全性较低，因为如果密文被拦截且密钥被破解，信息就很容易被破译。常见的对称加密算法包括DES、AES和3DES等。

非对称加密，与对称加密不同，它使用一对密钥：公钥和私钥。公钥用于加密数据，而私钥用于解密数据。私钥只能由一方安全保管，不能外泄，而公钥可以发给任何请求它的人。非对称加密提供了更高的安全性，因为公钥和私钥是相互独立的，使用其中一个密钥加密的数据只能由另一个密钥解密。因此，不需要将私钥通过网络发送出去，安全性大大提高。目前最常用的非对称加密算法是RSA算法。
