import jieba
import wordcloud
from scipy.misc import imread

mask = imread("hu.jpg")
excludes = {}
f = open("文本.txt", "r", encoding="gbk")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(
    width=800, height=600,
    background_color="white",
    font_path="msyh.ttc", mask=mask)
w.generate(txt)
w.to_file("hy.png")
