# Day 4 SSH与Django

## Windows系统下的ssh密钥

为了避免每次登录服务器都需要输密码的这个麻烦的问题，可以使用以下方法解决。

如果你的系统是mac，那么这个问题将会变的很简单，使用命令


```
ssh-copy-id userid@服务器地址
```

如果你的系统是Windows，那么先在Powershell里面输入

```
ssh-keygen
```

然后一路回车，直到看到生成了一些“奇怪的图形”，命令行也可以再次输入了。这时候输入

```
type $env:USERPROFILE\.ssh\id_rsa.pub | ssh xxx@spider1.utlab.ltd "cat >> ~/.ssh/authorized_keys"
```

将这里的xxx换成你的名字，如果你的服务器地址不一样，自行更改即可。

从现在开始，你再登录你的服务器，就不需要输密码了。

## Django

首先进入服务器之后，先安装Django

```
pip install django
```

安装好之后，使用命令创建一个项目

```
django-admin startproject 项目名
```

然后简单介绍一下项目的框架，以下的项目名都是mysite：
- 最外层的 **mysite/** 根目录只是你项目的容器， 根目录名称对 Django 没有影响，你可以将它重命名为任何你喜欢的名称。
- **manage.py**: 一个让你用各种方式管理 Django 项目的命令行工具。
- 里面一层的 **mysite/** 目录包含你的项目，它是一个纯 Python 包。它的名字就是当你引用它内部任何东西时需要用到的 Python 包名。 (比如 mysite.urls).
- **mysite/__init__.py**：一个空文件，告诉 Python 这个目录应该被认为是一个 Python 包。
- **mysite/settings.py**：Django 项目的配置文件。
- **mysite/urls.py**：Django 项目的 URL 声明，就像你网站的“目录”。
- **mysite/asgi.py**：作为你的项目的运行在 ASGI 兼容的 Web 服务器上的入口。
- **mysite/wsgi.py**：作为你的项目的运行在 WSGI 兼容的Web服务器上的入口。

现在可以用

```
python manage.py runserver 0:30009
```

运行你的项目，我这里的示例端口是30009，**请选择不要冲突的端口**。

于是这里可以进入`http://0.0.0.0:30009`查看你的网页，但是应该会出现一个不太友好的界面。

![](https://files.mdnice.com/user/58281/56ac833b-e8b4-4a7e-95d2-56c1679798a7.png)

需要修改项目文件里的**settings.py**，将`ALLOWED_HOSTS = []`修改为`ALLOWED_HOSTS = ["*"]`

再次进入你的端口

![](https://files.mdnice.com/user/58281/fd4f5efb-285a-46d5-932f-1b3a08a16933.png)

出现了一个小火箭，说明运行成功了。

```
python manage.py startapp polls
```

现在我们创建了一个名为polls的投票项目，项目的文件夹下面多出了一个名为polls的文件夹。

![](https://files.mdnice.com/user/58281/2e6a7682-8440-4f4b-a25c-29c3cc36b899.png)

打开polls目录下的views.py文件，添加这段代码

```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

```

![](https://files.mdnice.com/user/58281/d066fcce-7afb-4aa2-97bb-0846b299cf59.png)

这是编写的第一个视图，要将第一个URL映射到它。对应的index是路径下需要渲染的https，第一个需要修改应用的url。

然后，在这个目录下创建一个urls.py文件，添加以下内容

```
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

![](https://files.mdnice.com/user/58281/b9e06d75-e4e1-483d-8c83-c7e9f3dca06e.png)

捕获了url为空，调用views.index函数，上面编写的。

然后在 mysite/urls.py 文件的 urlpatterns 列表里插入一个 include()，或者直接替换里面所有的内容为以下内容

```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```

但第一个url不够，需要在大的项目上定义。这一步把刚才的全部抓到大项目的主要部分。
![](https://files.mdnice.com/user/58281/3d1cf009-fa58-4c84-b3c3-94de12456eeb.png)

这里我连接的服务器是spider1.utlab.ltd，在30009端口上开启，所以这里我在浏览器打开`http://spider1.utlab.ltd:30009/polls/`

![](https://files.mdnice.com/user/58281/bd4b3197-68b5-45f7-b7ea-037ffdce6791.png)

成功出现了hello world。

### 数据库

Django默认的数据库是SQLite。项目的根目录下已经有了这个文件

![](https://files.mdnice.com/user/58281/977638b7-4bf8-428b-9e66-393f860ca95a.png)

目前先不考虑使用别的数据库，因为需要添加一些额外的设置。先不管时区，如果以后需要上线再进行修改。

使用

```
python manage.py migrate
```

启用数据库

![](https://files.mdnice.com/user/58281/d60ee21d-fe40-4a72-bb2a-a2986047dcc8.png)

使用这个命令

```
sqlite3 db.sqlite3
```

就可以进入数据库，使用一些SQL语句了。

编辑模型polls/models.py

```
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```
    
编辑 polls/apps.py 中

```
INSTALLED_APPS = [
    "polls.apps.PollsConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

添加了`"polls.apps.PollsConfig",`这一行

运行以下的这两行代码迁移并同步管理你的数据库结构：

```
python manage.py sqlmigrate polls 0001

python manage.py migrate 
```

### 管理员账号

```
python manage.py createsuperuser

Username: admin

Email address: admin@example.com
```

然后输入密码，如果你的密码过于简单会被警告，这里如果不想管他，输入y即可。接下来，你已经成为了网站管理员了！

这里启动开发服务器的前提下，转到本地的目录，还是以我的url为例

`http://spider1.utlab.ltd:30009/admin/`

![](https://files.mdnice.com/user/58281/656822cf-3a14-4539-9655-1c4534d32c3a.png)

现在来到了一个登录页面，输入账号密码之后即可登录。

![](https://files.mdnice.com/user/58281/18ccd2cb-a65f-46cc-aa25-a43cfce960e2.png)

打开 polls/admin.py 文件，把它编辑成下面这样


```
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```

现在在网站的管理界面上已经有了POLLS里面的Questions类，可以使用了。

接下来按照教程，开始创建接口

向 polls/views.py 里添加更多视图

```
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```
把这些新视图添加进 polls.urls 模块里

```
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```
修改polls/views.py

```
from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


# Leave the rest of the views (detail, results, vote) unchanged
```

现在，在polls 目录里创建一个 templates 目录。在你刚刚创建的 templates 目录里，再创建一个目录 polls，然后在其中新建一个文件 index.html 。

输入以下代码

```
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```
更新一下 polls/views.py 里的 index 视图

```
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

![](https://files.mdnice.com/user/58281/65333fc4-4ec7-455a-9275-c38cb20949bd.png)

```

到这里为止，才只到了Django官方文档的很小一部分。这份文档号称编程界最顶级的文档之一（黄老师说的，别问我是不是真的），建议有时间时，每个人都可以看一看。







