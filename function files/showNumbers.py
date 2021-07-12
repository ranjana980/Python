def shownumbers(limit):
  i=0
  while i<=limit:
    if i%2==0:
      print("even")
    else:
        print("odd")
    i=i+1

shownumbers(100)