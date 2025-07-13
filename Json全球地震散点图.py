import json
import plotly.express as px
import pandas as pd

#探索数据结构
fn='数据可视化/JSON地震文件解析/eq_data_30_day_m1.json'
with open(fn) as f:
    eq=json.load(f)

# 解析为可读文件(解析完后应立刻注释)
#readable_file='eq_readable_data.json'
#with open(readable_file,'w') as f:
    #json.dump(eq,f,indent=4)

number=eq['features']

#提取信息

mags,titles,lons,lats=[],[],[],[]
for n in number:
    title=n['properties']['title']
    mag=n['properties']['mag']
    x=n['geometry']['coordinates'][0]
    y=n['geometry']['coordinates'][1]

    mags.append(mag)
    titles.append(title)
    lons.append(x)
    lats.append(y)

#绘制散点图

data=pd.DataFrame(
    data=zip(lons,lats,titles,mags), columns=['经度','纬度','位置','震级']
)
fig=px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    title="全球地震散点图",
    size='震级',
    size_max=10,
    color='震级'
)

fig.write_html('global_eq.html')
fig.show()