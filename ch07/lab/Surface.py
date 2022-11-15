class Rectangle:
  def __init__(self,x,y,h,w):
    if x < 0:
      x = 0
    if y < 0:
      y = 0
    if h < 0: 
      h = 0
    if w < 0:
      w = 0
    self.x = x
    self.y = y
    self.height = h
    self.width = w
    self.rec = [self.x, self.y, self.height, self.width]
    
  def get_str(self):
    recstr = f'(x : {self.x}, y: {self.y}) width: {self.width}, height: {self.height} '
    # "(x : 5, y: 7) width: 10, height: 10", where the integers are the values of the instance variables
    
class Surface:
   def __init__(self, filename, x, y, h, w):
     self.rect.x = x
     self.rect.y = y
     self.rect.h = h
     self.rect.w = w
     self.image = filename
   def getRect(self):
     self.myrec = []
     for i in range(4):
       self.myrec.append(self.)
     
     
 