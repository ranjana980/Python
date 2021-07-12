def index():
  i=0
  b=0
  while i<3:
    userinput=int(input("enter the number"))
    i=i+1
    b=b+userinput
  print("sum of number is",b)
  print("average of numbers",b//3)

index()