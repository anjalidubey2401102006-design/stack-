class stack:
    def __init__(self):
        self.items=[]
    def push(self,items):
        self.items.append(items)
s=stack()
n=int(input("Enter the range of elements:\n"))
for i in range(n):
    num=int(input("Enter the number:\n"))
    s.push(num)
print("stack from Top to Bottom:")
for i in range(len(s.items)-1,-1,-1):
    print(s.items[i])