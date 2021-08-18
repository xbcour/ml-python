import numpy as np
import numpy as num
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('ex1data1.txt', names=['population', 'profit'])  # 读取文件 指定列名

# data.plot.scatter('population', 'profit', label='profit of population')  # 绘制散点图 数据可视化

data.insert(0, 'x_0', 1)  # 构建[1 x]
columns = data.shape[1]

x = data.iloc[:, 0:columns-1]
y = data.iloc[:, columns-1:columns]

x = x.values
y = y.values



