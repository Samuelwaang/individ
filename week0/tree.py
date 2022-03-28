def tree(n):
  for tr in range(n):
      for space in range(n-tr):
          print(' ', end=' ')
      for leaf in range(2*tr+1):
          print('^',end=' ')
      print()
      for bark in range(n-1):
          print('  ', end=' ')
      print('||')

def treeprint():
  row = int(input('rows: '))
  tree(row)

