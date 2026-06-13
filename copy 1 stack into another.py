class stack:
    def __init__(self):
        self.items=[]
    def push(self,items):
        self.items.append(items)
s1=stack()
s2=stack()
num=int(input("enter the range of elements:"))
for i in range(num):
    n=int(input("enter the elements:"))
    s1.push(n)
for j in s1.items:
    s2.push(j)
print("original stack:",s1.items)
print("copied stack:",s2.items)