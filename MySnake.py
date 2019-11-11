import pygame

class Square:
  
  def __init__(self, h, w):
    self.h = h
    self.w = w
    
  def draw_square(surface):
    pygame.draw.rect(surface, (255,255,255), (250, 250, 10,10))


def drawGrid(surface, n_squares, x_dim, y_dim):
  
  delta_x = x_dim//n_squares
  delta_y = y_dim//n_squares
  
  x = 0
  y = 0
  
  for i in range(n_squares+1):
    
    # horizontal line
    pygame.draw.line(surface, (0, 255, 0), (0, y),(x_dim, y))
    # vertical line
    pygame.draw.line(surface, (0, 255, 0), (x, 0),(x, y_dim))
    
    x += delta_x
    y += delta_y

def main():
  pygame.init()
  window = pygame.display.set_mode((500,500))
  pygame.display.set_caption("MySnake")
  
  drawGrid(window, 10, 500, 500)
  s = Square(10, 10)
  s.draw_square(window)
  pygame.display.update()
  print("Works")
  
  run = True
  while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        
main()
