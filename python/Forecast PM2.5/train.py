import sys
import pandas as pd
import numpy as np

data = pd.read_csv('Dataset/train.csv', encoding = 'big5')# 利用 pands 进行读取文件操作,big5为繁体编码
data = data.iloc[:, 3:]#去掉前三行代码
data[data == 'NR'] = 0#将等于NR的数据全部补0
raw_data = data.to_numpy()#变为二维数组==矩阵
month_data = {}
for month in range(12):#分为12个月
    sample = np.empty([18, 480])#开辟18*（24*20）的二维空间
    for day in range(20):#分为20天
        sample[:, day * 24 : (day + 1) * 24] = raw_data[18 * (20 * month + day) : 18 * (20 * month + day + 1), :]#将每月每天每18条数据赋值到上一组数据后面的位置，从day2开始（day=1）
    month_data[month] = sample#二维数组 ((1month((1day((0hour),(1hour),....)),(2day),....)),(2month),......,(12month)）
#print(month_data)
x = np.empty([12 * 471, 18 * 9], dtype = float)
y = np.empty([12 * 471, 1], dtype = float)
for month in range(12):
    for day in range(20):
        for hour in range(24):
            if day == 19 and hour > 14:
                continue
            x[month * 471 + day * 24 + hour, :] = month_data[month][:,day * 24 + hour : day * 24 + hour + 9].reshape(1, -1) #每个月会有480hrs，每 9 小时形成一个 data，每个月会有 471 个 data，故总资料数为 471 * 12 笔，而每笔 data 有 9 hour * 18 features (18 个 features * 9 小时)。
            y[month * 471 + day * 24 + hour, 0] = month_data[month][9, day * 24 + hour + 9] #value
print(x)
print(y)