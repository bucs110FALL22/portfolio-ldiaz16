uewchewlj;k gek'gm
oethmpo4t4toclass StringUtility:
  def __init__(self, string):
    self.newString = string
    

  def __str__(self):
    return self.newString

  def vowels(self):
    s1 = self.newString
    vowels = ['a','i','e','o','u']
    count = 0
    ret_str = ''
    for i in range(len(s1)):
      if s1[i] in vowels:
        count = count + 1
    if count >= 5:
      ret_str = 'many'
    else:
      ret_str = str(count)
    return ret_str
    
  #Count the number of vowels in the string, and return a new string of the form '<count>', where <count> is the number of vowels in the string as a string However, if the count is 5 or more, then return the word 'many' instead of the actual count. So "Binghamton" returns '3' and "Incomprehensibilities" returns 'many'
    
  def bothEnds(self):
    s1 = self.newString
    length = len(s1)
    s2 = ''
    temp_char = ''
    if len(s1) >= 3:
      for i in range(0,2):
        temp_char = s1[i]
        s2 = s2 + temp_char
      temp_char = s1[length-2]
      s2 = s2 + temp_char
      temp_char = s1[length-1]
      s2 = s2 + temp_char
    elif len(s1) < 3:
      s2 = ''
    return s2
#return a string made of the first 2 and last 2 chars of the original string, so 'spring' yields 'spng'. However, if the string length is less than or equal to 2, return an empty string instead.

  def fixStart(self):
    s1 = self.newString
    if len(s1) <= 1:
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

    #return a string where all occurrences of its first char have been changed to '*', _except do not change the first char itself_. e.g. 'babble' yields 'ba**le'. If the parameter is length 1 or less, return the parameter as is.

  def asciiSum(self):
    s1 = self.newString
    temp_num = 0
    sum = 0
    for i in range(len(s1)):
      temp_num = ord(s1[i])
      sum += temp_num
    return sum

#return an integer that is the sum of all ascii values in the string.

  
  def cipher(self):
    s1 = self.newString
    s2 = ''
    alpha_num = 0
    num_list = []
    length = len(s1)
    print(length)
    let = ''
    for i in range(len(s1)):
      alpha_num = ord(s1[i])
      if alpha_num != 32:
        alpha_num = alpha_num + length
      while alpha_num > 122:
        alpha_num = (alpha_num - 122) + 96
      while alpha_num >= 91 and alpha_num <= 96:
        alpha_num = (alpha_num - 91) + 65
      num_list.append(alpha_num)
    for i in num_list:
      let = chr(i)
      s2 = s2 +  let
    return s2

    #return an encoded string by incrementing all letters by the length of the string. You should leave any characters that are not letters unchanged. For example, the string "Dog" would be shifted by 3, resulting in "Grj", while "Horse" would become "Mtwxj" because it shifts by 5 characters. You must account for wrap around (z=>a). Uppercase always wraps around to upper case, and lowercase always wraps around to lower case. 




  

    
