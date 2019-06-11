# !/usr/bin/env python
# encoding: utf-8  
"""
Created by sunyh-vm on 19-4-24
Description:
"""

import re

''' 
^s  以s开头
.   任意字符
*   重复任意次
s$  以s结尾
?   非贪婪模式（默认贪婪模式）
s+  s至少出现一次
s{2}  s出现2次
s{2，}  s出现2次以上
s{2，4}  s出现2~4次
|   或
[abcd]  取abcd中任意一个
[0-9]   取1到9任意一个
[^1]    取任意一个不为1的字符
[.*$]   中括号中的字符没有特殊含义
\s  空格
\S  任意不为空格字符
\w  等同于 [A-Za-Z0-9_]
\W  任意不为[A-Za-Z0-9_]字符
[\u4e00-\u9fa5]  中文
\d  数字

(())  多个括号由外到内取值
'''


'''
match

'''


def test1():
    line = 'he1elllllooohee2elllo'
    # regex_str = '.*(e.*e).*'
    # e2e  匹配最后的ee
    # regex_str = '.*?(e.*?e).*'
    # e1e  匹配最前的ee
    # regex_str = '.*?(e.*e).*'
    # e1elllllooohee2e
    # regex_str = '.*(e.*?e).*'
    # e2e
    # regex_str = '.*(e.+e).*'
    # e2e
    regex_str = '.*(e.+e).*'
    match_obj = re.match(regex_str, line)
    if match_obj:
        print(match_obj.group(1))


test1()