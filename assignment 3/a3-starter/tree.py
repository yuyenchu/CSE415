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

  




