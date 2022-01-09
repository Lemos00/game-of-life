class cell:
  def __init__(self):
    self.alive = False
    self.neighbors = set()

  def isAlive(self):
    return self.alive
  
  def addNeighbor(self, newNeighbor):
    self.neighbors.add(newNeighbor)
  
  def getNeighbors(self):
    return self.neighbors

  