#!/usr/bin/python3
''' BFS.py
by Yen-Chu Yu
UWNetID: ayu1998
Student number: 1760258

Assignment 2, in CSE 415, Winter 2020.
January 21, 2020.
Univ. of Washington.

Breadth-First Search of a problem space.
 Version 0.1

 Usage:
 python3 BFS.py TowersOfHanoi
# The numbered STEP comments in the function BFS correspond
 to the algorithm steps for iterative depth-first as presented
 in Slide 8 of the "Basic Search Algorithms" lecture.
'''

import sys

if sys.argv==[''] or len(sys.argv)<2:
#  import EightPuzzle as Problem
  import TowersOfHanoi as Problem
else:
  import importlib
  Problem = importlib.import_module(sys.argv[1])

print("\nWelcome to BFS")
COUNT = None
BACKLINKS = {}

def runBFS():
  initial_state = Problem.CREATE_INITIAL_STATE()
  print("Initial State:")
  print(initial_state)
  global COUNT, BACKLINKS, MAX_OPEN_LENGTH
  COUNT = 0
  BACKLINKS = {}
  MAX_OPEN_LENGTH = 0
  BFS(initial_state)
  print(str(COUNT)+" states expanded.")
  print('MAX_OPEN_LENGTH = '+str(MAX_OPEN_LENGTH))

def BFS(initial_state):
  global COUNT, BACKLINKS, MAX_OPEN_LENGTH

# STEP 1. Put the start state on a list OPEN
  OPEN = [initial_state]
  CLOSED = []
  BACKLINKS[initial_state] = None

# STEP 2. If OPEN is empty, output “DONE” and stop.
  while OPEN != []:
    report(OPEN, CLOSED, COUNT)
    if len(OPEN)>MAX_OPEN_LENGTH: MAX_OPEN_LENGTH = len(OPEN)

# STEP 3. Select the first state on OPEN and call it S.
#         Delete S from OPEN.
#         Put S on CLOSED.
#         If S is a goal state, output its description
    S = OPEN.pop(0)
    CLOSED.append(S)

    if Problem.GOAL_TEST(S):
      print(Problem.GOAL_MESSAGE_FUNCTION(S))
      path = backtrace(S)
      print('Length of solution path found: '+str(len(path)-1)+' edges')
      return
    COUNT += 1

# STEP 4. Generate the list L of successors of S and delete 
#         from L those states already appearing on CLOSED.
    L = []
    for op in Problem.OPERATORS:
      if op.precond(S):
        new_state = op.state_transf(S)
        if not (new_state in CLOSED):
          L.append(new_state)
          BACKLINKS[new_state] = S

# STEP 5. Delete from L any members of OPEN that occur on L.
#         Insert all members of L at the end of OPEN.
    for s2 in L:
      for i in range(len(OPEN)):
        if (s2 == OPEN[i]):
          L.remove(s2); break


    OPEN =  OPEN+L
    print_state_list("OPEN", OPEN)
# STEP 6. Go to Step 2.

def print_state_list(name, lst):
  print(name+" is now: ",end='')
  for s in lst[:-1]:
    print(str(s),end=', ')
  print(str(lst[-1]))

def backtrace(S):
  global BACKLINKS
  path = []
  while S:
    path.append(S)
    S = BACKLINKS[S]
  path.reverse()
  print("Solution path: ")
  for s in path:
    print(s)
  return path    
  
def report(open, closed, count):
  print("len(OPEN)="+str(len(open)), end='; ')
  print("len(CLOSED)="+str(len(closed)), end='; ')
  print("COUNT = "+str(count))

if __name__=='__main__':
  runBFS()

