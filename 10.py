n = int(input("Enter the number\n"))
for i in range(n) :
    fact = n * fact(n-1) 
    if (n == 1):
        print("1")
    elif (n==0) :
        print("1")    
    else :    
      print(fact)
    