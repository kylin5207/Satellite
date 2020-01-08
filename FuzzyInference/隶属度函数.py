# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 15:18:57 2020
隶属度函数仿真测试
论文：考虑模糊推理及蒙特卡洛方法的毁伤评估研究
@author: 尚梦琦
"""
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import math

#1. 生成温度数据
t = np.linspace(18,30,100)

#2. 记地面存储温度为Tn=20℃,部件主要构建材料融化的温度时Tm=25℃。
Tn = 20
Tm = 25

#3. 戒上型、中间对称型、戒下型
y_sub = np.zeros_like(t)

for i in range(len(t)):
    
    if t[i] <= Tn:
        y_sub[i] = 1
    
    elif t[i] >= Tn and t[i] <= Tm:
        num = - t[i]**2
        y_sub[i] = math.exp(num)
    
    else:
        num = -t[i] ** 2
        y_sub[i] = 1 - math.exp(num)


#4. 绘制图像
#设置中文字体
mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False

plt.plot(t, y_sub)        
plt.title("隶属度函数在不同区间上的图像")
plt.xlabel("Temperature")
plt.ylabel("Value")

