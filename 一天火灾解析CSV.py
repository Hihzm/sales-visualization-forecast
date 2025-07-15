import csv
import plotly.express as px
import pandas as pd
from datetime import datetime as d

date=''
filename='数据可视化/CSV火灾解析/world_fires_1_day.csv'

with open(filename) as f:
    con=csv.reader(f)
    c=next(con)

    lons,lats,brig=[],[],[]
    lo=c.index('longitude')
    la=c.index('latitude')
    br=c.index('brightness')

    for x in con:
        if not date:
            date=x[c.index("acq_date")]

        try:
            lon=float(x[lo])
            lat=float(x[la])
            bri=float(x[br])

        except ValueError:
            pass
        else:
            lats.append(lat)
            lons.append(lon)
            brig.append(bri)

    
data=pd.DataFrame(
    data=zip(lons,lats,brig),columns=['经度','纬度','火灾强度']
)

#可视化

fig=px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200,200],
    range_y=[-90,90],
    title=f'{date}\n全球火灾强度图',
    width=1000,
    height=1000,
    size='火灾强度',
    size_max=10,
    color='火灾强度',
    opacity=0.5,
    color_continuous_scale='hot',
)
fig.update_xaxes(tickvals=list(range(-200,200,20)))
fig.update_yaxes(tickvals=list(range(-90,91,10)))

fig.write_html("files.html")
fig.show()