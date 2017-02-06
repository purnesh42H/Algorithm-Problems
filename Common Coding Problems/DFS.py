class Node:
    
    def __init__(self, id, i, j):
        self.id = id
        self.i = i
        self.j = j
        self.adjChild = []
        
    def addChild(self, i, j, grid):
        if i < len(grid) and i >= 0 and j >= 0 and j < len(grid[i]) :
            if grid[i][j] == 1:
                self.adjChild.append(i + j + i*(len(grid[i]) - 1))
        
    def addRowChild(self, grid):
        i = self.i
        j = self.j
        self.addChild(i, j-1, grid)
        self.addChild(i, j+1, grid)

    def addColChild(self, grid):
        i = self.i
        j = self.j
        self.addChild(i-1, j, grid)
        self.addChild(i+1, j, grid)

    def addDiagChild(self, grid):
        i = self.i
        j = self.j
        self.addChild(i-1, j-1, grid)
        self.addChild(i+1, j+1, grid)
        self.addChild(i-1, j+1, grid)
        self.addChild(i+1, j-1, grid)

    def allChildren(self):         
        return self.adjChild
           
    def allPossibleChildren(self, region):
        children = [self.id]
        links = self.allChildren()
        while links:
            link = links.pop()
            if link not in children:
                children.append(link)
                newNode = region[link]
                links.extend(newNode.allChildren())
                
        return children
        
    
def get_biggest_region(grid):
    i = 0
    j = 0
    n = len(grid)
    region = {}
    nodeId = 0
    while i < n:
        j = 0
        m = len(grid[i])
        while j < m:
            if grid[i][j] == 1:
                node = Node(nodeId, i, j)
                node.addColChild(grid)
                node.addRowChild(grid)
                node.addDiagChild(grid)
                region[nodeId] = node
            nodeId = nodeId + 1
            j += 1
        i+=1

    max = 1
    for node in region:
        temp = len(region[node].allPossibleChildren(region))
        if temp > max:
            max = temp
    return max
        

n = int(raw_input().strip())
m = int(raw_input().strip())
grid = []
for grid_i in xrange(n):
    grid_temp = map(int, raw_input().strip().split(' '))
    grid.append(grid_temp)
print get_biggest_region(grid)
