import csv
import matplotlib.pyplot as plt
from datetime import datetime as d

filename='数据可视化/CSV天气解析/sitka_weather_2018_full.csv'
with open(filename) as f:
    con=csv.reader(f)
    c=next(con)

    rain,date=[],[]

    for x in con:
        current=d.strptime(x[2],'%Y-%m-%d')
        try:
            water=float(x[5])
        except ValueError:
            pass
        else:
            date.append(current)
            rain.append(water)

#对结果可视化

plt.style.use("ggplot")
plt.rcParams['font.sans-serif'] = ['SimHei','Microsoft YaHei','KaiTi']  
plt.rcParams['axes.unicode_minus'] = False 

fig,ax=plt.subplots()

ax.plot(date,rain,color='red',linewidth=3)
ax.set_title("2018 sitka降水量",fontsize=16)
ax.set_xlabel("日期",fontsize=16)
ax.set_ylabel("降水量(mm)",fontsize=16)
fig.autofmt_xdate()

plt.show()