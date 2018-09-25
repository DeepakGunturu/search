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

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
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

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # Standard DFS algorithm using the stack data structure
    fringeFunction = util.Stack()

    # Adding the start state of the problem to the stack along with the direction array and the cost
    fringeFunction.push(problem.getStartState())
    fringeFunction.push([])
    fringeFunction.push(0)
  
    # Keeping a track of states that have already been visited
    isVisited = []

    while True:

        # If there are no states in the fringe function, we break out of the loop
        if fringeFunction.isEmpty():
            break

        # The current cost, direction array, and the present state are popped from the fringe
        currCost = fringeFunction.pop()
        currDirs = fringeFunction.pop()
        currState = fringeFunction.pop()

        # Bookkeeping the states
        if not currState in isVisited:
            isVisited.append(currState)

            # If the state is the goal of Pacman, returning the current directions
            if problem.isGoalState(currState):
                return currDirs

            # Storing the states, directions, and costs of the successors and searching each node deeply for the goal states
            for path in problem.getSuccessors(currState):
                nextStates = path[0]
                nextDirs = path[1]
                nextCost = path[2]
                fringeFunction.push(nextStates)
                fringeFunction.push(currDirs+[nextDirs])
                fringeFunction.push(nextCost+currCost)
    
    # If there is nothing in the fringe function
    return []

# This algorithm is the same algorithm as the DFS except that we use a queue instead to search the nodes at each level instead of searching each node deeply
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    fringeFunction = util.Queue()
    fringeFunction.push(problem.getStartState())
    fringeFunction.push([])
    fringeFunction.push(0)
    isVisited = []

    while True:

        if fringeFunction.isEmpty():
            break

        currState = fringeFunction.pop()
        currDirs = fringeFunction.pop()
        currCost = fringeFunction.pop()

        if not currState in isVisited:
            isVisited.append(currState)

            if problem.isGoalState(currState):
                return currDirs

            for path in problem.getSuccessors(currState):
                nextStates = path[0]
                nextDirs = path[1]
                nextCost = path[2]
                fringeFunction.push(nextStates)
                fringeFunction.push(currDirs+[nextDirs])
                fringeFunction.push(nextCost+currCost)
    
    return []

# This algorithm is the same algorithm as the DFS except that we use a priority queue taking into priority the cheapest nodes instead to search the nodes at each level instead of searching each node deeply
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    fringeFunction = util.PriorityQueue()
    fringeFunction.push((problem.getStartState(),[],0),0)
    isVisited = []    
    
    while True:

        if fringeFunction.isEmpty():
            break
        
        tmp = fringeFunction.pop()
        currState = tmp[0]
        currDirs = tmp[1]
        currCost = tmp[2]


        if not currState in isVisited:
            isVisited.append(currState)
            
            if problem.isGoalState(currState):
                return currDirs
            
            for path in problem.getSuccessors(currState):
                nextStates = path[0]
                nextDirs = path[1]
                nextCost = path[2]
                tup = (nextStates,currDirs+[nextDirs],nextCost+currCost)
                fringeFunction.push((tup),nextCost+currCost)
    
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
