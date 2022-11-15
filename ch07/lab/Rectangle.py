class Rectangle:
  def __init__(self,x,y,h,w):
    if x < 0 or y < 0 or h < 0, w < 0:
      print("Invalid rectangle value")
      main()
    self.x = x
    self.y = y
    self.height = h
    self.width = w
  def get_str(self):
    recstr = f'(x : {self.x}, y: {self.y}) width: {self.width}, height: {self.height} '
    # "(x : 5, y: 7) width: 10, height: 10", where the integers are the values of the instance variables
    
