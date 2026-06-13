class stack:
    def __init__(self):
        self.items=[]
    def push(self,items):
        self.items.append(items)
s=stack()
for i in range(5):
    num=int(input("enter the numbers:"))
    s.push(num)
print("stack contents:",s.items)