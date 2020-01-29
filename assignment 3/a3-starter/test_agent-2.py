from backgState import *

def useAlphaBetaPruning(prune=False):
  global pruning
  pruning = prune
def statesAndCutoffsCounts():
  return p_count


#placeholders
def setMaxPly(maxply=-1):
  return None
def useSpecialStaticEval(func):
  return None


def staticEval(state):
  val = 0
  for i in range(0,24):
    pt=state.pointLists[i]
    for c in pt:
      if (c==0):
        val += (23-i)
      else:
        val -= i
  return val

bestMove=[]
moves=[]
pruning=True
p_count=0
s_count=0
#bestMove is the move agent will choose at current state

# moves is a dict contain moves from root to its children,
# where children states are keys and their moves are values

#pruning is boolean for active pruning or not

#p_count is the count for number of pruning actions

#s_count is the count for number of states explored in one move

# Minimax Pseudocode
def aBMinimax(state, alpha, beta, depth, d_limit):

  global bestMove, moves, pruning, p_count, s_count
  # check if at search bound
  if (depth == d_limit):
    return staticEval(state)

  # check if leaf
  children = successors(state)
  s_count += len(children)

  if (len(children) == 0):
    if (depth == 0):
        bestMove = [] 
    return staticEval(state)

  # initialize bestMove
  if (depth == 0):
    bestMove = next(iter(moves.values())) #first move possible
    # check if there is only one option
    if (len(children) == 1):
        return None

  if (depth%2 == state.whose_move):
    for c in children:
        result = aBMinimax(c, alpha, beta, depth+1, d_limit)
        if (result > alpha):
          alpha = result
          if (depth == 0):
              bestMove = moves[c]
        if (alpha >= beta and pruning):
          p_count += 1
          return alpha
    return alpha

  else:
    for c in children:
        result = aBMinimax(c, alpha, beta, depth+1, d_limit)
        if (result < beta):
          beta = result
          if (depth == 0):
              bestMove = moves[c]
        if (beta <= alpha and pruning):
          p_count += 1
          return beta
    return beta

#generating all possible states
def successors(state,die1,die2):
  mover = state.whose_move
  ptsWithColor = []
  possibleStates = []
  count = 0
  for pt in state.pointLists:
    count += 1
    if mover in pt:
      ptsWithColor.append(count)
  for pt1 in ptsWithColor:
    new_state = check_legal(state,str(pt1)+','+str(pt1+die1), die1, die2)
    if (new_state != None):
        print(str(pt1)+','+str(pt1+die1))
        possibleStates.append(new_state)
    new_state = check_legal(state,str(pt1)+','+str(pt1+die2)+',R', die1, die2)
    if (new_state != None):
        print(str(pt1)+','+str(pt1+die2)+',R')
        possibleStates.append(new_state)
    new_state = check_legal(state,str(pt1)+',P', die1, die2)
    if (new_state != None):
        print(str(pt1)+',P')
        possibleStates.append(new_state)
    new_state = check_legal(state,str(pt1)+',P,R', die1, die2)
    if (new_state != None):
        print(str(pt1)+',P,R')
        possibleStates.append(new_state)
    for pt2 in ptsWithColor:
      new_state = check_legal(state,str(pt1)+','+str(pt2), die1, die2)
      if (new_state != None):
        print(str(pt1)+','+str(pt2))
        possibleStates.append(new_state)
      new_state = check_legal(state,str(pt1)+','+str(pt2) + ',R', die1, die2)
      if (new_state != None):
        print(str(pt1)+','+str(pt2) + ',R')
        possibleStates.append(new_state)
  return possibleStates

def check_legal(current_state, move, die1, die2):
  '''return a new state if leagal, return NONE if not,
  assuming move is a string and current_state is legal
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
      current_state=new_state
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

print(staticEval(bgstate()))