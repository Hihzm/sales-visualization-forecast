import random as r
import matplotlib.pyplot as plt

class RandomWalk:
    #一个模拟随机漫步的类、
    def __init__(self,walk_point=10000):
        #初始化随机漫步的点数
        self.walk_point=walk_point

        #起点于（0,0）开始
        self.x=[0]
        self.y=[0]

    def walk(self):
        #停止前不断漫步
        while len(self.x) < self.walk_point:
            x_step=self.get_step()
            y_step=self.get_step()

            #防止原地踏步
            if x_step ==0 and  y_step==0:
                continue
            
            #下一次的漫步坐标
            xz=self.x[-1]+x_step
            yz=self.y[-1]+y_step

            self.x.append(xz)
            self.y.append(yz)

    def get_step(self):
        direction=r.choice([-1,1])
        dis=r.choice([0,1,2,3,4])
        a=direction * dis
        return a


rw=RandomWalk()
rw.walk()
plt.style.use('bmh')
#绘制图像，并且调整尺寸大小

fig,ax=plt.subplots(figsize=(15,9))
p_num=range(rw.walk_point)
ax.scatter(rw.x,rw.y,c=p_num,cmap='viridis',edgecolors='none',s=20)   

#突出起点和终点
ax.scatter(0,0,c='red',edgecolors='none',s=50)
ax.scatter(rw.x[-1],rw.y[-1],c='blue',edgecolors='none',s=50)

#隐藏坐标轴
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show() 