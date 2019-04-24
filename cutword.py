# -*- coding: utf-8 -*-
# @Time : 2019/1/2 7:52 PM
# @Author : cxa
# @File : cutword.py
# @Software: PyCharm
# coding=utf-8
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 获取所有评论
comments = []
with open('msg.txt', mode='r', encoding='utf-8') as f:
    rows = f.readlines()
    for row in rows:
        comments.append(row)


# 设置分词
comment_after_split = jieba.cut(str(comments), cut_all=False)  #分词，cut_all=false
words = ' '.join(comment_after_split)  # 以空格进行拼接

# 设置屏蔽词
STOPWORDS = set(map(str.strip, open('stopwords').readlines()))
print(STOPWORDS)
# 导入背景图
bg_image = plt.imread('1.jpg')
# 设置词云参数，参数分别表示：画布宽高、背景颜色、背景图形状、字体,屏蔽词、最大词的字体大小
wc = WordCloud(background_color='white', mask=bg_image,font_path='msyhbd.ttf',stopwords=STOPWORDS, max_font_size=400,
               random_state=200)

# 将分词后数据传入云图
wc.generate_from_text(words)
plt.imshow(wc)
plt.axis('off')  # 不显示坐标轴
plt.show()

# 保存结果到本地
wc.to_file('ggcfcmd.jpg')
