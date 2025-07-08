import pandas as pd
from wordcloud import WordCloud
import jieba
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# 加载中文停用词表

import chardet

# Detect the encoding of the file
with open(r'D:\大学\任务活动\第六学期\统计建模大赛\ChineseStopWords.txt', 'rb') as file:
    rawdata = file.read()
    result = chardet.detect(rawdata)
    encoding = result['encoding']
    print("Detected encoding is:", encoding)

# Now read the file with the detected encoding
with open(r'D:\大学\任务活动\第六学期\统计建模大赛\ChineseStopWords.txt', 'r', 
          encoding=encoding) as file:
    stops = file.read().split('\n')


# 读取评论数据
df = pd.read_excel(r'D:\大学\任务活动\第六学期\统计建模大赛\评论罗伯特python新\数据\爬虫数据202401-202405\罗伯特的评论0101-0501.xls',
                 )
comments = ' '.join(df['评论内容'].astype(str))  # 假设CSV文件中存储评论的列名为“评论”

# 使用jieba进行中文分词
words = jieba.lcut(comments)
filtered_words = [word for word in words if word not in stops and len(word) > 1]

# 词频统计
word_freq = {}
for word in filtered_words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# 词频排序
sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

# 打印前30个最高频词
for word, freq in sorted_word_freq[:30]:
    print(word, freq)


from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 绘制词云
wordcloud = WordCloud(
    font_path='simhei.ttf',
    background_color='white',
    scale=1.5,  # 增加分辨率
    max_font_size=100,  # 最大字体大小
    width=800,
    height=600
).generate_from_frequencies(dict(sorted_word_freq))

# 画图
plt.figure(figsize=(10, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # 不显示坐标轴
plt.show()