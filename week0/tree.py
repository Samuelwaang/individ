def triangle(n):
  for i in range(n):
      for j in range(n-i):
          print(' ', end=' ')
      for k in range(2*i+1):
          print('^',end=' ')
      print()
  
  # Generating recatngle shape
def rectangle(n):
  for i in range(n):
      for j in range(n-1):
          print(' ', end=' ')
      print('| | |')
    
def treeprint():
  row = int(input('rows: '))
  triangle(row)
  triangle(row)
  triangle(row)
  rectangle(row)

