'''Farmer_Fox.py
by Yen-Chu Yu
UWNetID: ayu1998
Student number: 1760258

Assignment 2, in CSE 415, Winter 2020.
January 21, 2020.
Univ. of Washington.
 
This file contains my problem formulation for the problem of
the Farmer, Fox, Chicken, and Grain.
'''
#<METADATA>
QUIET_VERSION = "0.2"
PROBLEM_NAME = "Farmer, Fox, Chicken, and Grain"
PROBLEM_VERSION = "0.1.3"
PROBLEM_AUTHORS = ['Yen-Chu Yu']
PROBLEM_CREATION_DATE = "21-JAN-2020"
PROBLEM_DESC=\
'''This formulation of the Towers of Hanoi problem uses generic
Python 3 constructs and has been tested with Python 3.7.
It is designed to work according to the QUIET2 tools interface.
'''
#</METADATA>

#<COMMON_DATA>
class State:
  def __init__(self, d):
    self.d = d

  def __eq__(self,s2):
    for p in ['left','right']:
      if self.d[p] != s2.d[p]: return False
    return True

  def __str__(self):
    # Produces a textual description of a state.
    # Might not be needed in normal operation with GUIs.
    txt = "["
    for side in ['left','right']:
      txt += str(self.d[side]) + " ,"
    return txt[:-2]+"]"

  def __hash__(self):
    return (self.__str__()).__hash__()

  def copy(self):
    # Performs an appropriately deep copy of a state,
    # for use by operators in creating new states.
    news = State({})
    for side in ['left','right']:
      news.d[side]=self.d[side][:]
    return news

  def check_logic(side):
    if "Farmer" in side or len(side) <= 1 or len(side) == 3:
      return True
    elif len(side) == 2 and ("Fox" in side) and ("Grain" in side):
      return True
    else: return False
   
  def can_move(self,From,To,Chara):
    '''Tests whether it's legal to move a character Chara in 
        state s from the From side of the river to the To side .'''
    try:
      pf=self.d[From].copy() # side character goes from
      pt=self.d[To].copy()   # side character goes to
      # no character to move or farmer not with the character
      #print("from="+From+";chara="+Chara+";pf="+str(pf)+";pt="+str(pt)+str((Chara not in pf) or ("Farmer" not in pf)))
      if (Chara not in pf) or ("Farmer" not in pf):
        #print("pf="+str(pf))
        return False
      if Chara != "Farmer":
        pf.remove(Chara)
        pt.append(Chara)
      pf.remove("Farmer")
      pt.append("Farmer")
      #print("from="+From+";chara="+Chara+";pf="+str(pf)+";pt="+str(pt)+str(State.check_logic(pf) and State.check_logic(pt)))
      return State.check_logic(pf) and State.check_logic(pt)
    except (Exception) as e:
      print(e)

  def move(self,From,To,Chara):
    '''Assuming it's legal to make the move, this computes
       the new state resulting from moving the specified 
       character from the From side to the To side.'''
    news = self.copy() # start with a deep copy.
    pf=news.d[From]
    pt=news.d[To]
    if Chara != "Farmer":
      pf.remove(Chara)
      pt.append(Chara)
    pf.remove("Farmer")
    pt.append("Farmer")
    pf.sort()
    pt.sort()
    #news.d[From]=pf # remove farmer and Chara from the From side
    #news.d[To]=pt # Put character to destination side
    return news # return new state
  
def goal_test(s):
  '''If the left side is empty, then s is a goal state.'''
  return s.d['left']==[]

def goal_message(s):
  return "Everyone passed the river!"

class Operator:
  def __init__(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)

#</COMMON_CODE>

#<INITIAL_STATE>
INITIAL_DICT = {'left': ["Farmer","Grain","Chicken","Fox"], 'right':[] }
CREATE_INITIAL_STATE = lambda: State(INITIAL_DICT)
#DUMMY_STATE =  {'left':[], 'right':[] }
#</INITIAL_STATE>

#<OPERATORS>
side_combinations = [("left","right","Farmer"), ("right","left","Farmer"),
                     ("left","right","Grain"),  ("right","left","Grain"),
                     ("left","right","Chicken"),("right","left","Chicken"),
                     ("left","right","Fox"),    ("right","left","Fox")]
                     
OPERATORS = [Operator("Move character "+c+" from "+p+" to "+q,
                      lambda s,p1=p,q1=q,c1=c: s.can_move(p1,q1,c1),
                      # The default value construct is needed
                      # here to capture the values of p&q separately
                      # in each iteration of the list comp. iteration.
                      lambda s,p1=p,q1=q,c1=c: s.move(p1,q1,c1) )
             for (p,q,c) in side_combinations]
#</OPERATORS>

#<GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>

