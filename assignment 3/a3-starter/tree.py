class node:
  def __init__(self, state, static_value=None, children=None):
    self.state = state
    self.static_value = static_value
    if children:
      self.children = children
    else:
      self.children = []
  
  def add(self,state):
    new_node = node(state)
    self.children.append(new_node)
    return new_node

  #assuming state is bgstate type
  def remove(self,key):
    for n in self.children:
      if(
        n.bar == key.bar[:] and
        n.white_off == key.white_off[:] and
        n.red_off == key.red_off[:] and
        n.cube == key.cube and
        n.offering_double == key.offering_double and
        n.whose_move == key.whose_move and
        n.pointLists == key.pointLists]
      ):
        return self.children.pop(n)
      

class tree:
  def __init__(self):
    self.root = None

# Minimax Pseudocode
alpaBetaMinimax(node, alpha, beta) 

   """ 
   Returns best score for the player associated with the given node.
   Also sets the variable bestMove to the move associated with the
   best score at the root node.  
   """

   # check if at search bound
   if node is at depthLimit
      return staticEval(node)

   # check if leaf
   children = successors(node)
   if len(children) == 0
      if node is root
         bestMove = [] 
      return staticEval(node)

   # initialize bestMove
   if node is root
      bestMove = operator of first child
      # check if there is only one option
      if len(children) == 1
         return None

   if it is MAX's turn to move
      for child in children
         result = alphaBetaMinimax(child, alpha, beta)
         if result > alpha
            alpha = result
            if node is root
               bestMove = operator of child
         if alpha >= beta
            return alpha
      return alpha

   if it is MIN's turn to move
      for child in children
         result = alphaBetaMinimax(child, alpha, beta)
         if result < beta
            beta = result
            if node is root
               bestMove = operator of child
         if beta <= alpha
            return beta
      return beta

  

