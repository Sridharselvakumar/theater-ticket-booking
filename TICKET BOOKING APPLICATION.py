import time
from time import sleep

print("----> [ WELCOME TO --ROON CINEMAS-- TICKET BOOKING APPLICATION ] <---- ")
print("----> CREATE ACCOUNT  <----")
n = input("CREATE YOUR USERNAME :")
m = input("CREATE YOUR PASSWORD :")
dob=input("ENTER THE DOB DD/MM/YYYY :")
print("----> LOGIN ACCOUNT <----")
o = input("ENTER YOUR USERNAME :")
p = input("ENTER YOUR PASSWORD :")    ##ENTER INCORRECT PASSWORD TO USE FORGET PASSWORD OPTION ##
if n == o and m == p:
    print("*** LOGIN SUCCESSFULLY ***")
elif n != o and m != p:
    print("*** INCORRECT USERNAME OR PASSWORD ***")
    q = input("IF YOU FORGOT PASSWORD TYPE YES :")
    if q=="YES" or q=="yes":
        db=(input("ENTER YOUR DOB (DD/MM/YYYY) :"))
        if dob==db:
            print("YOUR ACCOUNT HAS BEEN VERIFIED")
            m = input("ENTER YOUR NEW PASSWORD:")
            print("*** PASSWORD CHANGED SUCCESSFULLY ***")
            print("----> LOGIN ACCOUNT <----")
            o = input("ENTER YOUR USERNAME :")
            p = input("ENTER YOUR PASSWORD :")
            if o==n and p==m:
                print("*** YOUR ACCOUNT LOGIN SUCCESSFULLY ***")
print("[------->   WELCOME TO ROON CINEMAS   <-------]")
print(" ----- MOVIE LIST -----")
mov={'SCREEN _N0': "MOVIE_NAME",
     1: "AVENGERS",
     2: "ENG GAME",
     3: "SPIDER MAN",
     4: "IRON MAN",
     5: "CAPTAIN AMERICA"}
for key, values in mov.items():
    print(f" {key} : {values}")
s=int(input("ENTER THE SCREEN NUMBER TO SELECT MOVIE :"))
if s==1:
    print("----->  SELETED MOVIE NAME IS :",mov[1])
elif s==2:
    print("----->  SELETED MOVIE NAME IS :",mov[2])
elif s==3:
    print("----->  SELETED MOVIE NAME IS :",mov[3])
elif s==4:
    print("----->  SELETED MOVIE NAME IS :",mov[4])
elif s==5:
    print("----->  SELETED MOVIE NAME IS :",mov[5])
else:
    print(" *** INVALID SCREEN NUMBER *** ")

q=int(input("ENTER THE NUMBER OF TICKETS : "))
r=q*150
print("YOUR TICKET PRICE IS :",r)

t=int(input("ENTER YOUR PIN NUMBER :"))
import time
if t>=0:
    print("..... PROCESSING.....")
    time.sleep(5)
    print(" *** BOOKING SUCCESSFUL ***")











