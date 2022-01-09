import pygame
from sys import exit

# global variables / variaveis globais
WINDOW_WIDTH = 800
WINDOW_LENGTH = 800
SCREEN = None

#global colors
BLACK = (0, 0, 0)
GREY = (150, 150, 150)

"""
  drawGrid will be responsible for drawing the grid for the game of life
"""
def drawGrid():
  global WINDOW_WIDTH, WINDOW_LENGTH, WHITE
  
  #size of squares
  blockSize = 15

  
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
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    
    pygame.display.update()


if __name__ == "__main__":
  main()