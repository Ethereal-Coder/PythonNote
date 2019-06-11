# !/usr/bin/env python
# encoding: utf-8  
"""
Created by sunyh-vm on 19-4-23
Description:
"""

from matplotlib import font_manager
from matplotlib import pyplot as plt

my_font = font_manager.FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSerifCJK-SemiBold.ttc')

a = ["猩球崛起3：终极之战", "敦刻尔克", "蜘蛛侠：英雄归来", "战狼2"]
b_16 = [15746, 312, 4497, 319]
b_15 = [12357, 156, 2045, 168]
b_14 = [2358, 399, 2358, 362]

bar_width = 0.2

x_14 = list(range(len(a)))
x_15 = [i + bar_width for i in x_14]
x_16 = [i + bar_width * 2 for i in x_14]

plt.figure(figsize=(20, 8), dpi=80)

plt.bar(x_14, b_14, width=bar_width, label='14')
plt.bar(x_15, b_15, width=bar_width, label='15')
plt.bar(x_16, b_16, width=bar_width, label='16')

plt.xticks(x_15, a, fontproperties=my_font)

plt.legend(prop=my_font)

plt.show()
