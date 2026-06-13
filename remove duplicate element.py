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
new_stack=[]
for j in s.items:
    if j not in new_stack:
        new_stack.append(j)
print("after removing duplicate:",new_stack)