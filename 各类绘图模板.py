
# coding: utf-8

# # Python 画图模板

# # 0000绘图通用命令

# In[11]:


import matplotlib.pyplot as plt

"""  画图操作常用命令
# 以下命令可以在1.3尝试
#改图形大小
plt.figure(figsize=(10,5)) #图像大小

#调整线的颜色，点的样子，线的形状，后三个可以变
plt.plot(x, y, label="xx", color="green", marker=".", linestyle="--")

# 标注x、y轴、加图表名、加legend、加网格
plt.xlabel("年龄")
plt.ylabel("年薪")
plt.title("年龄和薪水的关系")
plt.legend()
plt.grid(True)

# 改图形样子，一般放在code 的比较开头的位置
#plt.style.use('fivethirtyeight')
#plt.style.use('ggplot')

# 画多个图
plt.figure(figsize=(10,6))
plt.subplot(2,2,1)
plt.subplot(2,2,2)
plt.subplot(2,2,3)
plt.subplot(2,2,4)
plt.show()

 画图操作常用命令 """




# # 1.1 最简单折线图

# In[4]:


import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(15,8)) #图像大小

plt.subplot(2,2,1)
x = np.linspace(-1, 1, 50)#-1是开始点1是结束点50是每个格子的长度
y = x**2
plt.plot(x, y)
plt.subplot(2,2,2)
plt.show()


# #  1.2 多条线折线图

# In[5]:


from matplotlib import pyplot as plt

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
plt.plot(ages_x, dev_y)

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(ages_x, py_dev_y)

plt.xlabel("年龄")
plt.ylabel("年薪")
plt.title("年龄和薪水的关系")

plt.legend(['全部开发者','Python开发者'])

plt.show()


# # 1.3 好看一点的折线图

# In[6]:


from matplotlib import pyplot as plt


ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
plt.style.use('fivethirtyeight')
plt.figure(figsize=(10,4)) #图像大小
plt.plot(ages_x, dev_y, label="全部开发者", color="red", marker=".", linestyle="-")

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(ages_x, py_dev_y, label="Python开发者", color="green", marker=".", linestyle="--")

plt.xlabel("年龄")
plt.ylabel("年薪")
plt.title("年龄和薪水的关系")

plt.legend()
plt.grid(True)

plt.show()


# # 2 散点图

# In[ ]:


plt.scatter(x, y, s=20) # s为散点的大小
plt.show()


# # 3 直方图

# # 3.1 简单直方图

# In[7]:


import numpy as np
import pandas as pd
from pylab import mpl
import matplotlib.pyplot as plt
series = np.array([3, 5, 7, 10, 3])
plt.bar(x=list('ABCDE'), height=series, color='tab:green', width=.5)
plt.show()
plt.barh(y=list('abcde'), width=series, height=.5)
plt.show()


# # 3.2 复杂直方图

# In[8]:


import numpy as np
import pandas as pd
from pylab import mpl
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
mpl.rcParams['font.sans-serif'] = ['SimHei']  
series = np.array([15.4, 12.3, 9.2, 6.4, 2.2])
series1 = np.array([14.3, 11.4, 7.4, 5.5, 1.1])
series2 = np.array([14.6, 9.6, 6.5, 4.3, 1.6])
labels = [1,2,3,4,5]
x = np.arange(len(labels))
width = 0.1
plt.xlabel("time(day)", fontsize=12)
plt.ylabel("Surplus of sand(cm3)", fontsize=12)
plt.bar(x-width, series, width, label='cone')
plt.bar(x, series1, width, label='Cylinder')
plt.bar(x+width, series2, width, label='Pyramid')
plt.legend()
plt.xticks(x, labels)
plt.title("The change of sand surplus caused by the impact of sea water on sand pile at different time", fontsize=7)
plt.show()


# # 4 多个图形

# In[9]:


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

font = FontProperties("SimHei")  # 定义一个字体对象
fig = plt.figure(figsize=(8, 6))  # 定义一个8*6的绘图窗体
xlabels = ["直方图1", "直方图2", "直方图3", "直方图4", "直方图5", "直方图6", "直方图7", "直方图8", "直方图9"]
for i in range(1, 10):  # 通过循环绘制9个直方图
    ax = fig.add_subplot(3, 3, i)
    plt.xlabel(xlabels[i-1], fontproperties=font)
    x = np.random.randint(0, 101, 200)
    plt.hist(x, bins=10, color="b", edgecolor="k")
plt.suptitle("直方图比较", fontproperties=font, fontsize=20)  # 添加整个图表的标题
plt.subplots_adjust(left=0.05, right=0.95, hspace=0.4, wspace=0.2)  # 调整子图组合及子图之间的位置与间距
plt.show()

