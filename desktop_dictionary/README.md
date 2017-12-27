# DesktopDictionary
Python 桌面词典 Based on Youdao API 
仅支持 Linux
=======================

主体查询函数为query_word()

单词缓存功能的逻辑是用词典储存

每次执行query_word()时都查一遍本地是否有这个词（有没有被词典储存过）

有的话直接输出本地缓存

没有的话查完之后把词加到词典缓存里

调用有道API

============

另一重点是动作接受 就是检测选中词

用get_text() 和 get_targets()函数

"STRING" 与 "ATOM"是指数据的类型

string就是string

atom 是一个被定义在gtk里的固定的整数 标记着一个字符串 GDK_PRIMARY_SELECTION 就是一个atom 对应着/"PRIMARY/"这个字符串

ref: 
http://www.pygtk.org/pygtk2tutorial/sec-RetrievingTheSelection.html

http://aijuans1.iteye.com/blog/1536691

============

webkit 可以实现一个简单的浏览器 可以解析html字符串 由此可将有道API获取的网页内容放到创建的页面（webview）上

help from shiyanlou.com
