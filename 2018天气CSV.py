import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename='数据可视化/CSV与JSON文件/sitka_weather_2018_full.csv'

with open(filename) as f:
    c=csv.reader(f)
    con=next(c)

    high=[]
    low=[]
    date=[]
    for x in c:
        d=datetime.strptime(x[2],'%Y-%m-%d')
        try:
            ma=int(x[8])
            mi=int(x[9])
        except ValueError:
            pass
        else:
            high.append(ma)
            low.append(mi)
            date.append(d)

#开始可视化
plt.style.use('ggplot')
plt.rcParams['font.sans-serif'] = ['SimHei','Microsoft YaHei','KaiTi']  
plt.rcParams['axes.unicode_minus'] = False  

fig,ax=plt.subplots()
ax.plot(date,high,c='red',linewidth=3,alpha=0.5)
ax.plot(date,low,c='blue',linewidth=3,alpha=0.5)
ax.fill_between(date,high,low,color='purple',alpha=0.25)

ax.set_title("2018年美国stika每月最高温与最低温",fontsize=16)
ax.set_xlabel("日期",fontsize=16)
ax.set_ylabel("温度(F)",fontsize=16)
fig.autofmt_xdate()
ax.tick_params(axis='both',which='major',labelsize=12)

plt.show()