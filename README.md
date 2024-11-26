# Develop from Zero to Hero Tutorial by EZELAB

See the [website](https://EZEORG.github.io/dev_zero_to_hero/)


## How to contribute

First, you need to learn how to write article with [Markdown](https://docs.github.com/zh/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github) or [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) (Markdown is necessary).

After that, you (e.g., WinstonCHEN1) can checkout a new branch using:

```
git checkout -b WinstonCHEN1-add-xxx
```
where, `xxx` is the content of your writing

Then, write a new `xxx.md` in `source/draft` directory.

You should include article infomation for your authorship.

Please check the your profile link and avatar.

````markdown
```{article-info}
:avatar: https://avatars.githubusercontent.com/u/163944337 
:avatar-link: https://github.com/WinstonCHEN1/
:avatar-outline: muted
:author: [@WinstonCHEN1](https://github.com/WinstonCHEN1/)
:date: |today|
:read-time: "{sub-ref}`wordcount-minutes` min read"
:class-container: sd-p-2 sd-outline-muted sd-rounded-1
```
````

See [Development](https://github.com/EZEORG/dev_zero_to_hero?tab=readme-ov-file#development), you will learn how to preview it in your local machine.

After finishing your writing, please push into your branch, and @WinstonCHEN1 or @eze-root will try to merge your branch into main and deploy into our pages.



## Development


### Install

```python
virtualenv venv
source venv/bin/activate
pip install -r requirements-dev.txt
```

### Develop in localhost

```bash
bash run_dev.sh
```

Open [http://localhost:11111/darfts/xxx.html](http://localhost:11111/darfts/xxx.html), you will have your writing



