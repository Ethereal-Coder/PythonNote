# !/usr/bin/env python
# encoding: utf-8  
"""
Created by sunyh-vm on 19-4-23
Description:
"""

from matplotlib import pyplot as plt
import random
from matplotlib import font_manager

'''
    https://matplotlib.org/gallery/index.html
'''

'''
    查看系统字体
    fc-list
    fc-list :lang=zh
'''
my_font = font_manager.FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSerifCJK-SemiBold.ttc')

x = range(2, 26, 2)
x1 = range(2, 26, 2)
y = [random.randint(-10, 10) for _ in range(12)]
y1 = [random.randint(-10, 10) for _ in range(12)]

# img size
# plt.figure(figsize=(20, 8), dpi=80)
# set x, y
plt.plot(x, y, label='first', linestyle='-.')
plt.plot(x1, y1, label='second')
# set ticks
# plt.xticks(x)
_xtick_lables = ['中文{}标签'.format(i) for i in x]
plt.xticks(x, _xtick_lables, rotation=45, fontproperties=my_font)
plt.yticks(range(min(y), max(y)+1)[::3])
# plt.grid()
plt.grid(alpha=0.1, linestyle=':')
# description
plt.xlabel('xticks desc', fontproperties=my_font)
plt.ylabel('yticks desc')
plt.title('title')

plt.legend(prop=my_font, loc='upper left')

# save pic
# plt.savefig('./t1.png')
# plt.savefig('./t1.svg')
# show pic
plt.show()
