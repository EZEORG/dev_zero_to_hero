
Scrapy + Celery + Multiprocessing
=================================


.. article-info::
    :avatar: https://avatars.githubusercontent.com/u/154419224
    :avatar-link: https://github.com/eze-root
    :avatar-outline: muted
    :author: `@eze-root <https://github.com/eze-root>`_
    :date: 2024-11-27 
    :read-time: 25 min read
    :class-container: sd-p-2 sd-outline-muted sd-rounded-1




Backgrounds
-----------

首先说明一下本博文需要解决问题，要使用scrapy + celery 来实现定期对多个爬虫的运行问题。

当然，上述的运行，通过 \ `django-celery-beat <https://github.com/celery/django-celery-beat>`_ 和 \ `django-celery-results <https://django-celery-results.readthedocs.io/en/latest/>`_ 可以用 django的web页面进行管理，比较方便。

假设现在有spider1, spider2 两个爬虫，可以通过 

.. code-block:: bash

  scrapy crawl spider1
  scrapy crawl spider2

实现调用，并且成功运行，接下来需要解决的问题是将上述的调用嵌入celery中。

需要完成函数

.. code-block:: python

  
  @shared_task
  def run_my_spider(*args, **kwargs):
      name = kwargs['spider_name']

      # Here, we need to implement calling a process for crawling



Scrapy Run Spider
-----------------

关于 \ :literal:`Scrapy`\, 启动一个爬虫的方式通常包括:

1. 使用命令行 \ :code:`scrapy crawl xxx`\, 其中 \ :code:`xxx`\ 是爬虫的名字。
2. 使用 \ :code:`CrawlerProcess`\ 或者 \ :code:`CrawlerRunner`\, 详细的代码请查看 [Common-Practices-in-Scrapy]_ 


特别的，如果想要更多的了解 \ `CrawlerRunner <https://docs.scrapy.org/en/latest/topics/api.html#scrapy.crawler.CrawlerRunner>`_ \ 和 `CrawlerProcess <https://docs.scrapy.org/en/2.11/topics/api.html#scrapy.crawler.CrawlerProcess>`_ , 请阅读 \ `CoreAPI <https://docs.scrapy.org/en/latest/topics/api.html>`_ ，值得一提的是，正如文档说的, \ :emphasis:`Scrapy is built on top of the Twisted asynchronous networking library, so you need to run it inside the Twisted reactor`\。 这意味着在进行多个爬虫的并发过程中，可能出现各种关于 \ :code:`ReactorNotRestartable`\ 、 \ :code:`ReactorAlreadyInstalledError`\ 等问题。

网上有许多的讨论关于最终使用什么样的方案来处理, 有的帖子提到最好在一个线程里面用单个的reactor来进行，有的认为使用多进程处理。
虽然官方也给出了日常中的 [Common-Practices-in-Scrapy]_ 来给出解决方案，例如 \ `Running multiple spiders in the same proces <https://docs.scrapy.org/en/2.11/topics/practices.html#running-multiple-spiders-in-the-same-process>`_ 。
但是当在Scrapy引入 Celery后，这个方案失效。


此外，在Celery中使用多进程仍然可能出现问题, \ `daemonic processes are not allowed to have children <https://github.com/celery/celery/issues/4525>`_ 。
其中，有开发者提到，`The default pool option of Celery is "prefork", which doesn't support multiprocessing`。因此在这一方面处理需要更多的注意, 需要将Celery切换到 `thread` 。所以本次博文想要描述一下问题和解决过程。



Celery
------

使用Django配合Celery，配合 \ :code:`django-celery-beat`\ 和 \ :code:`django-celery-results`\, 可以很好的实现爬虫任务的周期运行。

具体的配置包括:



.. tab-set::

  .. tab-item:: Python Install
  
    .. code-block:: bash
    
      pip install redis django-celery-beat django-celery-results

  .. tab-item:: docker-compose.yml

    .. code-block:: docker-compose.yml

      services:
        redis:
            image: redis:alpine
            restart: always
      
        web:
          build: 
            context: .
            dockerfile: Dockerfile
          image: xxx_system
          command: python3 run_aiohttp.py 
          volumes:
            - ./:/code
            - ./logs:/logs
          working_dir: /code
          tty: true
        
        celery_worker:
          image: xxx_system
          command: 'celery -A xxx_system worker -l info'
          volumes:
            - ./:/code
            - ./logs:/logs
          working_dir: /code
          depends_on:
            - redis
            - web
      
        celery_beat:
          image: xxx_system
          command: 'celery -A xxx_system beat -l info'
          volumes:
            - ./:/code
            - ./logs:/logs
          working_dir: /code
          depends_on:
            - redis
            - web
    
  .. tab-item:: celery.py

    .. code-block:: bash
    
      import os
      
      from celery import Celery
      
      # set the default Django settings module for the 'celery' program.
      os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xxx_system.settings")
      
      app = Celery("xxx_system")
      
      # Using a string here means the worker doesn't have to serialize
      # the configuration object to child processes.
      # - namespace='CELERY' means all celery-related configuration keys
      #   should have a `CELERY_` prefix.
      app.config_from_object("django.conf:settings", namespace="CELERY")
      
      # Load task modules from all registered Django app configs.
      app.autodiscover_tasks()
    
    

然后编写 \ :code:`tasks.py`\ 即可得到 celery 的运行函数，但是如果同时运行多个爬虫，很容易报错。

相关的解决方案使用 crochet 参考资料如下：

+ \ `解决django或者其他线程中调用scrapy报ReactorNotRestartable的错误 <https://www.cnblogs.com/WalkOnMars/p/11934535.html>`_
+ \ `Django Celery Scrappy ERROR: twisted.internet.error.ReactorNotRestartable <https://stackoverflow.com/questions/50140887/django-celery-scrappy-error-twisted-internet-error-reactornotrestartable>`_

这里提到的核心solutions是:

1. pip install crochet
2. import from crochet import setup
3. setup() - at the top of the file
4. remove 2 lines:
 d.addBoth(lambda _: reactor.stop())

 reactor.run()

原理是：因为CrawlerProcess自带reactor的启动关闭过程，而这个过程是在其他线程中发生的，

所以重复运行会报 :code:`ReactorNotRestartable、ReactorNotRestartable、ReactorNotRunning` 等一系列问题。使用 `crochet` 可以嵌套使用 `twisted` 线程。

但是这个方案，需要配合将celery变为基于 `threads`, 即

.. code-block:: python
   
   celery -A xxx_system worker -P threads -l info


另外一个方法也是一些资料提到的使用多进程的方式。在尝试了多个操作后，目前得到了相对较有的方案。记录自己的尝试如下：


Celery + Multiprocessing
------------------------

1. 使用 `multiprocessing`
*************************

.. code-block:: python

   from multiprocessing import Process

   def run_spider_process(name):
       settings = get_project_settings()
       process = CrawlerProcess(settings)
       crawler = process.create_crawler(name)
       process.crawl(crawler)
       process.start()
       stats_dict = crawler.stats.get_stats()
       return stats_dict
   
   @shared_task
   def run_my_spider(*args, **kwargs):
       name = kwargs['spider_name']
       process = Process(target=run_spider_process, args=(name, ))
       process.start()
       process.join()


但是这个还是会报错，`twisted.internet.error.ReactorAlreadyRunning`。
询问了ChatGPT, 结论是：

  您遇到的 twisted.internet.error.ReactorAlreadyRunning 错误是由于 Twisted 的 Reactor 已经在主进程中运行，而在子进程中尝试再次启动它导致的。Twisted 的 Reactor 设计为每个进程中只能有一个实例运行，因此在使用 multiprocessing 时需要特别注意。
  确保将 multiprocessing.set_start_method('spawn') 放在 if __name__ == '__main__': 块内，以避免在子进程中重复设置启动方式。

然后文章提到多个解决方案，特别是使用multiprocessing的情况下，需要修改默认的启动方式：

  默认情况下，multiprocessing 在某些操作系统（如 Unix）上使用 'fork' 启动方式，这会导致子进程继承父进程的资源，包括 Reactor 的状态。通过将启动方式更改为 'spawn'，可以确保子进程从一个全新的状态开始，不会继承 Reactor 的状态。

关于 `spawn` 和 `fork` 的详细说明，请查看 \ `contexts-and-start-methods <https://docs.python.org/3/library/multiprocessing.html#contexts-and-start-methods>`_ 这里面的文档涉及到很多操作系统的知识。



2. 使用 `billiard` 
******************

根据 \ `billiard <https://github.com/celery/billiard>`_ 的文档说明，其使用一个fork版本的多进程进行的开发。(billiard is a fork of the Python 2.7 multiprocessing package. The multiprocessing package itself is a renamed and updated version of R Oudkerk's pyprocessing package)

因此尝试将上述的multiprocessing修改为billiard, 出现了新的报错 `daemonic processes are not allowed to have children`

.. code-block:: python

  ...
  from billiard import Process

更多的魔改方法参见， \ `Run a Scrapy spider in a Celery Task <https://stackoverflow.com/questions/22116493/run-a-scrapy-spider-in-a-celery-task/22202877#22202877>`_ ，包括 use \ `Crawler <https://docs.scrapy.org/en/2.11/topics/api.html#scrapy.crawler.Crawler>`_ instead `CrawlerProcess`_ 。


3. 使用 `subprocess`
********************

使用subprocess是比较简单的方式，

.. code-block:: python

  def run_spider_subprocess(name):
      subprocess.run(f'scrapy crawl {name}', shell=True)

这个代码本身可以正常运行，但是问题就是不能返回结果，不是很好的能捕获输出的stats_dict 到 `django-celery-results`_ 中。


4. 使用 `spawn`
***************

在前文提到的报错的情况下，ChatGPT建议将启动方式改为 `spawn` 。
需要在 `__main__` 位置进行，显然是不适合这个场景的。



5. 使用 `ProcessExecutor`
*************************

最终，在进行多次分析后，得到了使用 \ `ProcessExecutor <https://docs.python.org/3/library/concurrent.futures.html#processpoolexecutor>`_ 的建议，并且同样需要设置启动方式为 `spawn` 

.. code-block:: python

    mp_context = multiprocessing.get_context('spawn')
    with ProcessPoolExecutor(max_workers=1, mp_context=mp_context) as excutor:
        future = excutor.submit(run_spider_process, 'xxx')
        return future.result()


这部分的代码便能很好的完成本文的需求。



总结
----

在本文中，我们尝试了很多的方案实现 Celery + Django + Scrapy ， 并且爬虫需要定期多个同时并发执行。
最终的解决solution是使用 `ProcessExecutor`_ , 配合使用 `spawn` 实现的。



.. [Common-Practices-in-Scrapy] \ `Common Practices in Scrapy <https://docs.scrapy.org/en/latest/topics/practices.html>`_
