import sys
import resource
import timeit
import heapq


class Node:
    
    def __init__(self, puzzle=None):
        self.puzzle = puzzle
        self.parent = None
        self.children = []
        self.depth = 0
        self.dirTakenFromParent = None

    def printPuzzle(self):
        ''' prints in matrix format '''
        count = 0
        while count < len(self.puzzle):
            
            if count%3 == 0:
                print("\n")
            
            print(self.puzzle[count], end=' ')
            count+= 1
        print("\n")
            
    def moveLeft(self, index):
        
        if index % 3 != 0:
            
            ''' create matrix for child node '''
            copyPuzzle = list(self.puzzle[:]) # create shallow copy of list
            
            tempVal = copyPuzzle[index - 1]
            
            copyPuzzle[index -1] = copyPuzzle[index]
            
            copyPuzzle[index] = tempVal
            
            ''' make assignments in the child node '''
            childNode = Node(tuple(copyPuzzle))
            childNode.parent = self
            # copies parent's direction list child direction list
            #childNode.dirTakenFromParent.extend(self.dirTakenFromParent)
            # this adds the parent's depth and 1 for the child
            childNode.depth = self.depth + 1
            childNode.dirTakenFromParent = 1
         
            ''' assign childNode to parent's children list '''
            self.children.append(childNode)
            
    def moveRight(self, index):
        
        if index % 3 !=  2:
            
            ''' create matrix for child node '''
            copyPuzzle = list(self.puzzle[:]) # create shallow copy of list
            
            tempVal = copyPuzzle[index + 1]
            
            copyPuzzle[index + 1] = copyPuzzle[index]
            
            copyPuzzle[index] = tempVal
            
            ''' make assignments in the child node '''
            childNode = Node(tuple(copyPuzzle))
            childNode.parent = self
            # copies parent's direction list child direction list
            #childNode.dirTakenFromParent.extend(self.dirTakenFromParent)
            childNode.dirTakenFromParent = 2
            # this adds the parent's depth and 1 for the child
            childNode.depth = self.depth + 1
         
            ''' assign childNode to parent's children list '''
            self.children.append(childNode)
         
    def moveUp(self, index):
        
        if index >= 3:
            
            ''' create matrix for child node '''
            copyPuzzle = list(self.puzzle[:]) # create shallow copy of list
            
            tempVal = copyPuzzle[index - 3]
            
            copyPuzzle[index - 3] = copyPuzzle[index]
            
            copyPuzzle[index] = tempVal
            
            ''' make assignments in the child node '''
            childNode = Node(tuple(copyPuzzle))
            childNode.parent = self
            # copies parent's direction list child direction list
            #childNode.dirTakenFromParent.extend(self.dirTakenFromParent)
            childNode.dirTakenFromParent = 3
            # this adds the parent's depth and 1 for the child
            childNode.depth = self.depth + 1
         
            ''' assign childNode to parent's children list '''
            self.children.append(childNode)  
    def moveDown(self, index):
        
        if index < 6:
            
            ''' create matrix for child node '''
            copyPuzzle = list(self.puzzle[:]) # create shallow copy of list
            
            tempVal = copyPuzzle[index + 3]
            
            copyPuzzle[index + 3] = copyPuzzle[index]
            
            copyPuzzle[index] = tempVal
            
            ''' make assignments in the child node '''
            childNode = Node(tuple(copyPuzzle))
            childNode.parent = self
            # copies parent's direction list child direction list
            #childNode.dirTakenFromParent.extend(self.dirTakenFromParent)
            childNode.dirTakenFromParent = 4
            # this adds the parent's depth and 1 for the child
            childNode.depth = self.depth + 1
         
            ''' assign childNode to parent's children list '''
            self.children.append(childNode)  
            
    def meetGoalNode(self):
        ''' determines if puzzle is in correct increasing order '''
        # initialize counters
        p_prev = 0
        p_next = 1
        
        while p_next < len(self.puzzle):
            
            # retrun false if list[i] not less than list[i+1]
            if (self.puzzle[p_prev] < self.puzzle[p_next]) is False:
                return False
            
            # increment the counters
            p_prev += 1
            p_next += 1
        return True
    def meetGoalNode2(self):
    	''' second method to determine if strictly increasing node is met '''
    	count = 0
    	while count < len(self.puzzle):

    		if self.puzzle[count] != count:

    			return False

    		count += 1
    		
    	return True
    
    def pathToGoal(self):
        ''' method that returns and array with the path to goal node '''
        
        path = []
        # initialize the very first parent
        parent = self
        
        
        while parent !=  None:
            # evaluates which values corresponds to which direction
            if parent.dirTakenFromParent == 1:
                path.insert(0, 'Left')
            elif parent.dirTakenFromParent == 2:
                path.insert(0, 'Right')
            elif parent.dirTakenFromParent == 3:
                path.insert(0, 'Up')
            elif parent.dirTakenFromParent == 4:
                path.insert(0, 'Down')
            parent = parent.parent
            
        return path
            
            
            
            
    def sameMatrix(self, matrix):
        ''' determines if the martrix is the same as cmp matrix '''

        i = 0
        while i < len(matrix):
            # if not equal somewhere - return false
            if matrix[i] != self.puzzle[i]:
                
                return False
            i += 1
        
        return True
     
    def expandNode(self):
        
        count = 0
        zeroIndex = None
        ''' find the zeroIndex '''
        while count < len(self.puzzle):
            if self.puzzle[count] == 0:
                zeroIndex = count
                
            count += 1
    
        self.moveUp(zeroIndex)
        self.moveDown(zeroIndex)
        self.moveLeft(zeroIndex)
        self.moveRight(zeroIndex)
        
    def getManhattan(self):
        
        ''' get the manhattan distance '''
        heuristicVal = 0
        positionIndex = 0
        x_axisP = 0
        y_axisP = 0
        x_axisW = 0
        y_axisW = 0
        while positionIndex < len(self.puzzle):
            ''' where am i in the puzzle calculation'''
            print("Number:", self.puzzle[positionIndex], "at index", positionIndex)
            # columns
            if positionIndex % 3 == 0:
                y_axisP = 1
            if positionIndex % 3 == 1:
                y_axisP = 2
            if positionIndex % 3 == 2:
                y_axisP = 3
            print("x_axisP:", x_axisP)  
            
            # row
            if positionIndex < 3:
                x_axisP = 3
            if positionIndex < 6 and positionIndex > 2:
                x_axisP = 2
            if positionIndex > 5:
                x_axisP = 1
            print("y_axisP:", y_axisP)    
            ''' where it should be in the puzzle calculation '''
            x_positionW = self.puzzle[positionIndex] 
            x_positionW = x_positionW - 1
            
            if (x_positionW )% 3 == 1:
                y_axisW = 1
                
            if (x_positionW ) % 3 == 2:
                y_axisW = 2
                
            if (x_positionW) % 3 == 0:
                y_axisW = 3
                
            print("x_axisW:", x_axisW)
            y_positionW = self.puzzle[positionIndex]
            y_positionW = y_positionW - 1
            
            if y_positionW < 3:
                y_axisW = 3
                
            if  y_positionW < 6 and y_positionW > 2: 
                y_axisW = 2
                
            if y_positionW > 5:
                y_axisW = 1
                
            print("y_axisW:", y_axisW)    
            # final calculation
            heuristicVal += abs(y_axisP - y_axisW)
            heuristicVal += abs(x_axisP - x_axisW)
            positionIndex += 1
            
        return heuristicVal
    
    def getCost(self):
        
        dictionary = { 0:(0,0), 1:(0,1), 2: (0,2), 3:(1,0), 4:(1,1), 5:(1,2), 6:(2,0), 7:(2,1), 8:(2,2)}
        

        index = 0
        heuristicVal = self.depth
        
        while index < len(self.puzzle):
            
            # where i currently am
            currentPosition = dictionary[index]
            #print("the index:", index, "currentPosition mapping:", currentPosition)
            
            # ignore this 
            currentValue = self.puzzle[index]
            #print("currentValue (ie the number)", currentValue)
            
            currentValuePair = dictionary[currentValue]
            #print("currentValue Pair(ie the mapping)", currentValuePair)
            
            # heuristic value x position
            #print("x:", currentPosition[0] - currentValuePair[0])
            #print("y:", currentPosition[1] - currentValuePair[1])
            heuristicVal += abs(currentPosition[0] - currentValuePair[0])
            heuristicVal += abs(currentPosition[1] - currentValuePair[1])
            
            index += 1
        return heuristicVal 
            
            
                
        
        

    def __lt__(self, other):
        ''' comparision operator for Node class '''
        return self.puzzle.index(0) < other.puzzle.index(0)




                
            
                
#########
def bfs(eightPuzzle):
    # initialize time
    t = timeit.Timer()
    # create a node obj
    node = Node(eightPuzzle)
    # max depth
    max_depth = 0
    # frontier and queue defined
    frontier = []
    # append first node
    frontier.append(node)
    # explored nodes
    # explored = []
    explored = set()
    # frontier and explored
    frontierAndExplored = set()
    
    # return empty list if failure
    emptylist = ["failed"]
    # count nodes expanded
    nodesExpanded = 0
    
    while len(frontier) > 0:
        
        stateNode = frontier.pop(0)
        #stateNode.printPuzzle()
        #print(stateNode.depth)
        
        #explored.append(stateNode)
        #explored_set = set()
        
        
        ''' calls expand node function - moveUp moveDown moveLeft moveRight'''
        stateNode.expandNode()
    
        
        if stateNode.meetGoalNode():
            # return array
            c = [stateNode, nodesExpanded]
            # checks
            sys.stdout = open('output.txt', 'w')
            print("path_to_goal:", stateNode.pathToGoal())
            print("cost_of_path:", len(stateNode.pathToGoal()))
            print("nodes_expanded:", len(explored))
            print("search_depth:", stateNode.depth)
            print("max_search_depth:", max_depth)
            print("running_time:", t.timeit())
            print("max_ram_usage:", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1000000)
            return c
        
        ''' moved this here because was counting one up '''
        explored.add(stateNode)
        frontierAndExplored.add(stateNode.puzzle)
        
        nodesExpanded += 1
        # for every child in the children list
        for child in stateNode.children:
           if child.puzzle not in frontierAndExplored:
            #if child not in seen:
                frontier.append(child)
                frontierAndExplored.add(child.puzzle)
                if child.depth > max_depth:
                   max_depth = child.depth
    return  emptylist
           



def dfs(eightPuzzle):
    # time
    t = timeit.Timer()
    # create a node obj
    node = Node(eightPuzzle)
    # max depth
    max_depth = 0
    # frontier and queue defined
    frontier = []
    # append first node
    frontier.append(node)
    # explored nodes
    # explored = []
    explored = set()
    # frontier and explored
    frontierAndExplored = set()
    
    # return empty list if failure
    emptylist = ["failed"]
    # count nodes expanded
    nodesExpanded = 0
    
    while len(frontier) > 0:
        
        stateNode = frontier.pop()
        #stateNode.printPuzzle()
        #print(stateNode.depth)
        
        #explored.append(stateNode)
        #explored_set = set()
        
        
        ''' calls expand node function - moveUp moveDown moveLeft moveRight'''
        stateNode.expandNode()
        

        
        if stateNode.meetGoalNode():
            # return array
            #sys.stdout = open('output.txt', 'w')
            c = [stateNode, nodesExpanded]

            sys.stdout = open('output.txt', 'w')
            print("path_to_goal:", stateNode.pathToGoal())
            print("cost_of_path:", len(stateNode.pathToGoal()))
            print("nodes_expanded:", len(explored))
            print("search_depth:", stateNode.depth)
            print("max_search_depth:", max_depth)
            print("running_time:", t.timeit())
            print("max_ram_usage:", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1000000)
            
            
            
            return c
        
        ''' moved this here because was counting one up '''

        explored.add(stateNode)
        frontierAndExplored.add(stateNode.puzzle)
        nodesExpanded += 1
        # for every child in the children list
        count = len(stateNode.children) - 1
        while count > -1:
           if stateNode.children[count].puzzle not in frontierAndExplored:
            #if child not in seen:
                frontier.append(stateNode.children[count])
                frontierAndExplored.add(stateNode.children[count].puzzle)
                
                if stateNode.children[count].depth > max_depth:
                   max_depth = stateNode.children[count].depth
           count+= -1
        
    return  emptylist

def ast(eightPuzzle):
    # time
    t = timeit.Timer()
    # create a node obj
    node = Node(eightPuzzle)
    # tuple for comparisions - cost and node value
    nodeTuple = (node.getCost(), node)
    # max depth
    max_depth = 0
    # frontier and queue defined
    frontier = []
    heapq.heapify(frontier)
    # pushfirst node first node
    heapq.heappush(frontier, nodeTuple)
    # explored nodes
    # explored = []
    explored = set()
    # frontier and explored
    frontierAndExplored = set()
    
    # return empty list if failure
    emptylist = ["failed"]
    # count nodes expanded
    nodesExpanded = 0
    
    while len(frontier) > 0:
        
        stateNode = heapq.heappop(frontier)
        #stateNode.printPuzzle()
        #print(stateNode.depth)
        
        #explored.append(stateNode)
        #explored_set = set()
        
        
        ''' calls expand node function - moveUp moveDown moveLeft moveRight'''
        stateNode[1].expandNode()
    
        
        if stateNode[1].meetGoalNode():
            # return array
            c = [stateNode[1], nodesExpanded]
            # checks
            sys.stdout = open('output.txt', 'w')
            print("path_to_goal:", stateNode[1].pathToGoal())
            print("cost_of_path:", len(stateNode[1].pathToGoal()))
            print("nodes_expanded:", len(explored))
            print("search_depth:", stateNode[1].depth)
            print("max_search_depth:", max_depth)
            print("running_time:", t.timeit())
            print("max_ram_usage:", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1000000)
            return c
        
        ''' moved this here because was counting one up '''
        explored.add(stateNode[1])
        frontierAndExplored.add(stateNode[1].puzzle)
        
        nodesExpanded += 1
        # for every child in the children list
        for child in stateNode[1].children:
           if child.puzzle not in frontierAndExplored:
            #if child not in seen:
                heapq.heappush(frontier,(child.getCost(), child))
                
                frontierAndExplored.add(child.puzzle)
                
                if child.depth > max_depth:
                   max_depth = child.depth
           elif child.puzzle in frontierAndExplored:
              
              updatePath(child,frontier)
              heapq.heapify(frontier)
                
            
    return  emptylist

def updatePath0(child, frontier):
    ''' check to see if the depth of another path is shorter - returns 1 on success'''   
    for theLists in frontier:
        if theLists[1].puzzle == child.puzzle and theLists[1].depth > child.depth:
             theLists = (child.getCost(), theLists[1])
             return 1
    return 0


def updatePath(child, frontier):
    ''' check to see if the depth of another path is shorter - returns 1 on success'''   
    for theLists in frontier:
        if theLists[1].depth > child.depth:
             theLists = (child.getCost(), theLists[1])
             return 1
    return 0




''' removes the commas from the string '''
arrCharacters = sys.argv[2].replace(",", "")

arrList = []
zeroIndex = None

''' coverts command line input into in array and finds index of the zero'''
zeroCount = 0
for i in arrCharacters:
    arrList.append( int (i))
    if(i == "0"):
        zeroIndex = zeroCount
    zeroCount +=1
    

eightPuzzle = tuple(arrList)


if sys.argv[1] == 'ast':
	ast(eightPuzzle)

elif sys.argv[1] == 'bfs':
    #print(True)
    bfs(eightPuzzle)
    
elif sys.argv[1] == 'dfs':
    
	dfs(eightPuzzle)



# if sys.argv[1] == 'bfs':
#     t = time.process_time()
#     bfs(eightPuzzle)
#     elapsed_time = time.process_time() - t
#     print(elapsed_time)
#     print("resource", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1000000)

# if sys.argv[1] == 'dfs':

#     dfs(eightPuzzle)

# t = time.clock()
# dfs(eightPuzzle)
# m = time.clock()
# print(m)

        
#node = Node(eightPuzzle)
##print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
#node.printPuzzle()
#node.expandNode()
#
#for i in node.children:
#    i.printPuzzle()
#bfs(eightPuzzle)
