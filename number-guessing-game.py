
import random 
n=random.randint(1,100)
a=-1
guesses =0
while (a!=n):
   guesses +=1
   a=int(input("enter your guess :"))
   if (a>n):
         print("lower number than",a,"pls")
   elif (a<n) :
         print("higher number than ",a,"pls")
print(f"You guessed the number {n} correctly yahoo! in {guesses} attempt")        