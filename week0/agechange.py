def ageChange(age1, age2):
      #print(age1, age2)
      if (age1 > age2):
          num = age1
          age1 = age2
          age2 = num
      return age1,age2

def agePrint ():
  print( ageChange(16, 21) )
  print ( ageChange(21, 16) )


