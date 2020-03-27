def recur_fibo(n): 
   #print(n) 
   if n <= 1:  
       return n  
   else:  
       return(recur_fibo(n-1) + recur_fibo(n-2))  
# take input from the user  
nterms = int(input("How many terms? "))  
# check if the number of terms is valid  
if nterms <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(0, nterms): 
       print(recur_fibo(i))  


# 0, 1, 2, 3

# 0
# 1

1. 0 
2. 1
3. func(2-1) + func(2-2) = 1
	1
