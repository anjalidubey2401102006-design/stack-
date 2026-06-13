class stack:
    def __init__(self):
        self.items=[]
    def push(self,items):
        self.items.append(items)
s=stack()
n=int(input("Enter the range of elements:"))
for i in range(n):
    num=int(input("enter the elements:"))
    s.push(num)
k=int(input("search:"))
if k in s.items:
    print("element found")
else:
    print("element not found")