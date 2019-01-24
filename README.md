# lightUtils
本项目仅为自己的Python常用工具类。

# 1 有道翻译api封装

## 1.1 说明

这里仅是一个简单的api调用测试，因为考虑到以后可能会用到这个api。

网上也有用这个api搞事情的，不过多为python2.7版本，官方Demo也是2.7的。

## 1.2 调用

对应`youdao`模块，调用方式如下：

```python
from pprint import pprint

from youdao import YDTranslater

ydt = YDTranslater()

pprint(ydt.query('good'))
```
结果：
```python
{'basic': {'explains': ['adj. 好的；优良的；愉快的；虔诚的',
                        'n. 好处；善行；慷慨的行为',
                        'adv. 好',
                        'n. (Good)人名；(英)古德；(瑞典)戈德'],
           'phonetic': 'gʊd',
           'uk-phonetic': 'gʊd',
           'uk-speech': 'http://openapi.youdao.com/ttsapi?q=good&langType=en&sign=1FB58CFFBC95233E763AC9FE0568EE9C&salt=1548329577177&voice=5&format=mp3&appKey=3573e0697ef130a9',
           'us-phonetic': 'ɡʊd',
           'us-speech': 'http://openapi.youdao.com/ttsapi?q=good&langType=en&sign=1FB58CFFBC95233E763AC9FE0568EE9C&salt=1548329577177&voice=6&format=mp3&appKey=3573e0697ef130a9',
           'wfs': [{'wf': {'name': '比较级', 'value': 'better'}},
                   {'wf': {'name': '最高级', 'value': 'best'}}]},
 'dict': {'url': 'yddict://m.youdao.com/dict?le=eng&q=good'},
 'errorCode': '0',
 'l': 'EN2zh-CHS',
 'query': 'good',
 'speakUrl': 'http://openapi.youdao.com/ttsapi?q=good&langType=en&sign=1FB58CFFBC95233E763AC9FE0568EE9C&salt=1548329577177&voice=4&format=mp3&appKey=3573e0697ef130a9',
 'tSpeakUrl': 'http://openapi.youdao.com/ttsapi?q=%E5%A5%BD&langType=zh-CHS&sign=520ABE140C59B71BD43360B07E9D4B2C&salt=1548329577177&voice=4&format=mp3&appKey=3573e0697ef130a9',
 'translation': ['好'],
 'web': [{'key': 'good', 'value': ['好的', '提供关于', '善', '良好']},
         {'key': 'Good Friday', 'value': ['耶稣受难节', '耶稣受难日', '受难节', '受难日']},
         {'key': 'Giffen Good', 'value': ['吉芬商品', '吉芬物品', '吉芬品', '季芬财']}],
 'webdict': {'url': 'http://m.youdao.com/dict?le=eng&q=good'}}
```

## 1.3 说明

欲使用此模块，还需要在youdao文件夹下新建`config.py`文件。内容格式如下：
```python
CONFIG = {
    'appKey': 'your appKey',
    'secretKey': 'your secretKey'
}
```
其中appKey和secretKey是自己在[有道智云开发平台](http://ai.youdao.com)创建应用并接入服务申请的。

## 1.4 参考
- [有道智云翻译 API 简介](https://ai.youdao.com/docs/doc-trans-api.s)


