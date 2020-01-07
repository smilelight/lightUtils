# lightUtils
本项目仅为自己的Python常用工具类。

## 功能

### 1.彩色日志

**声明**：本功能纯粹搬自[lightless233/colorlog: Python彩色log模块封装](https://github.com/lightless233/colorlog)，因为在使用时还要复制脚本到项目有些麻烦，所以这里直接集成进去，在使用时安装`lightUitls`这个库然后再引用就可以了。

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

## 参考
1. [lightless233/colorlog: Python彩色log模块封装](https://github.com/lightless233/colorlog)