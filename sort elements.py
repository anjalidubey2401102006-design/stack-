class stack:
    def __init__(self):
        self.items=[]
    def push(self,items):
        self.items.append(items)
s=stack()
num=int(input("enter the range of elements:"))
for i in range(num):
    n=int(input("enter the elements:"))
    s.push(n)
s.items.sort()
print("sorted stack:",s.items)