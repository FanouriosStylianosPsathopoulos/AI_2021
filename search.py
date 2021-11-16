# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    frontier=util.Stack()
    expanded=dict()
    frontier.push([problem.getStartState(),[]])
    
    visited=util.Queue()
    i=0
    while True:
        if (frontier.isEmpty()):
            break;
        else:
            new_node=frontier.pop()

        if (new_node[0] not in visited.list):
            visited.push(new_node[0])
            #print(problem.expand(new_node[0]))
            if problem.isGoalState(new_node[0]):

                #print("U did bre mpagasa")
                return new_node[1]
            else:
                
                expansion_nodes=problem.expand(new_node[0])
                
                for each_node in expansion_nodes:
                    result=new_node[1] + [each_node[1]]
                    frontier.push([each_node[0],result])
                       

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    frontier=util.Queue()
    expanded=dict()
    starting_node=[problem.getStartState(),[]]
    
    frontier.push(starting_node)

    if problem.isGoalState(starting_node[0]):
        return starting_node[1]
    
    visited=util.Queue()
  
    while True:
        if (frontier.isEmpty()):
            break;
        else:
            new_node=frontier.pop()

        if problem.isGoalState(new_node[0]):
        
            return new_node[1]

        if (new_node[0] not in visited.list):
            visited.push(new_node[0])
            
            expansion_nodes=problem.expand(new_node[0])
            
            for each_node in expansion_nodes:
            
                result=new_node[1] + [each_node[1]]
                frontier.push([each_node[0],result])

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    frontier=util.PriorityQueue()
    expanded=dict()
    nodes_in_expanded=dict()
    nodes_for_exp=list()
    starting_node=[problem.getStartState(),[],0,heuristic(problem.getStartState(),problem)]
    counter=0
    buzz=0
    
    
    frontier.push(starting_node,heuristic(problem.getStartState(),problem))
    
    if len(starting_node[0])==1:
        var=1
    elif type(starting_node[0][1]) is list:
        var=2
    else:
        var=3
    
    i=0
    while True:
        if (frontier.isEmpty()):
            break;
        else:
            new_node=frontier.pop()
        
        if problem.isGoalState(new_node[0]):
            return new_node[1]
        
        if var!=2:
            
            if new_node[0] not in nodes_in_expanded.keys():
                expansion_nodes=problem.expand(new_node[0])
                nodes_in_expanded[new_node[0]]=expansion_nodes
           
                for each_node in expansion_nodes:

                    if each_node[0] not in nodes_in_expanded.keys():
                        
                        result=new_node[1] + [each_node[1]]
                   
                        result_distance=new_node[2] + each_node[2]
                    
                        f_n=result_distance+heuristic(each_node[0],problem)

                        frontier.push([each_node[0],result,result_distance,f_n],f_n)
        
        else:

                if new_node[0][0] not in expanded.keys(): #not such key 

                    expansion_nodes=problem.expand(new_node[0])
                    take_list=[]
                    for x in new_node[0][1]:
                        take_list.append(x)
                    expanded[new_node[0][0]]=[take_list]

                    for each_node in expansion_nodes:
                        
                        if (each_node[0][0] not in expanded.keys()): #doesnt exist in expanded
                            
                            list_with_states=[]
                            
                            list_with_sth=[]

                            for each in new_node[0][1]:
                                list_with_sth.append(each)

                        
                            sth=[each_node[0][0],list_with_sth]
                        
                            result=new_node[1] + [each_node[1]]
                       
                            result_distance=new_node[2] + each_node[2]
                        
                            f_n=result_distance+heuristic(sth,problem)
                            
                            list_with_states.append([result,f_n,list_with_sth,list_with_sth])

                            frontier.push([sth,result,result_distance,f_n],f_n)
                        else: #maybe exists but not for the same situation
                            
                            already_exists=expanded[each_node[0][0]]

                            list_with_new_node=[]
                            

                            if new_node[0][1] not in already_exists:

                                for each in new_node[0][1]:
                                    list_with_new_node.append(each)

                                sth=[each_node[0][0],list_with_new_node]

                                each_node[0][1]=list_with_new_node

                                list_with_states=[]
                            
                                result=new_node[1] + [each_node[1]]
                           
                                result_distance=new_node[2] + each_node[2]
                            
                                f_n=result_distance+heuristic(sth,problem)

                                list_with_states.append([result,f_n,list_with_new_node,list_with_new_node])

                                frontier.push([sth,result,result_distance,f_n],f_n)


                else:
                    
                    already_exists=expanded[new_node[0][0]]
                    
                    stl_list=[]
                    
                    if new_node[0][1] not in already_exists:

                        expansion_nodes=problem.expand(new_node[0])
                        
                        for x in new_node[0][1]:
                            stl_list.append(x)

                        expanded[new_node[0][0]].append(stl_list)

                        already_exists=expanded[new_node[0][0]]
                        
                        for each_node in expansion_nodes:
                            if (each_node[0][0] not in expanded.keys()):
                                list_with_states=[]
                                    
                                list_with_sth=[]
                            
                                result=new_node[1] + [each_node[1]]
                                
                                
                                result_distance=new_node[2] + each_node[2]

                                for each in new_node[0][1]:

                                    list_with_sth.append(each)

                                sth=[each_node[0][0],list_with_sth]

                                f_n=result_distance+heuristic(sth,problem)
                                    
                                
                                frontier.push([sth,result,result_distance,f_n],f_n)
                
                            else:
                                
                                already_exists=expanded[each_node[0][0]]
                                
                                list_with_new_node=[]
                                
                                if new_node[0][1] not in already_exists:

                                    for each in new_node[0][1]:
                                        list_with_new_node.append(each)

                                    sth=[each_node[0][0],list_with_new_node]

                                    list_with_states=[]
                                
                                    list_with_new_node=[]
                                
                                    result=new_node[1] + [each_node[1]]
                               
                                    result_distance=new_node[2] + each_node[2]
                                
                                    f_n=result_distance+heuristic(sth,problem)

                                    list_with_states.append([result,f_n,list_with_new_node,list_with_new_node])

                                    frontier.push([sth,result,result_distance,f_n],f_n)
                

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
