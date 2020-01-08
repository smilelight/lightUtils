# lightUtils
本项目仅为自己的Python常用工具类。

其中有些是自己写的，有的则是网上找的，由于有些还需要copy代码到相应需求处才能使用，比如说放在gist或其他代码片段保存工具并不太方便，所以这里也构建一个库，用的时候先`install`然后直接`import`就好了。

## 功能

1. 彩色日志
2. 获取系统可用tcp端口

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

## 参考
1. [lightless233/colorlog: Python彩色log模块封装](https://github.com/lightless233/colorlog)
2. [Getting a random free tcp port in python using sockets](https://gist.github.com/gabrielfalcao/20e567e188f588b65ba2)