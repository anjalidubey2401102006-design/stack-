class stack:
    def __init__(self):
        self.items=[]
    def push(self,items):
        self.items.append(items)
s=stack()
num=int(input("enter the range:"))
for i in range(num):
    n=int(input("enter the element:"))
    s.push(n)
k=0
for j in s.items:
    k=k+j
print("sum=",k)