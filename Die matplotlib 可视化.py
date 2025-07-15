import matplotlib.pyplot as plt
import die

#创建Die类
d1=die.Die()
d2=die.Die()

result=[]
k1=d1.throw_die(10000)
k2=d2.throw_die(10000)
for x in range(10000):
    a=k1[x]+k2[x]
    result.append(a)


#分析结果
f=[result.count(c) for c in range(2,d1.side+d2.side+1) ]



plt.style.use('bmh')
plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False  

fig,ax=plt.subplots()
ax.plot(list(range(2,d1.side+d2.side+1)),f,color='blue',linewidth=3)

ax.set_title("掷两个D6 10000次的结果",fontsize=16)
ax.set_xlabel("结果",fontsize=16)
ax.set_ylabel("结果的频率",fontsize=16)
ax.set_xticks(range(2,d1.side+d2.side+1)) #设置x轴刻度

ax.tick_params(axis='both',labelsize=12)

plt.show()