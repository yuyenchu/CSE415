def useAlphaBetaPruning(prune=False):

def statesAndCutoffsCounts():

def setMaxPly(maxply=-1):

def useSpecialStaticEval(func):

def staticEval(state):


bestMove
# Minimax Pseudocode
def alpaBetaMinimax(state, alpha, beta, depth, d_limit):

   """ 
   Returns best score for the player associated with the given node.
   Also sets the variable bestMove to the move associated with the
   best score at the root node.  
   """
   global bestMove
   # check if at search bound
   if (depth == d_limit):
      return staticEval(state)

   # check if leaf
   children = successors(state)
   if (len(children) == 0):
      if (depth == 0):
         bestMove = [] 
      return staticEval(node)

   # initialize bestMove
   if (depth == 0):
      bestMove = operator of first child
      # check if there is only one option
      if len(children) == 1
         return None

   if (depth%2 == state.whose_move):
      for (k in children.keys()):
         result = alphaBetaMinimax(children[k], alpha, beta, depth+1, d_limit)
         if (result > alpha):
            alpha = result
            if (depth == 0):
               bestMove = k
         if (alpha >= beta):
            # count++
            return alpha
      return alpha

   else:
      for (k in children.keys()):
         result = alphaBetaMinimax(children[k], alpha, beta, depth+1, d_limit)
         if (result < beta):
            beta = result
            if (depth == 0):
               bestMove = k
         if (beta <= alpha)
            # count++
            return beta
      return beta

  

DETERMINISTIC = True
# for the deterministic version, where the dice are loaded in a way
# that prevents all randomness.

#DETERMINISTIC = False
# for the stochastic version of the game ("SSBG"), so that dice get
# rolled normally.


from backgState import *

DONE = False
def check_legal(current_state, move, deterministic=False):
  '''return a new state if leagal, return NONE if not
  assuming move is a string
  '''
  whose_move = current_state.whose_move
  new_state = None
  if move in ["Q", "q"]:
    return None
  if move in ["P", "p"]:
    if moves_exist(current_state, whose_move, die1, die2):
      return None
    else:
      new_state = bgstate(current_state)
      new_state.whose_move=1-whose_move
      return new_state
  else:
    try:
      move_list = move.split(',')
      if len(move_list)==3 and move_list[2] in ['R','r']:
        dice_list = [die2, die1]
      else:
        dice_list = [die1, die2]
      checker1, checker2 = move_list[:2]
    except:
      return None
    for i in range(2):
      if i==1 and checker2 in ['P','p']:
        new_state = bgstate(current_state)
        new_state.whose_move=1-whose_move
        return new_state

      pt = int([checker1, checker2][i])
      if pt==0:
        if not whose_move in current_state.bar:
          return None
        new_state = handle_move_from_bar(current_state, whose_move, dice_list[i])
        if not new_state:
          return None
        return new_state
      if any_on_bar(current_state, whose_move):
        return None
      if pt < 1 or pt > 24:
        return None
      if not whose_move in current_state.pointLists[pt-1]:
        return None

      die = dice_list[i]
      if whose_move==W:
        dest_pt = pt + die
      else:
        dest_pt = pt - die
      if dest_pt > 24 or dest_pt < 1:
        born_off_state = bear_off(current_state, pt, dest_pt, whose_move)
        if born_off_state:
          ##unknown type of state, need checking
          return born_off_state
        return None
      
      dest_pt_list = current_state.pointLists[dest_pt-1]
      if len(dest_pt_list) > 1 and dest_pt_list[0]!=whose_move:
        return None
      if not new_state:
        new_state = bgstate(current_state)
      new_state.pointLists[pt-1].pop()
      new_state = hit(new_state, dest_pt_list, dest_pt)
      new_state.pointLists[dest_pt-1].append(whose_move)
      new_state.whose_move=1-whose_move
      return new_state

def hit(new_state, dest_pt_list, dest_pt):
  opponent = 1-new_state.whose_move
  if len(dest_pt_list)==1 and dest_pt_list[0]==opponent:
    if opponent==W:
      new_state.bar.insert(W, 0) # Whites at front of bar
    else:
      new_state.bar.append(R) # Reds at end of bar
    new_state.pointLists[dest_pt-1]=[]
  return new_state

def bear_off(state, src_pt, dest_pt, who):
  # Return False if 'who' is not allowed to bear off this way.
  # Otherwise, create the new state showing the result of bearing
  # this one checker off, and return the new state.

  # First of all, is bearing off allowed, regardless of the dice roll?
  if not bearing_off_allowed(state, who): return False
  # Direct bear-off, if possible:
  pl = state.pointLists[src_pt-1]
  if pl==[] or pl[0]!=who:
    print("Cannot bear off from point "+src(src_pt))
    return False
  # So there is a checker to possibly bear off.
  # If it does not go exactly off, then there must be
  # no pieces of the same color behind it, and dest
  # can only be one further away.
  good = False
  if who==W:
    if dest_pt==25:
       good = True
    elif dest_pt==26:
       for point in range(18,src_pt-1):
         if W in state.pointLists[point]: return False
       good = True
  elif who==R:
    if dest_pt==0:
       good = True
    elif dest_pt== -1:
       for point in range(src_pt, 6):
         if R in state.pointLists[point]: return False
       good = True
  if not good: return False 
  born_off_state = bgstate(state)
  born_off_state.pointLists[src_pt-1].pop()
  if who==W: born_off_state.white_off.append(W)
  else:  born_off_state.red_off.append(R)
  return born_off_state


def moves_exist(state, die1, die2, who):
  return False  # placeholder.

def any_on_bar(state, who):
  return who in state.bar

def remove_from_bar(new_state, who):
  #removes a white from start of bar list,
  # or a red from the end of the bar list.
  if who==W:
    del new_state.bar[0]
  else:
    new_state.bar.pop()
  print("After removing a "+get_color(who)+" from the bar,")
  print("  the bar is now: "+str(new_state.bar))

def handle_move_from_bar(state, who, die):
  # We assume there is a piece of this color available on the bar.
  if who==W: target_point=die
  else: target_point=25-die
  pointList = state.pointLists[target_point-1]
  if pointList!=[] and pointList[0]!=who and len(pointList)>1:
     print("Cannot move checker from bar to point "+str(target_point)+" (blocked).")
     return False
  new_state = bgstate(state)
  new_state = hit(new_state, pointList, target_point)
  remove_from_bar(new_state, who)
  new_state.pointLists[target_point-1].append(who)
  return new_state

def bearing_off_allowed(state, who):
  # True provided no checkers of this color on the bar or in
  # first three quadrants.
  if any_on_bar(state, who): return False
  if who==W: point_range=range(0,18)
  else: point_range=range(6,24)
  pl = state.pointLists
  for i in point_range:
    if pl[i]==[]: continue
    if pl[i][0]==who: return False
  return True