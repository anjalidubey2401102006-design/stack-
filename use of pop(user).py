class stack:
    def __init__(self):
        self.items=[]
    def push(self,items):
        self.items.append(items)
    def pop(self):
        if len(self.items)==0:
            print("stack is empty")
        else:
            return self.items.pop()
s=stack()
for i in range(5):
    num=int(input("enter the numbers:"))
    s.push(num)
print("stack before pop:",s.items)
removed=s.pop()
print("popped element:",removed)
print("stack elements now:",s.items)