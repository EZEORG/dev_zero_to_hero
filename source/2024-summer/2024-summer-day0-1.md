---
title: Markdown入门
tags: Markdown, Notes
author: WinstonCHEN1
date: July, 16, 2024
title: Markdown 入门
---

# Day0 Markdown入门

```{article-info}
:avatar: https://avatars.githubusercontent.com/u/163944337
:avatar-link: https://github.com/WinstonCHEN1/
:avatar-outline: muted
:author: [@WinstonCHEN1](https://github.com/WinstonCHEN1/)
:date: June, 30, 2024
:read-time: 10 min read 
:class-container: sd-p-2 sd-outline-muted sd-rounded-1
```

## 前言

作为一名有几个月自媒体经验的卑微大学生，本人对 Markdown 可谓是又爱又恨。爱就爱在，这玩意确实很好用，有了它之后各种文档整的飞起。恨点主要在于，大部分情况下，提及 Markdown 就代表来工作了。

那么，Markdown 到底如何快速上手呢？其实我只用了半个小时，相信花一小会时间看完这份教程的你，一定能把比我学的更快。

首先，我们要了解一下，什么是Markdown。这是一种轻量级的标记语言，如果你了解HTML，那你上手 Markdown 一定超快，因为你大概不会用到超过十个不同的语法字符。当然，我也会使用一些HTML的例子进行类比，帮助你更快的上手。

另外，Markdown文件的后缀名是`.md`。

## 排版

在HTML中我们有很多不一样的标签，比如`<p>`、`<a>`等等，在这里，全部简化！只需要输入，输入，再输入，所见即为所得。

比如，你现在看到的这段文字：

Man！What can I say？Mamba Out！

这就是它的源代码了！

在Markdown里，换行很简单，按两下回车，让它空出一行，这就是换行了。我们来举个例子：

```
这是第一行。

这是第二行。
```
这是第一行。

这是第二行。


```
这是第一行。
这是第二行，但没有换行成功。
```
这是第一行。
这是第二行，但没有换行成功。

通过这样的一个例子，相信你已经看懂了换行。当然，如果你不确定标题、图片等等的元素到底需不需要空一行来换行，我的建议是：**只要不是非得黏在一起的，就换。**

## 标题

在HTML中标题就很简单，h1、h2...以此类推。在Markdown中，标题用井号#表示。一个#就是h1，两个就是h2，最多有几个？我也不知道，咱应该用不上那么多，如果我没记错，一般能有六个。

```
# 一级标题

## 二级标题
    
### 三级标题

#### 四级标题
```

一定要记得，井号后面一定要给一个空格，这样才会识别成标题。

## 列表

我们知道，列表分有序列表和无序列表。其实也很简单，往下的教程我就只写语法吧，没有什么需要解释的，熟能生巧。

列表如果需要写子列表，通常使用**缩进**控制。

```
- 无序列表 1
- 无序列表 2
  - 无序列表 2.1
  - 无序列表 2.2
```

- 无序列表 1
- 无序列表 2
  - 无序列表 2.1
  - 无序列表 2.2

```
1. 有序列表 1
2. 有序列表 2
3. 有序列表 3
```

1. 有序列表 1
2. 有序列表 2
3. 有序列表 3

## 引用

```
一级引用如下：

> ### 一级引用示例
> 
> 读一本好书。 **——歌德**
    
二级引用如下：

>> ### 二级引用示例
>>
>> 读一本好书。 **——歌德**

三级引用如下：

>>> ### 三级引用示例
>>>
>>> 读一本好书。**——歌德**
```

一级引用如下：

> ### 一级引用示例
> 
> 读一本好书。 **——歌德**
    
二级引用如下：

>> ### 二级引用示例
>>
>> 读一本好书。 **——歌德**

三级引用如下：

>>> ### 三级引用示例
>>>
>>> 读一本好书。**——歌德**

## 斜体和粗体

```
**这个是粗体**

*这个是斜体*
    
***这个是粗体加斜体***
```


**这个是粗体**

*这个是斜体*
    
***这个是粗体加斜体***

## 链接

```
[EZEORG-dev_zero_to_hero](https://github.com/EZEORG/dev_zero_to_hero)
```
[EZEORG-dev_zero_to_hero](https://github.com/EZEORG/dev_zero_to_hero)

也可以这么玩，加个星号
```
* [EZEORG-dev_zero_to_hero](https://github.com/EZEORG/dev_zero_to_hero)
```
* [EZEORG-dev_zero_to_hero](https://github.com/EZEORG/dev_zero_to_hero)

## 分割线和删除线

```
---
```

这里有一条分割线

---

这里有一条分割线

```
~~这是要被删除的内容。~~
```


~~这是要被删除的内容。~~

## 表格

这个其实我用的也不多，但是项目主页，这个超级实用。

```
| 姓名       | 年龄 |         工作 |
| :--------- | :--: | -----------: |
| 科比     |  18  |     篮球 |
| 蔡徐坤   |  20  |   唱，跳.. |
| 理塘丁真 |  22  | 宣传禁烟 |
```

| 姓名       | 年龄 |         工作 |
| :--------- | :--: | -----------: |
| 科比     |  18  |     篮球 |
| 蔡徐坤   |  20  |   唱，跳.. |
| 理塘丁真 |  22  | 宣传禁烟 |

## 代码块


```java
// FileName: HelloWorld.java
public class HelloWorld {
  // Java 入口程序，程序从此入口
  public static void main(String[] args) {
    System.out.println("Hello,World!"); // 向控制台打印一条语句
  }
}
```
这个，代码的效果就是它本身，不好展示。简而言之就是符号`，第一行三个，最后一行三个，中间的内容就会变成代码块了。记得是英文输入法！

支持以下语言种类：

```
bash
clojure，cpp，cs，css
dart，dockerfile, diff
erlang
go，gradle，groovy
haskell
java，javascript，json，julia
kotlin
lisp，lua
makefile，markdown，matlab
objectivec
perl，php，python
r，ruby，rust
scala，shell，sql，swift
tex，typescript
verilog，vhdl
xml
yaml
```

还有一个东西叫做行内代码，效果如下：
```
这是我的行内代码`python`
```
这是我的行内代码`python`

## 结语

这里我们再讲讲用什么玩意写md，其实VSCODE就很不错，记得安装插件，搜Markdown之后的第二个**Markdown Preview Enhanced**，别下错了。这样你就可以在VSCODE中预览你写的Markdown了。我本人用的是网上其他的编辑器，因为有些快捷键习惯了，如果你有中意的也可以，但这里只做VSCODE的推荐。

还有，在不同的页面上你可能会看到一些很帅的文档，其实它们也是md，但是采用了一些主题，就理解成游戏里的皮肤吧。如果喜欢，可以自己看看咋整。

好了，其实差不多也就到这了，会一点基础的，写一个简单的README肯定是没问题了（~~只是好不好看的问题~~）。祝学习顺利！
