# -*- coding: utf-8 -*-
# @Time : 2019/1/7 10:33 PM
# @Author : cxa
# @File : analysis.py
# @Software: PyCharm
from pyecharts import Line
from collections import Counter, Mapping
from operator import itemgetter

# 评论数时间分布
with open("ctime.txt") as fs:
    data = (i.strip() for i in fs.readlines())
d = dict(sorted(Counter(data).items(), key=itemgetter(0)))
print(d)
##print(isinstance(d,Mapping)) 属于字典
chart = Line("评论数时间分布")
chart.use_theme('dark')
chart.add('评论数时间分布', list(d.keys()), list(d.values()), is_fill=True, line_opacity=0.2,
          area_opacity=0.4, symbol=None)

chart.render('评论时间分布.html')
