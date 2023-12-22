def division(a, b):
  integer_part = str(a // b)  
  remainder = a % b 

  if remainder == 0:
      return integer_part  

  decimal_part = ""  
  remainder_map = {}  
  index = 0

  while remainder != 0 and remainder not in remainder_map:
      remainder_map[remainder] = index 
      remainder *= 10
      decimal_part += str(remainder // b)  
      remainder = remainder % b
      index += 1

  if remainder == 0:
      return integer_part + "." + decimal_part  

  recurring_part = decimal_part[remainder_map[remainder]:] 
  decimal_part = decimal_part[:remainder_map[remainder]] + "(" + recurring_part + ")"
  return integer_part + "." + decimal_part

a = int(input("Введите числитель: "))
b = int(input("Введите знаменатель: "))

print(division(a, b))