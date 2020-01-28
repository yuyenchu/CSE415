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

  

