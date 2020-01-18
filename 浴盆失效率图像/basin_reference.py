# -*- coding: utf-8 -*-
"""
Kylin
故障概率曲线——浴盆曲线
绘制相应的分布函数、密度函数和故障率函数图像
"""
import numpy as np
import matplotlib.pyplot as plt


#1. 生成时间序列
t = np.linspace(0,4,100)

#2. 设置相关参数值
yitalist = [2, 5, 10]
beitalist = [0.5, 1, 4]

#3. 绘制分布函数和密度函数图像
fig, ax = plt.subplots(3,3)
plt.subplots_adjust(wspace=0.6, hspace=0.9)
fig.suptitle("Distribution Function (F) and Density Fuction(f)")

sub = 1

for i in range(3):
    #获取相应的yita值
    yita = yitalist[i]
    
    for j in range(3):
        #获取相应的beita值
        beita = beitalist[j]
        
        title = "η = " + str(yita) + ",β = " + str(beita)
        
        F = 1 - np.exp(1 - np.exp(t/yita)**beita)
        f = np.exp(1 - np.exp(t/yita)**beita) * (np.exp(t/yita)**beita) * (beita * t**(beita-1) / yita**beita)
        
        plt.subplot(3,3,sub)
    
        plt.plot(t, F, color="blue", label="F")
        plt.plot(t, f, color="red", label="f")
        plt.xlabel("t")
        plt.ylabel("value")
        plt.legend()
        plt.title(title)
        
        sub += 1

#4. 绘制失效率函数图像
fig, ax = plt.subplots(3,3)
plt.subplots_adjust(wspace=0.6, hspace=0.9)
fig.suptitle("Fault Fuction(r)")

sub = 1

for i in range(3):
    #获取相应的yita值
    yita = yitalist[i]
    
    for j in range(3):
        #获取相应的beita值
        beita = beitalist[j]
        
        title = "η = " + str(yita) + ",β = " + str(beita)
        
        r = np.exp(t/yita) * (beita * t**(beita-1) / yita**beita)
        
        plt.subplot(3,3,sub)
    
        plt.plot(t, r, color="blue")
        plt.xlabel("t")
        plt.ylabel("value")
        plt.title(title)
        
        sub += 1

