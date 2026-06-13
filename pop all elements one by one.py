class stack:
    def __init__(self):
        self.items=[]
    def push(self,items):
        self.items.append(items)
    def pop(self):
        return self.items.pop()
s=stack()
n=int(input("enter the range of elements:"))
for i in range(n):
    num=int(input("enter the elements:"))
    s.push(num)
print("popped elements:")
while len(s.items)>0:
    print(s.pop())