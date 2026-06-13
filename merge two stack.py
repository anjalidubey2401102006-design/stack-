class stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
s1=stack()
s2=stack()
num1=int(input("enter the range of the elements in stack1:"))
for i in range(num1):
    n=int(input("enter the elements:"))
    s1.push(n)
num2=int(input("enter the range of elements in stack2:"))
for i in range(num2):
    n=int(input("enter the elements:"))
    s2.push(n)
merge=s1.items+s2.items
print("merged stack",merge)