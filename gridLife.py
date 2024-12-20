class cell:
  def __init__(self, row, column, width, totalRows, aliveColor, deadColor):
    self.row = row
    self.col = column
    self.x = self.row * width
    self.y = self.col * width
    self.alive = False
    self.aliveColor = aliveColor
    self.deadColor = deadColor

  def getColor(self):
    if self.alive:
      return self.aliveColor
    
    return self.deadColor

  def getAlive(self):
    return self.alive
  
  def setAlive(self, newState):
    self.alive = newState
  
  def getPositionXY(self):
    return (self.x, self.y)

  def getPosition(self):
    return (self.row, self.col)