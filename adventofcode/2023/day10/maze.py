class Pipe:
    def __init__(self, name, x ,y):
        self.name = name
        # self.map = map
        self.x = x
        self.y = y

    def setMap(self,map):
        self.map = map

    def calculate(self):
        coordinates = {
            "7": [(-1, 0),(0, 1)],
            "F": [(1, 0),(0, 1)],
            "J": [(-1, 0),(0, -1)],
            "L": [(1, 0),(0, -1)],
            "-": [(1, 0),(-1, 0)],
            "|": [(0, 1),(0, -1)],
        }
        # 假设 self.name 的值为 name
        if self.name in coordinates:
            x, y = coordinates[self.name][0]
            x1, y1 = coordinates[self.name][1]
            list = []
            self.findPipe(list, x, y)
            self.findPipe(list, x1, y1)
            self.list = list


    def findPipe(self, list, x, y):
        x = x + self.x
        y = y + self.y
        if x == -1 or y == -1:
            pass
        if x >= len(map[0]) or y >= len(map):
            pass
        else:
            list.append(self.map[y][x])


def mapToPicture(map):
    result = [ [ point.name for point in row] for row in map]
    for row in result:
        for element in row:
            print(element, end="")  # 打印每个元素并以空格分隔
        print()  # 在每行结束时打印换行符
    return  result
    pass

charMapper = {
    "7": "┐",
    "F": "┌",
    "J": "┘",
    "L": "└",
    "-": "-",
    "|": "|",
    "*": "*",
    "S": "S"
}

def mapToPictureOnlyPath(map):
    all_x = [point.x for row in map for point in row if getattr(point, 'mark', None)]
    all_y = [point.y for row in map for point in row if getattr(point, 'mark', None)]
    max_x = max(all_x)
    min_x = min(all_x)
    max_y = max(all_y)
    min_y = min(all_y)

    result = [[point.name if getattr(point, 'mark', None) else "*" for point in row] for row in map]

    for i in range(min_y,max_y+1):
        for j in range(min_x,max_x+1):
            print(charMapper[map[i][j].name] if getattr(map[i][j], 'mark', None) else "*" if getattr(map[i][j], 'enclose', True) else "0", end="")  # 打印每个元素并以空格分隔
            pass
        print()
        pass
    print("next step")
    # for row in result:
    #     for element in row:
    #         print(element, end="")  # 打印每个元素并以空格分隔
    #     print()  # 在每行结束时打印换行符
    return  result
    pass



# 读入文件内容
with open('input.txt', 'r') as file:
    content = file.readlines()

# 去除每行末尾的换行符
content = [line.strip() for line in content]
two_d_array = [list(row.strip()) for row in content]

map = []
for i in range(len(two_d_array)):
    row_map = []
    for j in range(len(two_d_array[0])):
        pass
        row_map.append(Pipe(two_d_array[i][j], j, i))
    map.append(row_map)
    pass

mapToPicture(map)

one_d_array = [element for row in map for element in row]
for pipe in one_d_array:
    pipe.setMap(map)
    pipe.calculate()
    pass

start_point = next((tup for tup in one_d_array if tup.name == 'S'), None)

def findPeripheralNodesToS(start_point):
    points = [(-1,0),(1,0),(0,1),(0,-1)]
    list = [ map[start_point.y+point[1]][start_point.x+point[0]] for point in points]
    # list = [point for point in list if point.list.index(start_point)]
    return list

points = findPeripheralNodesToS(start_point)
possibleNodes = [point for point in points if  point.list is not None and  (start_point in point.list)]

def printMap(map, path):
    for node in path:
        node.mark = True
    test = mapToPictureOnlyPath(map)
    print("find the way ++++++++++++")
    # print(test)
    pass

def findTheWay(inputPath):
    stack = [inputPath]
    while stack:
        pointway = stack.pop()
        point = pointway.point
        path = pointway.path
        if point.list is not None:
            nextNode = next((next for next in point.list if next!=pointway.pre),None)
            start = next((next for next in point.list if next==start_point),None)
            if len(path) >= 1:
                # printMap(point.map,path)
                pass
            if start is not None and len(path)>2:
                printMap(point.map,path)
                return path
                pass
            if nextNode is not None:
                path.append(nextNode)
                stack.append(PointWay(point, nextNode, path))
    printMap(inputPath.point.map,inputPath.path)
    pass

class PointWay:
    def __init__(self, pre, point,path):
        self.pre = pre
        self.point = point
        self.path = path



for point in possibleNodes:
    path = findTheWay(PointWay(start_point,point,[start_point,point]))
    if path is not None:
        print("++++++++++++++++++++++++++++++++++++++++++++++++")
        print(len(path)/2)
        # print(path)

print("end")


print("++++++++++++++++++++++++++++++++++++++++++++++++step2 find the loop++++++++++++++++++++++++++++++++++++++++++++++++")


def valid(x, y, map):
    max_x = len(map[0])-1
    max_y = len(map)-1
    if x<0 or x>max_x or y<0 or y>max_y:
        return False
    return True


def resolveRoundPoint(pointList):
    stack = pointList
    while stack:
        cur_point = stack.pop()
        if getattr(cur_point, 'visit', None) :
            continue
        cur_point.visit = True
        # if(cur_point.enclose is not None):
        #     pass
        coordinates = [(0,1),(0,-1),(1,0),(-1,0)]
        try:
            points = [ cur_point.map[cur_point.y+coordinate[0]][cur_point.x+coordinate[1]] for coordinate in coordinates if valid(cur_point.x+coordinate[1],cur_point.y+coordinate[0],cur_point.map)]
        except Exception:
            print("Invalid")

        hasNoEncloseTile = next( (p for p in points if getattr(p,'enclose',None)!=None and p.enclose==False),None)
        isBoundNode = next( (coordinate for coordinate in coordinates if not valid(cur_point.x+coordinate[1],cur_point.y+coordinate[0],cur_point.map)) ,None)
        if hasNoEncloseTile or isBoundNode:
            if not getattr(cur_point, 'mark', None):
            # if cur_point.name == "*":
                cur_point.enclose = False
                for p in points:
                    if not getattr(p,'visit',None) :
                        stack.append(p)
            # if cur_point.name == "":
            #     pass
        pass


def filterTheOutLoop(map):
    all_x = [point.x for row in map for point in row if getattr(point, 'mark', None)]
    all_y = [point.y for row in map for point in row if getattr(point, 'mark', None)]
    max_x = max(all_x)
    min_x = min(all_x)
    max_y = max(all_y)
    min_y = min(all_y)

    # 最外层设置成非 enclosed
    for i in range(len(map)):
        for j in range(len(map[0])):
            if j< min_x or j> max_x or i<min_y or i> max_y:
                point = map[i][j]
                point.enclose = False
                point.visit = True
        pass
    pass
    mapToPictureOnlyPath(map)
    # if True:
    #     return
    firstPoints = []
    for i in range(min_x,max_x+1):
        firstPoints.append(map[min_y][i])
        firstPoints.append(map[max_y][i])
    for i in range(min_y,max_y+1):
        firstPoints.append(map[i][min_x])
        firstPoints.append(map[i][max_x])

    resolveRoundPoint(firstPoints)

filterTheOutLoop(map)


print("filter:")
mapToPictureOnlyPath(map)

# print(map)

