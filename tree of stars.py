print("Hello!, Welcome to here!")
print("we're gonna play this game!")
print("we're gonna build a tree of stars!!")
n=int(input("Enter a number n that is odd:"))
c=input("Enter a valid character:")
if (n%2==0):
  print("No game")
else: 
  for i in range (1,n,2):
    print(" "*((n-i)//2)+c*i+" "*((n-i)//2))
  print(" "*((n-2)//2)+"[]")