
def percentage_to_letter(score):
  if score >= 90:
    return "A"
  elif score >= 80:
    return 'B'
  elif score >= 70:
    return 'C'
  elif score >= 60:
    return 'D'
  else:
    return 'F'


def is_passing(letter):
  return letter in 'ABC'
  
def main():
  grade = int(input("Enter your grade from this assignment/assessment: "))
  letter_grade = percentage_to_letter(grade)
  print("Your grade was a",letter_grade)
  pass_boolean = is_passing(letter_grade)
  print("You passed this assignment:",pass_boolean)

main()