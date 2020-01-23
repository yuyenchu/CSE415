'''EightPuzzleWithManhattan.py
by Yen-Chu Yu
UWNetID: ayu1998
Student number: 1760258

Assignment 2, in CSE 415, Winter 2020.
January 21, 2020.
Univ. of Washington.

This file augments EightPuzzle.py with heuristic information,
so that it can be used by an A* implementation.
The particular heuristic is the total of Manhattan distances
for the 8 tiles

'''

from EightPuzzle import *

CORRECT={0:(0,0),1:(0,1),2:(0,2),
         3:(1,0),4:(1,1),5:(1,2),
         6:(2,0),7:(2,1),8:(2,2)}

def h(s):
  '''We return the sum of Manhattan distances of the 8 tiles.'''
  count = 0
  for i in range(3):
    for j in range(3):
      if(s.b[i][j]!=0):
        (row,col) = CORRECT[s.b[i][j]]
        count += abs(row-i)+abs(col-j)
  return count

# A simple test:
print(h(State(init_state_list)))
