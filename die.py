import random as r
class Die:
    #模拟骰子的面
    def __init__(self,side=6):
        #初始化骰子的属性
        self.side=side


    def throw_die(self,throwtime=1):
        #掷骰子
        list1=[]
        for _ in range(throwtime):
            number=r.randint(1,self.side)
            list1.append(number)
        return list1