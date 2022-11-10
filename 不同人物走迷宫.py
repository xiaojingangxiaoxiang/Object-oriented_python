# 三个人物走迷宫
import numpy  # 导入numpy这个文件,主要用于二维数组的创建 和random函数的调用

class Map:
    # 用于初始化地图的类
    length : int # 地图的长
    width : int # 地图的宽
    map : None

    def __init__(self, length : int, width : int) -> map:
        self.length = length
        self.width = width
        self.map = numpy.zeros((self.length, self.width), dtype=numpy.int0) # 这里利用numpy创建了一个二维数组
        self.initMap() # 调用map初始化方法完成地图的初始化

    def initMap(self):
        # 初始化地图的方法
        for i in range(self.length):
            for j in range(self.width):
                rad =  numpy.random.random((1,1)) # 这个就是返回一个1个数到数组中 范围是[0,1)
                if i == 0 or i == self.length - 1:
                    self.map[i][j] = 1
                if j == 0 or j == self.length -1:
                    self.map[i][j] = 1
                if rad[0] < 0.3:
                    self.map[i][j] = 1
            # 设置起点和终点
            self.map[1][1] = 0
            self.map[1][self.width - 2] = 0
            self.map[1][self.width//2] = 0
            self.map[self.length - 2][self.width - 2] = 0
            self.map[self.length - 2][1] = 0
            self.map[self.length//3][self.width - 2] = 0
        
    def clearMap(self):
        # 将地图重置
        for i in range(self.length):
            for j in range(self.width):
                if self.map[i][j] == 2 or self.map[i][j] == 3:
                    self.map[i][j] = 0

class Person:
    # 定义两个类变量一个是长度，一个是宽度注释为int类型
    length = 10
    width = 10
    speed = 1  # 人物的移动速度/每次走一步所用的时间
    time = 0  # 用于计算所用时间
    map : None

    def __init__(self, length : int, width : int, map) -> None:
        self.length = length
        self.width = width
        self.map = map
        
    def findWay_1():
        # 策略下 右 上 左
        pass

    def findWay_2():
        # 策略下 左 上 右
        pass

    
# 战士类speed快，但是只有一种寻路方法       
class Warrior(Person):
    def __init__(self, length: int, width: int, map) -> None:
        super().__init__(length, width, map)
        self.speed = 1 # 没走一个耗费1s

    def findWay_1(self,i, j, goal_L, goal_W):
        # 如果目标位子数字已经是2说明找到路
        if(self.map[goal_L][goal_W] == 2):
            return True
        elif(self.map[i][j] == 0):
            # 假设当前位置可以走
            self.map[i][j] = 2
            self.time += self.speed
            # 寻路的策略上->右->下->左
            if(self.findWay_1(i+1,j,goal_L, goal_W)): # 下移
                return True
            elif(self.findWay_1(i,j+1,goal_L, goal_W)): # 右移
                return True
            elif(self.findWay_1(i-1,j,goal_L, goal_W)): # 上移
                return True
            elif(self.findWay_1(i,j-1,goal_L, goal_W)): # 左移
                return True
            else:
                self.map[i][j]=3
                self.time += 4*self.speed # 回溯一次花费四倍时间
                return False
        else:
            return False
            
# 智者类speed慢，但是有两种种寻路方法
class Wiseman(Person):
    time_1 = 0 # 子类特有的变量 用于记录方式2时间
    time = 0  # 继承这里只是为了明显一点，没有重写
    def __init__(self, length: int, width: int, map) -> None:
        super().__init__(length, width, map)
        self.speed = 1.5 # 每走一步要3s

    def findWay_1(self, i, j,goal_L,goal_W):
        # 如果目标位子数字已经是2说明找到路
        if(self.map[goal_L][goal_W] == 2):
            return True
        elif(self.map[i][j] == 0):
            # 假设当前位置可以走
            self.map[i][j] = 2
            self.time += self.speed
            # 寻路的策略上->右->下->左
            if(self.findWay_1(i+1,j,goal_L, goal_W)): # 下移
                return True
            elif(self.findWay_1(i,j+1,goal_L, goal_W)): # 右移
                return True
            elif(self.findWay_1(i-1,j,goal_L, goal_W)): # 上移
                return True
            elif(self.findWay_1(i,j-1,goal_L, goal_W)): # 左移
                return True
            else:
                self.map[i][j]=3
                self.time += 3*self.speed # 回溯一次花费四倍时间
                return False
        else:
            return False
        
    def findWay_2(self,i, j,goal_L,goal_W):
        # 如果目标位子数字已经是2说明找到路
        if(self.map[goal_L][goal_W] == 2):
            return True
        elif(self.map[i][j] == 0):
            # 假设当前位置可以走
            self.map[i][j] = 2
            self.time_1 += self.speed
            # 寻路的策略上->右->下->左
            if(self.findWay_2(i+1,j,goal_L, goal_W)): # 下移
                return True
            elif(self.findWay_2(i,j-1,goal_L, goal_W)): # 左移
                return True
            elif(self.findWay_2(i-1,j,goal_L, goal_W)): # 上移
                return True
            elif(self.findWay_2(i,j+1,goal_L, goal_W)): # 右移
                return True
            else:
                self.map[i][j]=3
                self.time_1 += 3*self.speed # 回溯一次花费四倍时间
                return False
        else:
            return False

# 冒险家类速度适中，有回溯快的技能
class Adventurer(Person):
    def __init__(self, length: int, width: int, map) -> None:
        super().__init__(length, width, map)
        self.speed = 1.25
    
    def findWay_1(self, i, j,goal_L,goal_W):
        # 如果目标位子数字已经是2说明找到路
        if(self.map[goal_L][goal_W] == 2):
            return True
        elif(self.map[i][j] == 0):
            # 假设当前位置可以走
            self.map[i][j] = 2
            self.time += self.speed
            # 寻路的策略上->右->下->左
            if(self.findWay_1(i+1,j,goal_L, goal_W)): # 下移
                return True
            elif(self.findWay_1(i,j+1,goal_L, goal_W)): # 右移
                return True
            elif(self.findWay_1(i-1,j,goal_L, goal_W)): # 上移
                return True
            elif(self.findWay_1(i,j-1,goal_L, goal_W)): # 左移
                return True
            else:
                self.map[i][j]=3
                self.time += 2*self.speed # 回溯一次花费四倍时间
                return False
        else:
            return False

 
def createGoal(length, width):
    goal_L = length - 2
    goal_W = length - 2
    goal = [0,0]
    rad =  numpy.random.random((1,1))
    if rad[0] <= 0.5:
        # 这个坐标就是地图的右下角
        goal_L = length - 2
        goal_W = width -2 
    else :
        # 这个坐标是地图的左下角
        goal_L = length - 2
        goal_W = 1
    goal[0] = goal_L
    goal[1] = goal_W
    return goal
        
def createStart(length,width):
    start_L = 1
    start_W = 1
    start = [0,0]
    rad = numpy.random.random((1,1))
    if rad[0] < 0.25:
        start_L = 1
        start_W = 1
    elif rad[0] < 0.50:
        start_L = 1
        start_W = width//2
    elif rad[0] < 0.75:
        start_L = length//3
        start_W = width - 2
    start[0] = start_L
    start[1] = start_W
    return start
    

def main():
    # 初始化地图
    mp = Map(15,15)
    map1 = mp.map
    # 初始化起点和终点
    goal = createGoal(mp.length, mp.width)
    start = createStart(mp.length, mp.width)
    print("=======规则========")
    print("终点是",goal)
    print("起点是",start)
    print("=======战士========")
    wa = Warrior(mp.length, mp.width, map1)
    wa.findWay_1(i=start[0], j=start[1], goal_L=goal[0], goal_W=goal[1])
    print(wa.map)
    print(wa.time)

    print("=======智者========")
    mp.clearMap()
    wise = Wiseman(mp.length, mp.width, map1)
    wise.findWay_1(i=start[0], j=start[1], goal_L=goal[0], goal_W=goal[1])
    print(wise.map)
    print(wise.time)
    mp.clearMap()
    wise.findWay_2(i=start[0], j=start[1], goal_L=goal[0], goal_W=goal[1])
    print(wise.map)
    print(wise.time_1)
    
    print("=======冒险家=======")
    mp.clearMap()
    ad = Adventurer(mp.length, mp.width, map1)
    ad.findWay_1(i=start[0], j=start[1], goal_L=goal[0], goal_W=goal[1])
    print(ad.map)
    print(ad.time)
    if map1[goal[0]][goal[1]] == 2:
        print("找到终点")
    else:
        print("没有找到终点")

if __name__ == '__main__':
    main()