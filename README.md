# lightUtils
本项目仅为自己的Python常用工具类。

其中有些是自己写的，有的则是网上找的，由于有些还需要copy代码到相应需求处才能使用，比如说放在gist或其他代码片段保存工具并不太方便，所以这里也构建一个库，用的时候先`install`然后直接`import`就好了。

## 功能

1. 彩色日志
2. 获取系统可用tcp端口
3. 从文件中逐行获取json对象
4. 发送邮件
5. 将时间间隔（s为单位）转换为日时分秒表示
6. 将迭代器转化为批量数据返回形式

## 使用

### 1.彩色日志

#### 示例
```python
from lightutils import logger

logger.info("info")
logger.warning('warning')
logger.debug('debug')
logger.error('error')
```

效果如图：
![效果](res/log-demo.jpg)

### 2.获取系统可用tcp端口

#### 示例
```python
from lightutils import get_free_tcp_port

port = get_free_tcp_port()
print(port)
```

执行结果为：
```bash
49783
<class 'int'>
```

### 3.从文件中逐行获取json对象

从文件中逐行获取json对象，

#### 示例

```python
from lightutils import read_json_line

for obj in read_json_line('test.json'):
    print(obj)
```

执行结果为：
```bash
{'info': {'word': '丘为', 'means': [['寻西山隐者不遇', '寻西山隐者不遇'], ['左掖梨花', '左掖梨花']]}, 'type': 'ambiguous'}
{'info': {'word': '丘为', 'means': [['寻西山隐者不遇', '寻西山隐者不遇'], ['左掖梨花', '左掖梨花']]}, 'type': 'ambiguous'}
```

原文件内容为：
```json
{"info": {"word": "丘为", "means": [["寻西山隐者不遇", "寻西山隐者不遇"], ["左掖梨花", "左掖梨花"]]}, "type": "ambiguous"}
{asdf}
{"info": {"word": "丘为", "means": [["寻西山隐者不遇", "寻西山隐者不遇"], ["左掖梨花", "左掖梨花"]]}, "type": "ambiguous"}
```

错误输出日志`error.log`内容如下：
```text
line2: {asdf}

```

### 4.发送邮件

使用Python发送一封邮件

#### 示例

```python
from lightutils import send_email_notification

to = "iamlightsmile@qq.com"
subject = "just a test"
contents = ["the test of lightUtils's send_email_notification function"]
result = send_email_notification(to, subject, contents)
if result:
    print("发送成功！")
else:
    print("发送失败！")
```

#### 运行结果：

```text
发送成功！
```

#### 效果截图：

![UTOOLS1580802152439.png](https://lightsmile-img.oss-cn-beijing.aliyuncs.com/UTOOLS1580802152439.png)

### 5.将时间间隔（s为单位）转换为日时分秒表示

#### 使用示例

```python
from lightutils import time_convert

print(time_convert(10000000.234))
print(time_convert(1000000.0))
print(time_convert(100000.0))
print(time_convert(10000.0))
print(time_convert(1000.0))
print(time_convert(100.0))
print(time_convert(10.0))
print(time_convert(1.0))
print(time_convert(0.0))
```

#### 运行结果：

```text
115天17小时46分钟40.23秒
11天13小时46分钟40.0秒
1天3小时46分钟40.0秒
2小时46分钟40.0秒
16分钟40.0秒
1分钟40.0秒
10.0秒
1.0秒
0.0秒
```

### 6.将迭代器转化为批量数据返回形式

#### 使用示例

```python
from lightutils import batch

if __name__ == '__main__':
    for item in batch(range(100)):
        print(item)
```

#### 运行结果：

```text
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
[20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
[30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
[40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
[50, 51, 52, 53, 54, 55, 56, 57, 58, 59]
[60, 61, 62, 63, 64, 65, 66, 67, 68, 69]
[70, 71, 72, 73, 74, 75, 76, 77, 78, 79]
[80, 81, 82, 83, 84, 85, 86, 87, 88, 89]
[90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
```


## 参考
1. [lightless233/colorlog: Python彩色log模块封装](https://github.com/lightless233/colorlog)
2. [Getting a random free tcp port in python using sockets](https://gist.github.com/gabrielfalcao/20e567e188f588b65ba2)
3. [kootenpv/yagmail: Send email in Python conveniently for gmail using yagmail](https://github.com/kootenpv/yagmail)
4. [Python最良心的邮件发送库--yagmail_Detector_的博客-CSDN博客](https://blog.csdn.net/Detector_/article/details/79673875)
5. [Python用QQ邮箱发送邮件时授权码问题_wateryouyo的博客-CSDN博客](https://blog.csdn.net/wateryouyo/article/details/51766345)
6. [python - how to split an iterable in constant-size chunks - Stack Overflow](https://stackoverflow.com/questions/8290397/how-to-split-an-iterable-in-constant-size-chunks)

## 打赏

如果该项目对您有所帮助，欢迎打赏~

![UTOOLS1578660899400.jpg](https://lightsmile-img.oss-cn-beijing.aliyuncs.com/UTOOLS1578660899400.jpg)
