cr=eval(input())
cr<=1000
if(cr>1):
  for i in range(2,cr):
    if(cr%i==0):
      print("no")
      break
  else:
    print("yes")
else:
  print("no")
