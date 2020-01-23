'''EightPuzzleWithHamming.py
This file augments EightPuzzle.py with heuristic information,
so that it can be used by an A* implementation.
The particular heuristic is the number of tiles out of place,
but not the blank, or the "Hamming Distance".

'''

from EightPuzzle import *

CORRECT=[[0,1,2],[3,4,5],[6,7,8]]

def h(s):
  '''We return the number of tiles out of place excluding blank.'''
  count = 0
  for i in range(3):
    for j in range(3):
      if (s.b[i][j] != 0 and s.b[i][j] != CORRECT[i][j]):
        count+=1

  return count

# A simple test:
#print(h(State(init_state_list)))
