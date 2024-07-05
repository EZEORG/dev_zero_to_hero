# Day1 Linux、VScode与Git

## 一、Basic Linux


### 1. 文件和目录管理

列出当前目录下的文件列表
```
ls

```

显示当前工作目录的路径
```
pwd
```

进入目录

```
cd /path/to/directory（请替换需要进入的路径）
```

显示磁盘结构，包括各个磁盘的挂载点

```
lsblk
```


### 2. 系统监控和任务管理


显示任务管理器，监控系统进程

```
top
```

美化版的top，提供更直观的任务管理界面

```
btop
```


### 3. 清理屏幕

清空当前终端页面
```
clear
```

### 4. 网络和系统信息

查看curl命令的文档

```
man curl
```


查看当前IP地址

```
curl ip.sb
```

使用curl测试网络连接，使用谷歌可查看是否能访问外网
```
curl baidu.com
curl google.com
```

显示每个接口的详细信息
```
ip a
```

### 5. 文件传输和安装

使用scp命令进行文件传输

```
scp file.txt username@remotehost:/path/to/destination/
```

运行bash脚本进行安装
```
bash install.sh
```

### 6. VIM快捷键
向下移动

```
J
```
向上移动
```
K
```
退出VIM（组合键）
```
:q
```

### 7. Python和虚拟环境管理
创建Python虚拟环境，用于隔离项目的依赖环境
```
virtualenv myenv
```

## 二、VScode


### Extension


#### 1.Remote
安装Remote插件, 然后进行服务器的登录操作
![image.png](https://cdn.nlark.com/yuque/0/2024/png/43076700/1719925146461-f8bf3229-c1d0-4082-88ee-6c9464920a62.png#averageHue=%23303942&clientId=ud3b6b92c-252e-4&from=paste&height=72&id=u7f5c4d03&originHeight=72&originWidth=249&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5064&status=done&style=none&taskId=ube1af80b-f928-494d-9411-5ab3a601e82&title=&width=249)


#### 2.简体中文
如果不习惯看英文，可以安装简体中文的插件
![image.png](https://cdn.nlark.com/yuque/0/2024/png/43076700/1719925162642-0d700547-4947-4b13-ae13-f465b45fb658.png#averageHue=%232f373f&clientId=ud3b6b92c-252e-4&from=paste&height=74&id=ucc5e036b&originHeight=74&originWidth=250&originalType=binary&ratio=1&rotation=0&showTitle=false&size=6301&status=done&style=none&taskId=ub71f9b60-5f50-4ccf-8acb-607af93fa88&title=&width=250)


#### 3.Python
VSCode中Python开发环境支持的插件
![image.png](https://cdn.nlark.com/yuque/0/2024/png/43076700/1719925182463-3510f60a-9563-4f8e-9dc8-6de9941c932c.png#averageHue=%233d4956&clientId=ud3b6b92c-252e-4&from=paste&height=71&id=u566b79b5&originHeight=71&originWidth=247&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5240&status=done&style=none&taskId=u9f99da98-b4c1-4d1a-b2d1-1f86df7bd6e&title=&width=247)


### VSCode连接服务器
在安装好remote插件后，就可以连接到服务器了。
点击这个按钮：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/43076700/1719925705407-e7e0d283-4126-4bb4-b855-a1cdce5f9c7c.png#averageHue=%232c3136&clientId=u0c009d04-de1b-4&from=paste&height=55&id=u24a6a018&originHeight=55&originWidth=164&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3336&status=done&style=none&taskId=uab81b8ae-2e4a-4cc1-9cbe-92a3c297b5a&title=&width=164)
左边栏空空如也，点击这个加号按钮：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/43076700/1719925731564-51dd461f-6546-40e1-aef5-cc00c29fb32d.png#averageHue=%23282f35&clientId=u0c009d04-de1b-4&from=paste&height=48&id=ud09127ca&originHeight=48&originWidth=246&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3328&status=done&style=none&taskId=u4f964cb4-0a8a-45fe-a5ca-28e9a4e5cb3&title=&width=246)
输入ssh连接命令：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/43076700/1719925744839-d4d1594c-8a52-4063-8d82-cfda00fd79ba.png#averageHue=%232f363d&clientId=u0c009d04-de1b-4&from=paste&height=97&id=u3a339893&originHeight=97&originWidth=613&originalType=binary&ratio=1&rotation=0&showTitle=false&size=7818&status=done&style=none&taskId=u6976d1ea-efaf-4768-a97e-cc6ebea3797&title=&width=613)
现在假设已经添加好了，点击刷新，左边就可以进行连接了。
这里用挂在校园网上的服务器举例：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/43076700/1719925796677-203bef53-7b76-4044-9783-14ba887fdd8b.png#averageHue=%232c3237&clientId=u0c009d04-de1b-4&from=paste&height=59&id=u24eb3380&originHeight=59&originWidth=271&originalType=binary&ratio=1&rotation=0&showTitle=false&size=4920&status=done&style=none&taskId=u9047495b-2cfb-456e-b796-e9d40f52f74&title=&width=271)
点击箭头，顶端搜索栏中会要求输入密码，输入正确后即可连接。
此时点击左边的资源管理器，画面如下：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/43076700/1719925856335-809ad7af-34f3-4abb-84e7-2cf40c5615ec.png#averageHue=%23252d33&clientId=u0c009d04-de1b-4&from=paste&height=219&id=u8c025546&originHeight=219&originWidth=237&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10188&status=done&style=none&taskId=u2491b072-0d78-45db-abb2-ea0e470d880&title=&width=237)
点击打开文件夹，就可以进入服务器中的文件夹了。
在你有权限的文件夹中，你可以进行文件的增删改等操作，请根据服务器不同位置的具体权限自行使用。


## 三、Git
首先请确保你的电脑已经安装了Git！
Git的安装网址如下：
[https://git-scm.com/book/zh/v2/%E8%B5%B7%E6%AD%A5-%E5%AE%89%E8%A3%85-Git](https://git-scm.com/book/zh/v2/%E8%B5%B7%E6%AD%A5-%E5%AE%89%E8%A3%85-Git)
如果你是MacOS系统，可以使用brew进行安装。
首次使用需要在命令行对个人信息进行初始化：

```
git config --global user.name 你的用户名
git config --global user.email 你的邮箱
git config --global credential.helper cache
```
这里的邮箱需要与你注册github的邮箱对应。为了方便，用户名和邮箱都使用Github的注册信息即可。


### 命令行操作
如果你要把Github上的项目克隆到本地，分两种情况，操作都大同小异。
在后文，项目统一用repo代替，与github的repositories对应。

#### 一、repo是你自己创建的/你参与协作且拥有访问权限
进入自己的repo，点击绿色的Code按钮，会找到一个https网址，把它复制下来。用这行代码克隆到你初始化的仓库，url即复制的网址。访问Github可以使用科学上网。

```git clone 复制的url```
命令行会反馈是否成功，如果不成功可能是网络问题。

#### 二、repo是别人的，你想搬运来用
点击Fork按钮，将项目fork到你自己的repo中，随后在自己的repo中查看url并使用相同的命令。网址后的ID是你自己的才是正确的。
举例：![image.png](https://cdn.nlark.com/yuque/0/2024/png/43076700/1716475568434-0fcba53d-4e2e-48f4-83a0-7989a3ef9acd.png#averageHue=%23d5d8d9&clientId=ub1b7a934-b487-4&from=paste&height=41&id=u93b3b16b&originHeight=82&originWidth=682&originalType=binary&ratio=2&rotation=0&showTitle=false&size=14834&status=done&style=none&taskId=u5ca81032-fbc7-4780-81a8-e40c54f6bb4&title=&width=341)
现在，你可以在本地对这个项目进行操作。
这里需要注意项目的法律条款协议。
当操作完成后，需要将项目推送到GitHub时
命令行进入工作文件夹。

```
git add .
```
将文件夹中的所有文件添加到工作区

```
git status
```

查看当前工作区状态，可以查看经过修改的文件
```
git commit -m "your message"
```

将修改好的内容提交到工作区，your message部分是你的提交信息，日志会更新在这里![image.png](https://cdn.nlark.com/yuque/0/2024/png/43076700/1716475753120-747bb456-425c-4c5f-a8ac-e3115b07adbd.png#averageHue=%23fef8f7&clientId=ub1b7a934-b487-4&from=paste&height=45&id=u38d828e6&originHeight=90&originWidth=1790&originalType=binary&ratio=2&rotation=0&showTitle=false&size=26386&status=done&style=none&taskId=u904fbf6f-4a05-4b8d-a87b-4b4af143263&title=&width=895)
```
git push
```

将代码推送到GitHub，如果失败是网络问题
如果你要将你修改的代码提交到别人的repo中，第一次，要用到
```
git push--set-upstream origin
```

推送远程仓库，第一次可能需要登录
如果GitHub的仓库更新了，比如和别人共同协作一个repo，他提交了代码，你要同步
```
git pull
```
拉取最新的代码
如果在repo中有不同的分支
```git branch 分支名```
创建本地分支

```
git checkout -a
```

查看本地的所有分支
```
git checkout 分支名
```

切换到某分支
```
git branch - D 分支名
```

删除本地分支

```
git remote add origin url
```

将本地分支同步到远程分支

### VSCode中源代码管理

![image.png](https://cdn.nlark.com/yuque/0/2024/png/43076700/1719925375990-e0bed7f5-c33c-4b5c-9fe3-5fb4400596a3.png#averageHue=%23272d33&clientId=ud3b6b92c-252e-4&from=paste&height=240&id=a759u&originHeight=240&originWidth=45&originalType=binary&ratio=1&rotation=0&showTitle=false&size=3227&status=done&style=none&taskId=u7e767b32-88d4-4737-ad17-608f5120cbd&title=&width=45)
页面的左侧工具栏自上往下第三个是源代码管理，在这里可以对你代码的修改提交进行管理。
例如我对我的代码进行了修改，在源代码管理处就能看到我进行的修改。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/43076700/1719926119935-50dfbdf6-13e6-4aca-a877-c9b033e14773.png#averageHue=%23293138&clientId=u0c009d04-de1b-4&from=paste&height=243&id=WF74e&originHeight=243&originWidth=237&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15871&status=done&style=none&taskId=uba9a29c1-81d2-42a0-b45b-9fa5fac7e3d&title=&width=237)
点击修改文件右边的加号，把修改提交到暂存区。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/43076700/1719926140200-b830f9e8-5f94-4025-ba30-b836a1f206c1.png#averageHue=%23293036&clientId=u0c009d04-de1b-4&from=paste&height=229&id=pIyz1&originHeight=229&originWidth=237&originalType=binary&ratio=1&rotation=0&showTitle=false&size=15496&status=done&style=none&taskId=u4d894b74-8141-447a-9cf4-9ddd230d059&title=&width=237)
在将所有需要提交的文件提交到暂存区后，请输入修改信息，例如：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/43076700/1719926188744-c5d00cfa-d873-4764-b744-5cf3a6fa971b.png#averageHue=%23263039&clientId=u0c009d04-de1b-4&from=paste&height=120&id=cvMsX&originHeight=120&originWidth=218&originalType=binary&ratio=1&rotation=0&showTitle=false&size=5560&status=done&style=none&taskId=uaeb577c6-bb26-43b9-88a6-c8ee8868e29&title=&width=218)
这里的修改信息请遵守规范。
编辑好信息后确认无误，请点击提交。
![image.png](https://cdn.nlark.com/yuque/0/2024/png/43076700/1719926225878-19644134-dab2-4795-9bd4-9bdf074e021b.png#averageHue=%23262d32&clientId=u0c009d04-de1b-4&from=paste&height=168&id=Zlkpk&originHeight=168&originWidth=237&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10373&status=done&style=none&taskId=u100bda21-bd81-46a3-8495-f3789f08181&title=&width=237)
点击同步更改，即可将提交的更改进行推送。
界面的最上面，会有这个图标，请善用：
![image.png](https://cdn.nlark.com/yuque/0/2024/png/43076700/1719926277458-ca69a5af-106e-47c1-a5f6-8893725daf59.png#averageHue=%23252b31&clientId=u0c009d04-de1b-4&from=paste&height=33&id=OwqQI&originHeight=33&originWidth=235&originalType=binary&ratio=1&rotation=0&showTitle=false&size=2882&status=done&style=none&taskId=u72a4287d-4938-44bb-ada8-96834db09f2&title=&width=235)
![image.png](https://cdn.nlark.com/yuque/0/2024/png/43076700/1719926284537-27be0214-382d-4300-b35f-97ee735f6f21.png#averageHue=%23343b42&clientId=u0c009d04-de1b-4&from=paste&height=367&id=ETeIS&originHeight=367&originWidth=200&originalType=binary&ratio=1&rotation=0&showTitle=false&size=10087&status=done&style=none&taskId=ud66b78cf-69e9-4c50-84d4-e8993128eab&title=&width=200)
这里简单进行一下解释，可以参考上文的命令行操作进行比对。
拉取（pull）：如果你的代码版本和main分支下的代码不同，或者是有新的更新要从代码仓库拉取，请使用**拉取**
推送（push）：在提交了更改后，使用**推送**将代码推送到所在的分支
克隆（clone）：从URL**克隆**整个代码仓库到本地
签出到（branch）：**切换**分支
抓取（fetch）：与pull不同之处在于，fetch会下载远程分支的所有更新，但不会自动合并到本地分支

### 代码提交操作步骤

1. 将仓库克隆到本地目录
2. 切换到正确的分支，对代码进行修改
3. 将所有要提交的修改添加到暂存区
4. 确认无误后，提交修改，编辑符合规范的提交信息
5. 将已提交的修改推送到远程仓库。如果分支需要合并，请在GitHub提交合并请求，由项目负责人检查代码后进行操作。如果推送到自己的分支，自己进行确认即可。
