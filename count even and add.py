class stack:
    def __init__(self):
        self.items=[]
    def push(self,items):
        self.items.append(items)
s=stack()
n=int(input("enter the range of elemnts:"))
for i in range(n):
    num=int(input("enter the elements:"))
    s.push(num)
even=0
odd=0
for j in s.items:
    if j%2==0:
        even+=1
    else:
        odd+=1
print("Even numbers:",even)
print("odd numbers:",odd)