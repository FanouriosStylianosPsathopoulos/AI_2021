# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and child states
        legalMoves = gameState.getLegalActions()
        print("Legal moves are ",legalMoves)


        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        print("Scores are ",scores)
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best
        print("Chosen index is ", chosenIndex)
        print("\n \n ")
        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed child
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        print("Action is ",action)
        childGameState = currentGameState.getPacmanNextState(action)
        newPos = childGameState.getPacmanPosition()
        newFood = childGameState.getFood()
        newGhostStates = childGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        print(childGameState)
        print("New positions is : ",newPos)
        print("New food is : ",newFood.asList())
        print("New ghost states is : ",(newGhostStates))
        #print("loop")
        for x in newGhostStates:
            print(x)
        print("New scared times is : ",newScaredTimes)
        

        #the logic i am gonna use is keeping a distance above 1 from every attacker
        #if it is scared though i will approach 

        #print(type(newScaredTimes))

        if len(newFood.asList())==0:
            return 10000000000

        for x in newGhostStates:
            print(x)
        array_with_val=[]
        for x in newFood.asList():
            array_with_val.append(manhattanDistance(newPos,x))

        print("Array with manhataans is ",array_with_val)

        x_min=min(array_with_val)
        if childGameState.getScore()>0:
            result= childGameState.getScore()-x_min
        else: 
            result=childGameState.getScore()-x_min
        print("X is ",x_min)
        x1,y1=newPos
        print("Total score is ",childGameState.getScore()-x_min)
        if newScaredTimes[0] >=2:
            return childGameState.getScore()-x_min
        else : #this means we have to keep distance

            for each in newGhostStates:
                x_0,y_0=each.configuration.pos
                #print(x,y)

                if abs(x1-x_0 + y1 -y_0 )==1 or (x1==x_0 and y1--y_0) :
                    return -100000000000000000000000
        
        print("\n \n ")
        "*** YOUR CODE HERE ***"
        return childGameState.getScore()-x_min

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.getNextState(agentIndex, action):
        Returns the child game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        print("some more")
        #print(gameState)
        #print(vars(gameState))
        #print(self.depth)
        #print(self.evaluationFunction(gameState))
        #print(gameState.getLegalActions(0))
        #print(gameState.getNumAgents())
        def Max_Value(self,gameState,index,currentDepth):
            legal_actions=gameState.getLegalActions(index)
            nodes_array=[]
            print("Legal actions  are ",legal_actions," and depth is ",currentDepth)
            if len(legal_actions)==0 or currentDepth>self.depth :
                print("mallon edw kai dineis timh ",self.evaluationFunction(gameState) )
                return self.evaluationFunction(gameState)
            for move in legal_actions:
                print("Move is for  ",index ," is : " ,move)
                childGameState= gameState.getNextState(index, move)
                print(childGameState)
                value= Min_Value(self,childGameState,index+1,currentDepth)
                nodes_array.append(value)
            value_to_return=max(nodes_array)
            return value_to_return

        def Min_Value(self,gameState,index,currentDepth):
            #check current Depth only if its the last ghost
            print("checkpoint")
            if index==gameState.getNumAgents()-1:
                print("Last ghost")
                
                legal_actions=gameState.getLegalActions(index)
                if len(legal_actions)==0:
                    print("edw")
                    return self.evaluationFunction(gameState)
                nodes_array=[]
                print("Last ghost 2")
                print("Last ghost legal actions are:",legal_actions)
                for move in legal_actions:
                    print("Move is for  ",index ," is : " ,move)
                    childGameState= gameState.getNextState(index, move)
                    print(childGameState)
                    value= Max_Value(self,childGameState,0,currentDepth+1)
                    print("Value is ",value)
                    nodes_array.append(value)
                value_to_return=min(nodes_array)
                return value_to_return
            else:
                print("Ghost is",index)
                legal_actions=gameState.getLegalActions(index)
                print("Legal actions for index: ",index ," are ",legal_actions)
                if len(legal_actions)==0:
                    return self.evaluationFunction(gameState)
                nodes_array=[]
                for move in legal_actions:
                    print("Move is for  ",index ," is : " ,move)
                    childGameState= gameState.getNextState(index, move)
                    print(childGameState)
                    print("papares",index+1)
                    value= Min_Value(self,childGameState,index+1,currentDepth)
                    print(value,index)
                    nodes_array.append(value)
                value_to_return=min(nodes_array)
                return value_to_return
                        

        #print("Last Value is" , Max_Value(self,gameState,0,0))
        print("ok")
        actions = gameState.getLegalActions(0)
        allActions = {}
        for action in actions:
            allActions[action] = Min_Value(self,gameState.getNextState(0, action), 1, 1)

        #print(print("All actions: ",allActions),allActions)
        print("All actions: ",allActions)
        print("give me sth ")
        direction=max(allActions, key=allActions.get)
        return direction
        #return max(allActions,key=allActions.get)
        util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        def Max_Value(self,gameState,index,currentDepth,a,b):
            print("A and B are ",a,b)
            initial_val=float('-inf')
            legal_actions=gameState.getLegalActions(index)
            nodes_array=[]
            print("Legal actions  are ",legal_actions," and depth is ",currentDepth)
            if len(legal_actions)==0 or currentDepth>self.depth or gameState.isLose() or gameState.isWin():
                #print("mallon edw kai dineis timh ",self.evaluationFunction(gameState) )
                print("current depth is ",currentDepth)
                return self.evaluationFunction(gameState)
            for move in legal_actions:
                print("Move is for  ",index ," is : " ,move)
                childGameState= gameState.getNextState(index, move)
                print(childGameState)
                #print("Current indexoulini is ",index)
                print("Prior call")
                value= Min_Value(self,childGameState,index+1,currentDepth,a,b)
                print("First ",initial_val,value)
                initial_val=max(initial_val,value)
                if initial_val>b: 
                    print("ok 1")
                    print("Value 5 returned for index ",index , " is ",initial_val)
                    return initial_val
                a=max(a,initial_val)
                #nodes_array.append(value)
            #value_to_return=max(nodes_array)
            print("Value 6 returned for index ",index , " is ",initial_val)
            return initial_val

        def Min_Value(self,gameState,index,currentDepth,a,b):
            #check current Depth only if its the last ghost
            print("A and B are ",a,b)
            #print("checkpoint")
            initial_val_pos=float('inf')
            initial_val_neg=initial_val_pos

            if index==gameState.getNumAgents()-1:
                #print("Last ghost")
                
                legal_actions=gameState.getLegalActions(index)
                if gameState.isWin() or gameState.isLose():  #no reason to check the depth since it only changes at when Max plays
                    return self.evaluationFunction(gameState)
                if len(legal_actions)==0:
                    #print("edw")
                    print("current depth 2 is ",currentDepth)
                    return self.evaluationFunction(gameState)
                nodes_array=[]
                print("Last ghost 2")
                print("Last ghost legal actions are:",legal_actions)
                for move in legal_actions:
                    print("Move is for  ",index ," is : " ,move)
                    childGameState= gameState.getNextState(index, move)
                    print(childGameState)
                    value= Max_Value(self,childGameState,0,currentDepth+1,a,b)
                    print("Value is ",value)
                    print("Second  1",initial_val_pos,value)
                    initial_val_pos=min(initial_val_pos,value)
                    if initial_val_pos<a: 
                        print("ok 2")
                        print("Value 3 returned for index ",index , " is ",initial_val_pos)
                        return initial_val_pos
                    b=min(b,initial_val_pos)
                
                print("Value 4 returned for index ",index , " is ",initial_val_pos)    
                return initial_val_pos
            else:
                print("Ghost is",index)
                legal_actions=gameState.getLegalActions(index)
                if gameState.isWin() or gameState.isLose():  #no reason to check the depth since it only changes at when Max plays
                    return self.evaluationFunction(gameState)
                print("Legal actions for index: ",index ," are ",legal_actions)
                if len(legal_actions)==0:
                    print("current depth 3 is ",currentDepth)
                    return self.evaluationFunction(gameState)
                nodes_array=[]
                for move in legal_actions:
                    print("Move is for  ",index ," is : " ,move)
                    childGameState= gameState.getNextState(index, move)
                    print(childGameState)
                    value= Min_Value(self,childGameState,index+1,currentDepth,a,b)
                    print("Value is ",value)
                    print("Second 2",initial_val_pos,value)
                    initial_val_pos=min(initial_val_pos,value)
                    if initial_val_pos<a: 
                        print("ok 2")
                        print("Value returned for index ",index , " is ",initial_val_pos)
                        return initial_val_pos
                    b=min(b,initial_val_pos)
        
                print("Value 2 returned for index ",index , " is ",initial_val_pos)
                return initial_val_pos

                        

        positive_infinity = float('inf')
        print('Positive Infinity: ', positive_infinity)
 
        # Defining a negative infinite integer
        negative_infinity = float('-inf')
        print('Negative Infinity: ', negative_infinity)

        actions = gameState.getLegalActions(0)
        allActions = 0
        action_for_return=""
        print("First actions are ",actions)
        initial_val=float('-inf')
        for action in actions:
            print("Action is ",action)
            successorState = gameState.getNextState(0, action)
            #print("sth big like my dick")
            allActions = Min_Value(self,successorState, 1, 1,negative_infinity,positive_infinity)
            print("ok mate  ",initial_val,allActions)
            #initial_val=max(initial_val,allActions)
            if allActions > initial_val:   #find the max of the ghost actions
                #print("ok mate  ",bestActionValue,nice)
                initial_val = allActions
                
                action_for_return = action
            if initial_val>positive_infinity: 
                print("ok 1")
                print("Last person ",initial_val,action)
                return action
            print("Last ",initial_val,action)
            negative_infinity=max(negative_infinity,initial_val)
            
            #action_for_return=action
        #print("gtxm")
        print("Last person 2 ",action_for_return)
        return action_for_return
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()    

# Abbreviation
better = betterEvaluationFunction
