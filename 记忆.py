import random
import time
import os
print("Hi,you have 10s to memory thr object name and its number")
things=["apple","banana","orange","soccer","penalty","blue","red","tea","coke","ten"]
for i in range(10):
    print(i,":",things[i])
time.sleep(10)
i=os.system("cls")
n=0
t2=random.sample(things,5)
for i in t2:
    ans=int(input(i+"的编号是："))
    if i==things[ans]:
        n=n+1
print("\nYou got",n,"times right")
input("\nenter to end the program")