class stack:
    def __init__(self):
        self.items=[]
    def push(self,items):
        self.items.append(items)
s=stack()
n=int(input("enter the range of elements:"))
for i in range(n):
    num=int(input("enter the elements:"))
    s.push(num)
largest=s.items[0]
for k in s.items:
    if k>largest:
        largest=k
print("Largest element:",largest)