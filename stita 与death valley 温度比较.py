import csv
import matplotlib.pyplot as plt
from datetime import datetime as d

filename1='数据可视化/CSV天气解析/sitka_weather_2018_full.csv'
filename2='数据可视化/CSV天气解析/death_valley_2018_full.csv'

#the temperature of sitka
with open(filename1) as f:
    con=csv.reader(f)
    c=next(con)

    s_tmax=[]
    s_tmin=[]
    s_date=[]
    for x in con:
        da=d.strptime(x[2],'%Y-%m-%d')
        try:
            ma=int(int(x[8])-32)*5/9
            mi=int(int(x[9])-32)*5/9
        except ValueError:
            pass
        else:
            s_tmax.append(ma)
            s_tmin.append(mi)
            s_date.append(da)

#the temperature of death valley
with open(filename2) as f:
    content=csv.reader(f)
    c1=next(content)

    d_tmax=[]
    d_tmin=[]
    d_date=[]
    for x in content:
        da=d.strptime(x[2],'%Y-%m-%d')
        try:
            ma=int(int(x[6])-32)*5/9
            mi=int(int(x[7])-32)*5/9
        except ValueError:
            pass

        else:
            d_tmax.append(ma)
            d_tmin.append(mi)
            d_date.append(da)

#可视化
plt.style.use('bmh')
plt.rcParams['font.sans-serif'] = ['SimHei','Microsoft YaHei','KaiTi']  
plt.rcParams['axes.unicode_minus'] = False  

fig,ax=plt.subplots()

ax.plot(s_date,s_tmax,c='red',linewidth=3,alpha=0.5)
ax.plot(s_date,s_tmin,c='blue',linewidth=3,alpha=0.7)
ax.fill_between(s_date,s_tmax,s_tmin,color='purple',alpha=0.3)

ax.plot(d_date,d_tmax,c='red',linewidth=3,alpha=0.7)
ax.plot(d_date,d_tmin,c='blue',linewidth=3,alpha=0.4)
ax.fill_between(d_date,d_tmax,d_tmin,color='purple',alpha=0.3)



ax.set_title("2018 stika温度和death valley温度比较",fontsize=16)
ax.set_xlabel("日期",fontsize=16)
ax.set_ylabel("温度(℃)",fontsize=16)

plt.show()