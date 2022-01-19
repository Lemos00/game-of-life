import pygame
from sys import exit

def drawitself(a,b,alive): #(coordinates/alive state) :
    #only draws if cell is alive
    if alive:
        blockSize = 15
        Rect = pygame.Rect(a, b, blockSize, blockSize)
        pygame.draw.rect(SCREEN, GREY, Rect, width=blockSize)
    else:
        pass

class cell:
  def __init__(self,a,b):
    self.alive = True
    self.neighbors = set()
    self.coordinates = [a,b] #cell coordinates
    self.appear = drawitself(a,b,self.alive) 

  def isAlive(self):
    return self.alive
  
  def addNeighbor(self, newNeighbor):
    self.neighbors.add(newNeighbor)
  
  def getNeighbors(self):
    return self.neighbors

# global variables / variaveis globais
WINDOW_WIDTH = 720
WINDOW_LENGTH = 720
SCREEN = None
blockSize = 15
#global colors
BLACK = (0, 0, 0)
GREY = (150, 150, 150)

"""
  drawGrid will be responsible for drawing the grid for the game of life
"""
def drawGrid():
  global WINDOW_WIDTH, WINDOW_LENGTH, WHITE, blockSize
  
  #size of squares
  

  for x in range(0, WINDOW_WIDTH, blockSize):
    for y in range(0, WINDOW_LENGTH, blockSize):
      rect = pygame.Rect(x, y, blockSize, blockSize)
      pygame.draw.rect(SCREEN, GREY, rect, 1)
  
  # create caption for game window
  pygame.display.set_caption("Game of Life")


def main():
  #execute window and display it
  global WINDOW_WIDTH, WINDOW_LENGTH, SCREEN, BLACK
  #initialize pygame
  pygame.init()

  SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_LENGTH))
  SCREEN.fill(BLACK)

  # infinite loop to keep game running
  while (True):
    drawGrid()
    cell(0,0) #create the cells


    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    
    pygame.display.update()

#def GenerateCoordinates():
    #global WINDOW_WIDTH, WINDOW_LENGTH, blockSize

    #numberOfColumns = WINDOW_WIDTH / blockSize
    #numberOfLines = WINDOW_LENGTH / blockSize
    


if __name__ == "__main__":
  main()

