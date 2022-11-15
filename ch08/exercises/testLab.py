class string:
  def __init__(self,string):
    self.newString = string
  def fixStart(self):
    
    s1 = self.newString
    if len(s1) <= 2:
      return s1
    first_char = s1[0]
    test = ''
    length = len(s1)
    s2 = s1[1:length]
    s3 = first_char
    for i in range(len(s2)):
      test = s2[i]
      if test == first_char:
        test = '*'
      s3 = s3 + test
    return s3

def main():
  test_strings = ["interesting", "aardvark", "aaa", "aeiouAEIOU", "a b c d e f g h i j k l m n o p q r s t u v w x y z", '']
  su = []
  for i in test_strings:
    su.append(string(i))
  for s in su:
    result = s.fixStart()
    print(result)

main()
